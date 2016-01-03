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

This just isn't true. This page describes the architecture of the [LMAX Disruptor](http://martinfowler.com/articles/lmax.html#footnote-free-lunch), a messaging library that they use to process 6 million events per second on a single machine. That article is also SUPER FASCINATING and really worth reading. Java is fast like C is fast (really fast). People write databases ([Cassandra](http://cassandra.apache.org/)) in Java!

So if your Java code is doing something easier than processing 6 million events a second, and it's slow, you can probably make it faster if you want to!

### How to make your Java code fast

Did you know the JVM ships with a profiler that can tell you which part of your code is the slowest? It's called [VisualVM](https://visualvm.java.net) and it's AWESOME. Here's VisualVM profiling VisualVM. It's spending most of its time on `org.netbeans.swing.tabcontrol.TabbedContainer.paint`. So it's mostly working on drawing the screen to show me the results of profiling itself!

([YourKit](https://www.yourkit.com/) is better, but VisualVM is free)

<a href="/images/visualvm.png"><img src="/images/visualvm-small.png"></a>