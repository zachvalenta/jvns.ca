---
title: "How does the Kubernetes scheduler work?"
date: 2017-07-27T21:07:12Z
draft: true
url: /blog/2017/07/27/how-does-the-kubernetes-scheduler-work-/
categories: []
---

Hello!  We talked about Kubernetes' [overall architecture](https://jvns.ca/blog/2017/06/04/learning-about-kubernetes/) a while back.

This week I learned a few more things about how the Kubernetes scheduler
works so I wanted to share! This kind of gets into the weeds of how the
scheduler works *exactly*.

### what is the scheduler for?

The Kubernetes scheduler is in charge of scheduling pods onto nodes.
Basically it works like this:

1. You create a pod
2. The scheduler notices that the new pod you created doesn't have a node assigned to it
3. The scheduler assigns a node to the pod

It's not responsible for actually *running* the pod -- that's the
kubelet's job. So it basically just needs to make sure every pod has a
node assigned to it. Easy, right?

So basically you could imagine the scheduler running a loop like this:

```
while True:
    pods = get_all_pods()
    for pod in pods:
        if pod.node == nil:
            assignNode(pod)
```

If you are not that interested in how the Kubernetes scheduler works you
can probably stop reading now -- this is a pretty reasonable model of
how it works.

I thought the scheduler **actually** worked this way because this is how the
[cronjob controller](https://github.com/kubernetes/kubernetes/blob/e4551d50e57c089aab6f67333412d3ca64bc09ae/pkg/controller/cronjob/cronjob_controller.go) 
works and that was the only Kubernetes component code I'd really read.
The cronjob controller basically iterates through all cronjobs, sees if
it has to anything to do for any of them, sleeps for 10 seconds, and
repeats forever. Super simple!

### this isn't how it works though

So! This week we were putting a little more load on our Kubernetes
cluster, and we noticed a problem.

Sometimes a pod would get stuck in the `Pending` state (with no node
assigned to it) forever. If we restarted the scheduler, the pod would
get unstuck. ([this issue](https://github.com/kubernetes/kubernetes/issues/49314))

This didn't really match up with my mental model of how the Kubernetes
scheduler worked -- surely if a pod is waiting for a node to be
assigned, the scheduler should notice and assign that pod a node. The
scheduler shouldn't have to be restarted!

So I went and read a lot of code. Here is what I learned about how the
scheduler actually works!

### how the scheduler works: a very quick code walkthrough

This is basically just what I figured out from reading the code, it's possible
I have something wrong here.

We'll start in [scheduler.go](https://github.com/kubernetes/kubernetes/blob/e4551d50e57c089aab6f67333412d3ca64bc09ae/plugin/pkg/scheduler/scheduler.go). (I actually [concatenated all the files in the scheduler together](https://gist.github.com/jvns/5d492d66130a2f47b47820fd6b52eab5) which I found helpful for jumping around and navigating.)

The core loop in the scheduler (as of commit e4551d50e5) is:

([link](https://github.com/kubernetes/kubernetes/blob/e4551d50e57c089aab6f67333412d3ca64bc09ae/plugin/pkg/scheduler/scheduler.go#L150-L156))

```
go wait.Until(sched.scheduleOne, 0, sched.config.StopEverything)
```

This basically means "run `sched.scheduleOne` forever". Cool, what does that do?

```
func (sched *Scheduler) scheduleOne() {
	pod := sched.config.NextPod()
    // do all the scheduler stuff for `pod`
}
```

Okay, what is this `NextPod()` business? Where does that come from?

```
func (f *ConfigFactory) getNextPod() *v1.Pod {
	for {
		pod := cache.Pop(f.podQueue).(*v1.Pod)
		if f.ResponsibleForPod(pod) {
			glog.V(4).Infof("About to try and schedule pod %v", pod.Name)
			return pod
		}
	}
}
```

Okay, that's pretty simple! There's a queue of pods (`podQueue`) and the next
pod comes from that queue.

But how do pods end up on that queue? Here's the code that does that:

```go
	podInformer.Informer().AddEventHandler(
		cache.FilteringResourceEventHandler{
			Handler: cache.ResourceEventHandlerFuncs{
				AddFunc: func(obj interface{}) {
					if err := c.podQueue.Add(obj); err != nil {
						runtime.HandleError(fmt.Errorf("unable to queue %T: %v", obj, err))
					}
				},
```

Basically there's an event handler that, whenever a new pod is added,
puts it on the queue.

### how the scheduler works, in English

Okay now that we've looked through the code, here's a summary in
English:

1. At the beginning, every pod that needs scheduling gets added to a queue
2. When new pods are created, they also get added to the queue
3. The scheduler continuously takes pods off that queue and schedules them
4. That's it

One interesting thing here is that -- if for whatever reason a pod **fails** to
get scheduled, there's nothing in here yet that would make the scheduler retry.
It'd get taken off the queue, it fails scheduling, and that's it. It lost its
only chance! (unless you restart the scheduler, in which case everything will
get added to the pod queue again)

Of course Kubernetes is actually smarter than that -- when a pod fails to schedule, in general it calls an error handler, like this:

```
	host, err := sched.config.Algorithm.Schedule(pod, sched.config.NodeLister)
	if err != nil {
		glog.V(1).Infof("Failed to schedule pod: %v/%v", pod.Namespace, pod.Name)
		sched.config.Error(pod, err)
```

This `sched.config.Error` function call adds the pod back to the queue
of things that need to be scheduled, and so it tries again.

### wait why did our pod get stuck then?

This is pretty simple -- it turned out that the `Error` function wasn't
always being called when there was an error. We made a patch to call the
`Error` function properly and that seems to have made it recover
properly! Cool!

### why is the scheduler designed this way?

I feel like this design would be more robust:

```
while True:
    pods = get_all_pods()
    for pod in pods:
        if pod.node == nil:
            assignNode(pod)
```

so why is it instead this more complicated thing with caches and queues?
I looked at the history a bit and I think it's basically for performance
reasons -- for example you can see this post from CoreOS about
[improving Kubernetes scheduler performance](https://coreos.com/blog/improving-kubernetes-scheduler-performance.html). That post says it improved the time to schedule 30,000 pods from 14 minutes to 10 minutes. That post says it improved the time to schedule 30,000 pods from 2 hours to 10 minutes. 2 hours is pretty slow! performance is important!

So it makes sense to me that it would be too slow to query for all
30,000 pods in your system every time you want to schedule a new pod.

### understanding how software works is fun!

So far I think Kubernetes has been pretty good to work with -- I find
the code pretty easy to understand when I read it.

But the experience of using Kubernetes so far is definitely not that it
"just works" -- it feels more like 

1. learn the basics of how a component is supposed to work
2. run into some subtleties/problems
3. read the code or do some experimentation to learn how it actually
   works
4. reading the code is pretty easy because it's in Go and usually the
   code makes sense
5. contribute an improvement if necessary (so far Kubernetes seems to be really really awesome
   at reviewing PRs)

So it's more like "this software's design seems reasonable, and it has a
lot of really great people actively working on it, and it's very
possible to fix the problems you run into, but there will probably be
problems and you have to be willing to invest in finding and fixing
them".

### how do you approach a new piece of software?

I feel like there are maybe 2 kinds of software -- with something like
nginx or HAProxy I basically assume it will "just work". Like if I
wanted a production webserver, I'd just start using nginx, assume
that works the way it's documented and that's it.

But with Kubernetes (and maybe Docker? My understanding of Docker is
bad), and maybe any complex system that's being very actively developed,
I think it's appropriate to approach it a lot more cautiously -- like
you can't just set it up and assume it does what the documentation says.
Instead I feel like I have to do a lot more testing and learning and
source-code-reading and rolling-it-out-carefully.

(though this isn't true with the Linux kernel, which is very complicated
and very actively developed -- certainly we run into kernel bugs from
time to time but I have quite a lot of confidence that kernel releases
will generally behave the way they're supposed to.)
