---
title: "A few things I've learned about Kubernetes"
draft: true
date: 2017-06-04T22:35:21Z
url: /blog/2017/06/04/learning-about-kubernetes/
categories: []
---

I've been learning about Kubernetes at work recently. It's been a pretty
slow road for me -- my partner Kamal has been excited about Kubernetes
for a few years (him: "julia! you can run programs without worrying what
computers they run on! it is so cool!", me: "I don't get it"), but I
understand it a lot better now.

This isn't a comprehensive explanation or anything it's just some things
I learned along the way that have helped me understand what's going on.

If you ever feel bad about taking a long time to learn stuff -- I have
apparently been learning things about Kubernetes for over 2 years. Kamal
tweeted in April 2015:

> spent an hour discussing kubernetes networking with @b0rk, with each
> of us coming from opposite ends of the abstraction. we both know more!

These days I am actually setting up a cluster instead of just hearing
about it on the internet and being like "what is that??" so I am learning
much faster :)

I'm not going to try to explain what Kubernetes is. I liked Kelsey
Hightower's introductory talk at Strange Loop called ["Managing Containers at Scale with CoreOS and Kubernetes"](https://www.youtube.com/watch?v=pozC9rBvAIs), and
Kelsey has given TONS of great kubernetes talks over the years if you want an intro.

Basically Kubernetes is a distributed system that runs programs
("containers") on computers.

### kubernetes from the ground up

One of first thing that helped me understand what was going on with
Kubernetes was Kamal's "Kubernetes from the ground up" series

He basically walks you through how all the Kubernetes components work
with each other one at a time -- "look, you can run the kubelet by
itself! And if you have a kubelet, you can add the API server and just
run those two things by themselves! Okay, awesome, now let's add the
scheduler!" I found it a lot easier to understand when presented like
this. Here's the 3 post series:

* Part 1: [the kubelet](http://kamalmarhubi.com/blog/2015/08/27/what-even-is-a-kubelet/)
* Part 2: [the API server](http://kamalmarhubi.com/blog/2015/09/06/kubernetes-from-the-ground-up-the-api-server/)
* Part 3: [the scheduler](http://kamalmarhubi.com/blog/2015/11/17/kubernetes-from-the-ground-up-the-scheduler/)

Basically these posts taught me that:

* the kubelet is in charge of running containers on nodes
* If you tell the API server to run a container on a node, it will tell the kubelet to get it done
* the scheduler translates "run a container" to "run a container on node
  X"

but you should read them in detail if you want to understand how these
components interact. Kubernetes stuff changes pretty quickly, but
I think the basic architecture like "how does the API server interact
with the kubelet" hasn't changed that much and it's a good place to
start

### etcd: kubernetes' brain

The next thing that really helped me understand how Kubernetes works is
understanding the role of etcd a little better.

Every component in Kubernetes (the API server, the scheduler, the
kubelet, the controller manager, whatever) is stateless. All of the
state is stored in a key-value store called etcd, and communication
between components often happens via etcd.

For example! Let's say you want to run a container on Machine X. You do not
ask the kubelet on that Machine X to run a container. That is not the
Kubernetes way! Instead, this happens:

1. you write into etcd, "This pod should run on Machine X". 
2. the kublet on Machine X looks at etcd and thinks, "omg!! it says that pod should be running and I'm not running it! I will start right now!!"

Similarly, if you want to put a container **somewhere** but you don't
care where:

1. you write into etcd "this pod should run somewhere"
2. the scheduler looks at that and thinks "omg! there is an unscheduled
   pod! This must be fixed!". It assigns the pod a machine (Machine Y) to run on
3. like before, the kubelet on Machine Y sees that and thinks "omg! that is scheduled to run on my machine! Better do it now!!"

When I understood that basically everything in Kubernetes works by
watching etcd for stuff it has to do, doing it, and then writing the new
state back into etcd, Kubernetes made a lot more sense to me.

### The API server is responsible for putting stuff into etcd

Understanding etcd also helped me understand the role of the API server
better! The API server has a pretty straightforward set of
responsibilities:

1. you tell it stuff to put in etcd
2. if what you said makes no sense (doesn't match the right schema),
   it refses
3. otherwise it does it

That's not too hard to understand!

It also manages authentication ("who is allowed to put what stuff into
etcd?") which is a pretty big deal but I'm not going to go into that
here. This [page on Kubernetes
authentication](https://kubernetes.io/docs/admin/authentication/) is
pretty useful, though it's kind of like "HERE ARE 9 DIFFERENT
AUTHENTICATION STRATEGIES YOU COULD USE". As far as I can tell the
normal way is X509 client certs.

### kubernetes components can run inside of kubernetes

One thing that kind of blew my mind was that -- relatively core
Kubernetes components (like the DNS system) can run inside of
Kubernetes! "hey, kubernetes, please start up the DNS system!"

This is basically because in order to run programs inside Kubernetes,
you only need a few things running:

* the scheduler
* the API server
* etcd
* kubelets on every node

Once you have those 4 things, you can schedule containers to run on
nodes! So if you want to run another Kubernetes component (like your
overlay networking, or the DNS server, or anything else), you can just
ask the API server (via `kubectl apply -f your-configuration-file.yaml`)
to schedule it for you and it'll run it!

There's also
[bootkube](https://github.com/kubernetes-incubator/bootkube) where you
run *all* kubernetes components inside Kubernetes (even the API server)
but that's a research project right now. Running stuff like the DNS
server inside Kubernetes seems pretty normal.

### kubernetes networking: not impossible to understand

[this page](https://kubernetes.io/docs/concepts/cluster-administration/networking/)
does a pretty good job of explaining the Kubernetes networking model
"every container gets an IP" but understanding how to actually make that
happen is not trivial!

When I started learning about Kubernetes networking I was the most
confused about how you give every container an IP address. In retrospect I think
this was because I didn't understand some of the fundamental networking
concepts involved yet (to understand what an "overlay network" is and
how it works you actually need to understand a bunch of things about
computer networking!)

Now I feel mostly able to set up a container networking thing
and like I know enough concepts to debug problems I run into! I wrote 
[a container networking overview](https://jvns.ca/blog/2016/12/22/container-networking/) where I
tried to summarize some of what I've learned.

This summary of how Sophie debugged a kube-dns problem ([misadventures with kube-dns](http://blog.sophaskins.net/blog/misadventures-with-kube-dns/)) is a good example
of how understanding fundamental networking concepts can help you debug
problems.

### concepts that have helped me understand Kubernetes

* distributed reliable key-value store (to understand what's up with
  etcd and operating it), Raft, consistency guarantees

for networking:

* overlay networks (I wrote [a container networking overview ](https://jvns.ca/blog/2016/12/22/container-networking/) about this last year)
* network namespaces (understanding namespaces in general is really
  helpful for working with containers)
* DNS (because kubernetes has a DNS server)
* route tables, how to run `ip route list` and `ip link list`
* network interfaces
* encapsulation (vxlan / UDP)
* TLS, server certs, client certs, certificate authorities

### the kubernetes source seems easy enough to read

The Kubernetes source code is all in Go which is great. The project
moves pretty fast so stuff isn't always documented (and you end up
reading github issues a lot to understand the current state of things),
but in general I find Go code eays to read and it's reassuring to know
that I'm working with something written in a language I can
understand.
