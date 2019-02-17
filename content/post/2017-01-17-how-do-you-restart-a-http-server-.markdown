---
title: "How do you restart a HTTP server?"
juliasections: ['Computer networking']
date: 2017-01-17T00:18:29Z
draft: true
url: /blog/2017/01/17/how-do-you-restart-a-http-server/
categories: []
---

Hello! The other day at work I needed to shut down a HTTP server gracefully. I thought this was an easy thing ("how hard could that be?") and I realized that restarting a HTTP server is harder than I thought.

### easy mode: PHP

First, let's talk about PHP and CGI. When I made my first websites, they were
Perl CGI scripts. I never worried about "restarting" them "safely".

With PHP and CGI scripts, every time you handle a HTTP request, you **start a
new process**.

So it looks like this:

1. A HTTP request comes into your webserver (like Apache)
1. Apache says "okay, let's start PHP!"
1. Apache starts up a new process & gives it the request parameters

When you update your PHP application, you don't need to do anything special!
Any processes Apache started before will eventually exit, and any new
processes will use your new code. No problem.

### harder mode: running a server

Okay, so now let's suppose that you've decided to run your own HTTP server in
Python or Go or Ruby or something.

You want to have the same cool thing as with PHP -- when you run new code, you
want requests to be handled with the new code, and for there to be no
downtime. Okay!

Starting a new process for every HTTP request is really expensive, so we don't
want to do that. Instead, we normally run a bunch of "worker processes"
