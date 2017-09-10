---
title: "Data structure: the treap!"
date: 2017-09-09T21:37:15Z
url: /blog/2017/09/09/data-structure--the-treap-/
categories: []
---

Here's a quick sketch I did yesterday about a randomized data structure: the
[treap](https://en.wikipedia.org/wiki/Treap).  It's basically a really cool way to implement a
balanced binary search tree. Kamal told me about it!

The main reason I know for sure this is useful is in case someone asks you to implement a balanced
binary search tree in an interview. More seriously though -- if you want to implement an ordered map
(like C++'s [std::map](http://en.cppreference.com/w/cpp/container/map)), then you probably want a
balanced BST!

C++'s std::map is usually a red-black tree, but a treap performs just as well (in expected value)
and the algorithms for insert/delete are way simpler.

<div align="center">
<img src="https://jvns.ca/images/treap_1.png">
<img src="https://jvns.ca/images/treap_2.png">
<img src="https://jvns.ca/images/treap_3.png">
</div>
