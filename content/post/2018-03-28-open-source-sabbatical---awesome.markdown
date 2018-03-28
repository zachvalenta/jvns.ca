---
title: "Open source sabbatical = awesome"
date: 2018-03-28T00:29:58Z
url: /blog/2018/03/28/open-source-sabbatical---awesome/
categories: ["ruby-profiler"]
---

Hello! This is my last week working on rbspy. I'm planning to write more about the profiler and how
it works soon, but I wanted to take a minute to talk (again) about how I ended up working on the
project and how it's funded. I want to talk about funding because it's an important part of how a
lot of open source software gets created and maintained!

Just about a year ago today (March 23, 2017) Segment announced their [Open Fellowship](https://segment.com/blog/segment-open-fellowship-2017/) -- funding for 3 months to work
on an open source project.

The blog post said:

> The primary goal of the fellowship is to enable participants to fully dedicate themselves to a project for a few months. We’re hoping to give them a chance to speed the adoption of a new, fast-growing project. Or maybe help them build some long-awaited key features of a library that’s already widely used. Or perhaps even jump-start an entirely new idea altogether.

When I saw this, my thought process went:

1. That sounds amazing!! I want to do that!
2. But what would I work on? Oh, I have this Ruby profiler prototype I built last year, maybe that??
   That would be fun and I think it might help a lot of people!
3. I'll apply and see what happens!

So I filled in the form, thinking "who knows if they'll accept me? I'll just apply and
see what happens!! If you're not getting rejections you're not being ambitious enough, julia!" and waited.
They accepted my application, and the project happened!!

### open source funding models

Before I talk about what made this fellowship + sabbatical work for me, I wanted to take a second to
catalog a few open source software funding models that I'm aware of:

* a company employs people who work on the software (like Hashicorp or Google or Mozilla or [Igalia](https://www.igalia.com/))
* companies who use the software donate to a software foundation (like the Linux foundation or 
  [Ruby Together](https://rubytogether.org/)) that pay developers to work on the project
* Crowdfunding with Patreon (successfully used by the [vue.js project](https://www.patreon.com/evanyou))
* [Google Summer of Code](https://summerofcode.withgoogle.com/) /
  [Outreachy](https://www.outreachy.org/) pay a ~$5000 stipend to students / folks from
  underrepresented groups to work on an open source project for 3 months. Participants get a mentor.
* Segment Open Fellowship / Stripe Open Source Retreat (pay someone to do 3 months of work on an
  open source project they choose)

There are certainly more that I'm leaving out but those are the ones I can think of right now.

One difference is that some models involve full-time employment and some models are about sponsoring
sprints of activity on a project. In this case, the "sprints of activity" model worked really well
for me.

### flexible starting time: very helpful

Originally, the fellowship was supposed to run from June 15 to September 15, 2017. Obviously I
didn't do it from June to September, because it's March now! So here's what happened. Segment offered me
the fellowship (yay!). I realized I couldn't take time off work by June 15, and told them so. They
(extremely kindly! said I could delay the fellowship until a later time that worked for me. I
suggested January -> March 2018 (6 months later) and they agreed to it!

Then I asked my manager if I could take 3 months off work in January (unpaid) to do the fellowship.
Since there was about 6 months notice (lots of time), we got permission to do it. Amazing!

I think it was **amazing** that Segment was so flexible about the dates of the fellowship -- their
flexibility (and Stripe's willingness to let me take 3 months off work) was what made it possible
for me to do this. Otherwise I probably won't have done this project.

### doing the fellowship remotely

The other thing that Segment did that I thought was amazing was -- they said it was totally fine if
fellowship participants did their projects remotely! This was important to me (I wouldn't have
applied otherwise) because, realistically, I wasn't going to move to San Francisco for 3 months to
do this project.

I blogged about my progress on and off as I went, which I think helped them feel like they knew what
was going on even though I wasn't in their office. They didn't ask that I do that, though -- they
were just supportive of me working in whatever way I chose to work.

Working from home is how I work usually so this felt pretty normal.

### sabbaticals are cool

I really like my job, and I didn't want to quit just to be able to dedicate some time to a project
that I was interested in. So I think it's awesome that I was able to take time off work to do the
project. I've been at Stripe for 4 years, so Stripe's sabbatical policy said that I was allowed to
take a 3-month unpaid break and come back after.

Working on a smallish (~4000 LOC) open source project has been a nice thing to do for a relatively
short/focused amount of time. I don't think rbspy needs more full-time dedicated attention right now
(it works! time to step back, see what people think of it, and fix bugs / add features as they're
needed), so I'm happy to go back to a job & team that I like.

Another benefit of doing this was that now I have actual code that I've written out in the open on
GitHub! I don't really believe in "github is your resume" (lots of great programmers don't do any
open source work! that's fine!) but it does feel good to have.

### build a prototype to build confidence

Taking time off work to build a programming project felt a little risky.  What if my ideas didn't
work? I think the biggest thing that helped me be confident in my ability to do the project was -- I
had a prototype!! In May 2016
([blog post: "How to spy on a Ruby program"](https://jvns.ca/blog/2016/06/12/a-weird-system-call-process-vm-readv/)), I'd
written a small prototype of what eventually became rbspy.

That prototype wasn't really something people could **use** -- it was pretty fragile and, while a
few people had used it and contributed to it, it needed a lot of work. But it did _kind of_ work,
and so I felt pretty confident that I could make it into something more robust if I just spent time
on it.  (spoiler: I was right! it's way more robust now! people are able to use it!)

### I don't do programming projects after work

Some people program after work. I think this is cool, but I don't! I don't really feel like I have
the energy to do it. For whatever reason I _do_ have the energy to write hundreds of blog posts
about programming, but I guess that comes out of a different energy reserve for me :).

I've done exactly 3 side programming projects in the last 4 years, none of them particularly time
consuming ([turn off retweets](http://turn-off-retweets.glitch.me), [computers are fast](https://computers-are-fast.github.io/), the rbspy prototype).

It's been useful for me to accept that I don't really want to program after work or on the weekends.
But of course there _are_ projects I'm excited about building, so this sabbatical was a great
opportunity to do programming work that I wouldn't otherwise do.

### maybe take a sabbatical!

It looks like Segment might be doing the same fellowship program again this year. If you're
interested in getting email when they open applications, the [open fellowship homepage](https://open.segment.com/fellowship)
has a mailing list.

For me taking this sabbatical has been great -- it's really fun to have an focused goal that's
outside of my usual comfort zone. "Ship a cross-platform binary", "do a medium-sized systems
programming project that people actually use", "build a profiler", and "lead an open source project"
are all things I was interested in but had never done before, and the end product is something that
people are using and that I'm happy with!
