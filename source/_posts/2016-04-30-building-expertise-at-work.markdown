---
layout: post
title: "How does knowledge get locked up in people's heads?"
date: 2016-04-30 09:51:50 -0400
comments: true
categories: 
---

, or, "Building expertise a twork"

I mentioned yesterday that I joined a new team at work this week, so learning and expertise have been on my mind. For the first time in a while, I'm working on systems that I don't always understand very well, and where I often can't figure out what the system does on my own.

The main thing that has bothered me at work, for a long time, is -- there are a bajillion people who know amazing things, and often that knowledge gets stuck in their head and other people don't end up learning it. For years, sometimes! How can this be?!

To start: this is not about people intentionally withholding information. 

I'm going to try to walk through the hard problems

### Discovery: who knows the thing?

So, if you're going to learn awesome stuff from the people you work with, first you have to actually know that they know it. here's an handful of examples of stuff I know that other people know.

* erik knows a lot about jvm performance (as does ianoc, I think)
* to get information about scala I'd just go to the #scala slack channel because there are a ton of scala experts. scala information is easy to come by.
* nelhage writes the most about the linux kernel and evan knows a ton too
* cory just wrote [cool blog posts about java garbage collection](http://onemogin.com) so it turns how he knows about that.
* jessitron knows about [java concurrency models](https://www.youtube.com/watch?v=yhguOt863nw) and her and jorge wrote a great article about [implicits](http://engineering.monsanto.com/2015/05/14/implicits-intro/)
* alyssa has a PhD in statistics and can answer basically any stats question I have

I have a bajillion pairings of people <-> information like this in my head. But as I'm writing down these examples, I'm realizing how *not* obvious it is who knows what! For instance, suppose I was running into a problem with JVM garbage collection 4 weeks ago. I would definitely 100% not have thought to ask Cory, even though it turns out he knows a lot about that! I had no idea that cory know about the JVM.

Ray wrote Cloudflare's DNS server. He won't tell you this if you meet him so you have to go look at his LinkedIn or something and read

> Designed, developed and maintained CloudFlare’s current DNS server
> infrastructure, RRDNS, in Golang that serves authoritative DNS for over 1
> Million domains and proxies DNS traffic for partners at 250+ Billion
> requests/month. 

Whoa, that's amazing! That is very relevant knowledge if you work with him.

And if I had a question about Go, I'd probably look up who maintains Go services internally, and maybe I'd come up with Carl or Colin, but I also happen to know that Aditya knows quite a bit about Go and [gave a cool talk at Gophercon](https://www.youtube.com/watch?v=s4e-cFhT620). I don't know how I'd discover that without googling "$coworker golang" for every single one of my coworkers. And that wouldn't even do it because lots of people don't have an internet presence.

So, discovery. In general I know (or can easily find out) what projects people work on at work. That is no problem and I can  But. I'm constantly shocked by how often I find out that there's a topic I need to know about for work and someone I work with either

* has a ton of previous professional experience with the topic ("oh yeah i worked on networking for 6 years")
* maintains an important open source project in the field that I had no idea about
* has been learning about the topic in their spare time and now knows a lot about it

and **I had no idea**. I basically think this is a travesty. People occasionally run internal talks about topics they know about which is THE BEST. But honestly sometimes I wish every developer (to say nothing of my other great colleagues!!!) I work with came up with a resume or document or something saying HERE IS WHY THIS PERSON IS REALLY IMPRESSIVE AND AWESOME AND THESE ARE THE THINGS THEY ARE AN EXPERT ON.

Okay, so that's discovery. I don't know how to fix it but I think it should be fixed, because not knowing that you have internal experts on a topic is just silly.

### how do people become experts?

Here's the easiest way.

* person builds system from scratch
* person is the expert forever

This sucks. The person who built the system has to answer questions about it forever, which puts a lot of pressure on them, it makes it harder for 

I find this a little mysterious because there are internal systems that are important which have a Single True Expert but that I honestly don't feel are **so** complicated -- they're often a few thousand lines of code, and have some history and complexity, but I feel like somebody else could, with some .

Like everything in this blog post, I don't know the answer to this one. It's easy to be an expert on a system that you built from scratch.

I think there are maybe two reasons for that (and probably more!)

First, if you built it then you have a really strong sense for the **history** of the system. Systems don't come into being fully formed, and if you try to understand them that way it doesn't work. I've been 

Second, you end up with this sense of... entitlement, or something, to knowledge about the system. If someone asks me a question about a system I started, my basic assumption is "yeah, I can answer that, no problem!". And even if I haven't looked at it for 6 months or other people have done significant development work on it afterwars, I **still** expect to be able to just ask them questions about what they did and figure out the answer to arbitrary questions about the system.

But for systems that I *didn't* build, I don't always feel that sense of "uh yeah I can definitely work that out just give me a minute / an hour / 3 hours".

I kind of feel like telling someone that they can't understand a system or that it's "too hard" or like "yeah that's weird only $other_person" knows about that is like... a crime. We should all expect to be able to understand the software systems that we work with! right????

### to make someone an expert, ask them questions

One thing I've noticed is that sometimes you have Person A and Person B who know roughly the same things but somehow Person A ends up being more respected and becoming the Internal Expert Who Everyone Goes To just because they're better at communicating those things / advertising that they know it.

I think some people just like answering questions about a topic more, which is fine. But I think it's more than that. 

If everyone always asks Person A questions about the System, then that is itself an organizational investment in Person A's knowledge. They're constantly practicing answering questions and updating their knowledge and checking their understanding of the system.

This was a huge thing on my old team -- for a long time, a small subset of people were responsible for answering questions on behalf of the team. Then we brought a bunch more people into the rotation. And after that those people reported feeling like they understood the system way better! Because they had to actually answer questions and figure out the answers if they didn't know.

[Kiran](https://twitter.com/kiranb) often says that you can build people who are "caches" for information -- put them in charge of answering questions, they slowly start to accumulate knowledge and eventually become experts.

### "how did you find that out?"

This one is not a phenomenon and is instead a MAGICAL TACTIC. I forget who I learned it from but maybe Alyssa.

Sometimes I ask someone a question "hey why is the database having timeouts" and the answer is "oh sorry I fixed it". This is sometimes great and sometimes my LEAST FAVORITE ANSWER.

I often follow up with 

* how did you do that? 
* how did you know that?
* what command did you run?

This is a great way to extract information from experts -- often they don't realize what they know, but if you ask them what they did RIGHT AFTER THEY DID IT they can usually remember.

From the other side, when people ask me questions I also often try to include the source of my answer -- "the answer is $blah but I found it by doing X Y Z".