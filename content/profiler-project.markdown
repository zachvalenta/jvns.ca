---
title: "Ruby profiler project"
staticpage: true
categories: []
---

From January 1 2018 -> April 1 2018 I'm working on a project to write a new Ruby CPU profiler! It's a **sampling
profiler**, and the goal of this project is to make it dead simple to figure out where **any**
running Ruby process is spending its time.

The idea is that there are 2 ways to run it:

1. Find the PID of an already-running program and profile it (`run-profiler -p $PID`)
2. Start a new program and profile it (`run-profiler ruby my-program.rb`)

The hard part of this project is that this profiler is a **separate process** so it doesn't have
much inside information about what the Ruby profiler is doing. So "how do you figure out what
$ARBITRARY_RUBY_PROCESS is actually doing?" is my main focus.

The code is at https://github.com/jvns/ruby-stacktrace/ right now. I've been
blogging about my progress on the project: you can see all the posts under the [ruby-profiler category](https://jvns.ca/categories/ruby-profiler/).

