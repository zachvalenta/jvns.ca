---
title: "Talk: How rbspy works"
date: 2018-04-16T13:58:38Z
url: /blog/2018/04/16/rbspy-talk/
categories: []
---


<style>

.container {
	display: flex;
    margin-bottom: 5px;
}
.slide {
	width: 50%;
}
.content {
	width: 50%;
	align-items: center;
	padding: 20px;
}

@media (max-width: 480px) { /*breakpoint*/
    .container {
        display: block;
    }
    .slide {
    	width: 100%;
    }
    .content {
    	width: 100%;
}

</style>

Last month I gave a talk at Localhost, the [Recurse Center](https://recurse.com)'s monthly talk
series. My favourite thing about Localhost's talk format is that speakers
give relatively in depth talks about technical topics, and then people ask **lots** of questions at
the end.

This talk is about the core of rbspy -- how do we read memory out of the Ruby interpreter to figure
out what function a Ruby process is running? How do we do that in a way that works across multiple
Ruby versions? Do we need to stop the Ruby process to figure out what function is running?

The talk is 30 minutes and it's followed by about 30 minutes of questions. The audio is a bit
sketchy in places. Here's the video:

<iframe width="560" height="315" src="https://www.youtube.com/embed/o6wWSPxYueU" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
