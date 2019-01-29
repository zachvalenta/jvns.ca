---
title: "Confidence intervals for A/B tests"
date: 2018-12-31T08:29:27Z
draft: true
url: /blog/2018/12/31/confidence-intervals-for-a-b-tests/
categories: []
---

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({tex2jax: {inlineMath: [['$','$'], ['\\(','\\)']]}});
</script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>


Hello! I'm trying to think about nonparametric statistics, but along the way I figured it also makes
sense to understand a tiny bit of parametric statistics a little bit. To start: let's get concrete.
We're going to talk about a really specific problem: the A/B test.

Disclaimer: I have never actually done an A/B test in real life, this is just me trying to work
though some math that relates to A/B testing. 

### what even is the distribution of anything?

The reason I'm interested in nonparametric statistics is that I think that as programmers, a lot of
the data we deal with (for example performance/latency data) doesn't come from a distribution that's
in any obvious parametric family. Why should how fast my Python program runs be normal?

For example, here's a histogram of how long a small python program takes to run on my laptop (over
~3400 runs of the program).

<img src="/images/runtimes.png">

What even is that distribution? Why are there weird spikes at 95 and 105?

### some things have actual distributions

But the point I want to make in this blog post is that some things *do* have actual distributions,
and it makes sense to use that fact.

### what is an A/B test?

Let's say you run an online boots store, and you have an idea that you think will increase the
number of people that buy your boots. Maybe you think that if you give the 'buy' button a purple
glittery font more people will buy boots. Whatever.

One model of how people choose to buy boots is -- every person decides at random with probability
p (for example 10%) whether they want to by the boots or not.

This is obviously not *actually* how people decide how to buy boots, but, this is statistics! "All
models are wrong but some are useful". So this seems like a pretty natural model to use, and it's
really simple. (are there other statistical models that people use for ecommerce than this? I don't
know!)

### A/B 

### the bernouilli distribution

The fancy math term for "every person decides at random with probability p to decide if they want to
buy boots or not" is "the bernoulli distribution". It has one parameter (p) and its mean is p. 

So another way of phrasing the question "did the purple glittery font make more people buy boots" is
"did the probability p that a person will buy boots change?". Answering that question is what
statistics is all about!

### how to estimate p

How do we estimate this parameter p? That's really easy: we just count the number of people who
bought boots, and divide it by the total number of people who visit the webpage, to get a number
like 0.02 or something (2%!). And we can do that division for the A side of the A/B test and the B
side and get 2 different numbers: maybe 0.02 and 0.025. Cool.

<small>
(side note: obviously "easy" is an overstatement, this is the internet and often it is actually
EXTREMELY DIFFICULT to reliably count the number of unique people who visited your website. But
luckily this is a math blog post so we'll assume we have somehow figured that out)
</small>

### what's the confidence interval?

So we know that 2% of the not-glittery-button people bought boots, and 2.5% of the glittery-button
set bought books. Cool! But of course the first thing you learn about statistics is not to trust
numbers like this!!! You want some kind of **confidence interval** around these numbers, to know how
close they likely are to being accurate.

Now, let's say that there were 10,000 people in the no-glittery-button set and 10,000 people in
the glittery-button set. Let's calculate a confidence interval!

### 3 ways to calculate a confidence interval
