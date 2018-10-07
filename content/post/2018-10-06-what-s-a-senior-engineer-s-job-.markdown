---
title: "What's a senior engineer's job?"
date: 2018-10-06T23:16:40Z
url: /blog/senior-engineer/
categories: []
---

There's this great post by John Allspaw called "[On being a senior engineer](https://www.kitchensoap.com/2012/10/25/on-being-a-senior-engineer/)". I originally read it
4ish years ago when I started my current job and it really influenced how I thought about the
direction I wanted to go on.

Rereading it 4 years later, one thing that's really interesting to me about that blog post is that
it's trying to show that empathy / helping your team succeed is an important part of being a senior
engineer. Which of course is true!

But from where I stand today, most (all?) of the senior engineers I know take on a significant
amount of helping-other-people work in addition to their individual programming work. The challenge
I see me/my coworkers struggling with today isn't so much "what?? I have to TALK TO PEOPLE??
UNBELIEVABLE." and more "wait, how do I balance all of this leadership work with my individual
contributions / programming work in a way that's sustainable for me? How much of what kind of work
should I be doing?". So instead of talking about the **attributes** that a senior engineer has from
Allspaw's post (which I totally agree with), instead I want to talk here about the **work** that a
senior engineer does.

### what this post is describing

"what a senior engineer does" is a huge topic and this is a small post. 2 things to keep in mind
when reading:

* this is just one possible description of what a "senior engineer" could do. There are a lot of ways
  to work and this isn't intended to be definitive.
* There are obviously a lot of levels of "senior engineer" out there. This is aimed somewhere around
  P3/P4 in the [Mozilla ladder](https://twitter.com/Gankro/status/1046438955439271936) (senior
  engineer / staff engineer), maybe a bit more on the "staff" side.

### What's part of the job

These are things that I view as being mostly a senior engineer's job and less a manager's job.
(though managers definitely do some of this too, especially creating new projects / relating
projects to business priorities)

The thing that holds all this together is that almost all of this work is fundamentally
**technical**: helping someone get unstuck on a tricky project is obviously a human interaction, but
the issues we'll be working on together will generally be computer issues! ("maybe if we simplify
this design we can be done with this way sooner!")

* **Write code.** (obviously)
* **Do code reviews.** (obviously)
* **Write and review design docs.** As with other review tasks, I think of "review design docs" less
   as "get a second set of eyes on it, which will probably help improve the design".
* **Help team members when they're stuck.** Sometimes folks get stuck on a project, and it's important
  to work to support them! I think of this less as "parachute from the sky and deliver your magical
  knowledge to people" and more as "work together to understand the problem they're trying to solve
  and see if 2 brains are better than 1" :). This also means working with someone to solve the
  problem instead of solving the problem for them.
* **Hold folks to a high quality standard.** "Quality" will mean different things for different folks
  (for my team it means reliability/security/usability). Usually when someone makes a decision that
  seems off to me, it's either because I know something that they don't or they know something I
  don't! So instead of telling someone "hey you did this wrong you should do X instead", I try to
  just give them some extra information that they didn't have and often that sorts it out. And
  pretty often it turns out that I was missing something and actually their decision was totally
  reasonable! In the past I've occasionally seen senior engineers handle disagreements by repeating
  their opinions more and more loudly because they think their opinions are Right and I haven't
  personally found that helpful.
* **Create new projects.** A software engineering team isn't a zero-sum place! The best engineers I know
  don't hoard the most interesting work for themselves, they create new interesting/important work
  and create space for folks to do that work. For example, someone on my team spearheaded a rewrite
  of our deployment system which was super successful and now there's a whole team working on new
  features that are way easier to build post-rewrite!
* **Plan your projects' work.** This is about writing down / communicating the roadmap for projects
  you're working on and making sure that folks understand the plan.
* **Proactively communicate project risks.** It's really important to recognize when something you're
  working on isn't going well, communicate it to other engineers/managers, and figure out what to
  do.
* **Communicate successes!**
* **Do side projects that benefit the team/company**. I see a lot of senior engineers occasionally
  doing small high leverage projects (like building dev tooling / helping set policies) that end up
  helping a LOT of people get their work done a lot better.
* **Be aware of how projects relate to business priorities.**
* **Decide when to stop doing a project**. Deciding when to **stop** (or not start) work on a
  project you're on is really important!

I put "write code" first because I find it surprisingly easy to accidentally let that take a back
seat :)

One thing I left out is "make estimates". Making estimates is something I'm still not very good at
and that I don't think I see very much of (?), but I think it could be worth spending more time on
some day.

This list feels like a lot and like it could easily grow to consume all available brain space. I
think in general it probably makes sense to carve out a subset and decide "right now I'm going to
focus on X Y Z, I think my brain will explode if I try to do A B C as well".

### What's not part of the job

I think it's very normal to help out with many of these sometimes, but these are things that I think
of as not being the job.

* Do sprint management / organize everyone's work into milestones / run weekly team meetings
* Make sure every team member's work is recognized
* Make sure work is allocated in a fair way
* Make sure folks are working well together
* Build team cohesion
* Have 1:1s with everyone on the team
* Train new managers / help them understand what's expected of them (though I think senior ICs often
  actually do end up picking some of this up?)
* Do project management for projects you're not working on
* Be a product manager

### Explicitly setting boundaries is useful

I ran into an interesting situation recently where I was talking to a manager about which things
were and weren't part of my job as an engineer, and we realized that we had very different
expectations! We talked about it and I think it's sorted out now, but it made me realize that it's
very important to agree about what the expectations are :)

When I started out as an engineer, my job was pretty straightforward -- I wrote code, tried to come
up with projects that made sense, and that was fine. My manager always had a clear sense of what my
job was and it wasn't too complicated. Now that's less true! So now I view it as being more my
responsibility to define a job that:

* I can do / is sustainable for me
* I want to do / that's overall enjoyable & in line with my personal goals
* is valuable to the team/organization

And the exact shape of that job will be different for different people (not everyone has the same
interests & strengths, for example I am actually not amazing at code review yet!), which I think
makes it even more important to negotiate it / do expectation setting. 

### Don't agree to a job you can't do / don't want

I think pushing back if I'm asked to do work that I can't do or that I think will make me unhappy
long term is important! I find it kind of tempting to agree to take on a lot of work that I know I
don't really enjoy ("oh, it's good for the team!", "well _someone_ needs to do it!"). But, while I
obviously sometimes take on tasks just because they need to be done, I think it's actually really
important for team health for folks to be overall doing jobs that are sustainable for them and that
they overall enjoy.

So I'll take on small tasks that just need to get done, but I think it's important for me not to say
"oh sure, I'll spend 25% of my time doing this thing that I'm bad at and that I dislike, no problem"
:). And if "someone" needs to do it, maybe that just means we need to hire/train someone new to fill
the gap :)

### I still have a lot to learn!

While I feel like I'm starting to understand what this "senior engineer" thing is all about (7 years
into my career so far), I still feel like I have a LOT to learn about it and I'd be interested to
hear how other people define the boundaries of their job!
