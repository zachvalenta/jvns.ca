---
layout: post
title: "Learning to like design documents"
date: 2016-06-03 21:01:44 +0200
comments: true
categories: 
---

Hi everyone! Today we're going to talk about software engineering and process!

A design document is where, before starting to implement a system, you write up a thing explaining what the system is going to do first. I think the idea is that, instead of discovering a crucial design flaw after 8 weeks of coding, you can discover the design flaw just by thinking about it in advance.

I used to get kind of grumpy when someone was like "hey julia can you write a design document for your system?" And then I'd be like "well, okay, this seems like a rational thing that might help me. Sure!" But the first couple of times I tried to write one I felt like.. it didn't help me? I liked the idea in principle, but I didn't know 

But last week I wrote a design doc and I thought it was pretty helpful. Here are some current thoughts.

### it's ok if nobody reads the whole thing

One of the first reasons to be grumpy about writing a design document is "UGH. NOBODY IS EVEN GOING TO READ THIS. TOO MANY WORDS. WHY?!". And I think it's actually kind of true? Getting a good review of a system design is hard! If it is a big system, the person reviewing your system has to put this whole hypothetical thing into their head, and think about every single thing that could go wrong, and think about the risks of all those things, and what already exists, and how it fits with those things, and how it will scale, and UGH.

So it's not like a simple code review where you're like "hey can you take a look after lunch?". I ended up trying to just think about it as a personal tool -- I came up with some questions I needed to answer before I started writing code, wrote down the options, and then picked one that seemed reasonable to me. 

I realized that instead of trying to get someone to read it, I could just talk to them and explain everything in the document to them and my thinking, and then they could suggest ideas for parts that could work better!

So then instead of it being like "Here is a LARGE DOCUMENT for you to read please review" it was more like "I have written extensive notes so that I can make sure to ask you all the most important questions I have and we can have a SUPER PRODUCTIVE MEETING". A+

### coding is easier if you think first

This is maybe sort of obvious! But -- sometimes I start coding, and then an hour or day in I'm like "oh no, I didn't think about this whole aspect of this project, hmm, what do I do?"

After writing this design doc, when I went to write the code I was like, oh, I made a lot of these decisions already. This is easy to write! Cool! And there were still unexpected difficulties, but I felt like it helped.

### you can't predict everything and it's okay

Another thing that made me grumpy about design docs was that -- this idea that you can predict all the flaws in advance and design the perfect system is actually a total lie. I still ran into things that I'd forgotten to consider! 

But I realized that writing a design doc isn't about predicting **everything** that could ever possibly go wrong. I mean, maybe there are magical wizards who can predict everything. But for me it really helped to let go of this idea that we're going to be able to design the perfect system just because now I have a document with "Design" written at the top and some people to help me review it.

### watch your decisions change

I asked a bunch of wonderful people about design docs a couple months ago and someone -- I forget who right now -- said "the reason you write them is **because** your requirements & ideas of how things should work will change over time, and it's useful to track that". And this is totally true! Often I'll make a design decision, forget about it, and then 8 months later be like "ugh who made that decision and why???". And then it was me, and I need to dig up an IM conversation from 8 months ago to try to figure it out.

And things change in software all the time. Maybe:

* 2 years later, the software you decided to not use is a lot more mature
* the thing you thought was awesome, after doing some more research, had some really serious flaws that might now be a dealbreaker
* you suddenly are handling 20x more data
* you did user research and the users said a lot of really unexpected things that make you want to reprioritize

So if nothing else, I think design documents are cool as personal archaelogical artifacts so that people from the future can understand you and why you decided what you did.