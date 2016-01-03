---
layout: post
title: "Java isn't slow"
date: 2016-01-03 06:27:07 -0500
comments: true
categories: performance
---

This is probably obvious to many of you, but I wanted to write it down just in case.

I used to write Java at work, and my Java programs were really slow. I thought
(and people sometimes told me) that this was because Java is a slow programming
language.

This just isn't true. This article describes the architecture of the [LMAX Disruptor](http://martinfowler.com/articles/lmax.html), a messaging library that they use to process 6 million events per second on a single machine. That article is also SUPER FASCINATING and really worth reading. Java is fast like C is fast (really fast). People write databases ([Cassandra](http://cassandra.apache.org/)) in Java!

So if your Java code is doing something easier than processing 6 million events a second, and it's slow, you can likely make it faster if you want to!

### How to make your Java (or Scala, or Clojure) code fast

Did you know the JVM ships with a free profiler that can tell you which part of your code is the slowest? It's called [VisualVM](https://visualvm.java.net). It’s very easy to use and it's an AWESOME first step to take. Here's a screenshot of VisualVM profiling VisualVM. It's spending most of its time on `org.netbeans.swing.tabcontrol.TabbedContainer.paint`. So it's mostly working on drawing the screen to show me the results of profiling itself!

<a href="/images/visualvm.png"><img src="/images/visualvm-small.png"></a>``

([YourKit](https://www.yourkit.com/) is better, but VisualVM is free)

I had some [slow JVM code](http://jvns.ca/blog/2015/09/10/a-millisecond-isnt-fast-and-how-we-fixed-it/) at work a while ago. We made it fast. I used VisualVM! So can you :)