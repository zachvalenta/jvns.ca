---
title: "netdev conference, day 3"
date: 2017-04-08T14:39:11Z
url: /blog/2017/04/08/netdev-conference-day-3/
categories: ["netdev"]
---

Okay, it's the last day of netdev! Today there was an exciting surprise! This
morning on the subway on the way there I got a mysterious text "julia, are you
coming to netdev today?"

When I got there (late), I discovered that I'd won a book!! So now I have this
cool [Linux Kernel Networking book](https://www.amazon.ca/Linux-Kernel-Networking-Implementation-Theory/dp/143026196X).
It's from 2014 which is pretty recent! I'm looking forward to looking at it.

themes from today:

* netfilter and nftables (which is a replacement for iptables)
* mesh networking (very low-power devices which want to network with each
  other)
* networking daemons

I think my main practical takeaway from today was "oh man, maybe I don't ever
have to learn iptables, I should maybe learn nftables instead? :)". Not sure
yet though!

### netfilter workshop

by Pablo Neira Ayuso

As usual a 'workshop' is not a tutorial, it's a discussion of new recent
advances in the tool. I think this workshop was actually mostly about nftables
(which is a new system inside netfilter).

**netfilter**

If you've ever used iptables to filter traffic, you've used the netfilter
system! netfilter includes a bunch of different 'tables': iptables, ipv6tables,
arptables, and ebtables.  

I think netfilter is also in charge of NAT, which is why it does connection
tracking ('conntrack') so it can know which connection every packet belongs to.

**nftables**

nftables is a new packet classification framework that replaces
the existing `{ip,ip6,arp,eb}_tables` infrastructure. The idea is that it's
more unified instead of being 4 different things! That makes sense.

The nftables wiki has a bunch of information. There's also
information in [the man page for nft](http://manpages.ubuntu.com/manpages/xenial/man8/nft.8.html).

Here are a few bullet points about what nftables is from the [nftables wiki](https://wiki.nftables.org/wiki-nftables/index.php/Main_Page).

* It is available in Linux kernels >= 3.13.
* It comes with a new command line utility nft whose syntax is different to iptables.
* It also comes with a compatibility layer that allows you to run iptables commands over the new nftables kernel framework.
* It provides generic set infrastructure that allows you to construct maps and concatenation. You can use this new feature to arrange your ruleset in multidimensional tree which drastically reduces the number of rules that need to be inspected until you find the final action on the packet.

There's a web tool you can use to [translate iptables rules to nftables rules](https://2nft.alemayhu.com/).

He also said that the beginning that in some benchmarks, nftables is almost 2x
as fast as iptables.

**new nftables features**

Here are some new features from the workshop

* new extension: **fib** ("forward internet base"). some things it lets you do
  * drop if reverse lookup fails 
  * drop if there's no destination route
  * drop packets to an address not configured on this interface
  * "works well with [Quagga](http://www.nongnu.org/quagga/)" (which is a BGP
    thing?)
* new extension: **rt** (something about routing?)
  * "drop any traffic to 192.168.0.1/24 that isn't routed via 192.168.0.1"
* new extension: **notrack** (disable connection traffic)
  * example `nft add rule prerouting dport 80 add notrack` or something (though
    i didn't get it exactly)
* new extension: **quota**  (supports byte quotas)
  * example `ip saddr timeout 60s quota over 50 mbytes` I think sets a quota of
    50 MB / minute per IP src address 
* updated extension: **payload**
  * this lets you update checksums (i didn't understand this)

I got kind of lost in the rest of the workshop. I did learn that there's a
nftables virtual machine with 25 instructions.

Someone asked in the question period whether they'd consider putting eBPF into
nftables -- i think the idea is that all these systems (tc, nftables, etc) are
a lot for users to learn, and if you could define new stuff in eBPF it would be
easier to add features and understand the landscape.

### morning keynote

by Jesse Brandenberg

what I learned from this keynote 

* there are 2.5 million lines of network device driver code in the Linux
  kernel, and it's increasing fast
* Linux is moving into a lot of different places
* people are gonna be using a lot more bandwidth (1000x more in the next 10
  years?)

on Intel's direction:

* intel is moving to switchdev (which is a way to program ASICs on switches
  with Linux, I think? and ASICs are networking hardware?)
* they want to add more hardware offloading capabilities to tc
* "make Linux the best choice for networking"

He said that it's important to offload crypto operations to hardware. Someone
asked "we've been trying to do that for a while, but Intel keeps releasing new
specialized CPU instructions that make it more efficient to just do crypto in
the CPU, is that going to change?"

It also doesn't really seem clear to me that you can offload crypto stuff to
hardware -- like he said you can do IPSec in hardware (I don't really know what
that is, something to do with VPNs or smoething?), but many people are using
TLS and I don't know how you'd do TLS termination in hardware exactly,
that seems complicated. He said that it's not obvious how to do TLS in
hardware.

### new mailing list: xdp-newbies

David Miller came up to me to tell me he made a new kernel mailing list for
people who are new to XDP! Cool! There's a [link to sign up here](http://vger.kernel.org/vger-lists.html).

weird aside: I learned when subscribing to this list that you cannot just sign up with Gmail
(or you have to do something special) -- I tried to sign up and it replied to
my confirmation email like

```
>>>> Content-Type: text/plain; charset=UTF-8
**** Command 'content-type:' not recognized.
```

so I guess I sent the wrong kind of email. Anyway I will figure it out. I
remember learning from the Outreachy docs that kernel mailing lists are kind of
particular about how you send email and I'm sure it's not that complicated,
lots of people have subscribed to the mailing lists before :)

### IoT workshop!

Okay! There was an IoT workshop after lunch. This seemed to be mostly about
"mesh networking" which is when a bunch of low-powered devices create a peer to
peer network.

**6lowpan**

I had no idea what "6LoWPAN" was so I looked it up! The [wikipedia article](https://en.wikipedia.org/wiki/6LoWPAN)
is pretty good. Basically it seems to be a protocol to send IPv6 messages over
very low powered networks.

"low powered network" seems to mean a very specific thing: there's this
standard [IEEE 802.15.4](https://en.wikipedia.org/wiki/IEEE_802.15.4)
which is like the wifi standards (`802.11`), in that they define which wireless
spectrum you use (902-928MHz in North America) and how you send data "frames
and MAC addresses" on that frequency

But the 802.15.4 standard doesn't actually define how to structure your packets
inside those frames, so I think that's what 6LoWPAN does.

The first talk in this workshop was about "MLE". what I learned:

* ZiGBee is a thing in the low powered networking world
* There is a protocol called MLE which is for
  * link establishment
  * link quality detection
  * network parameter distribution (what's that?)
  * I didn't totally understand though if anyone uses MLE or how it's related
    to zigbee
  * MLE uses a "frame counter" as a security feature to prevent replay attacks.
    This is the second time this week i hear about someone using a counter of
    some sort to prevent replay attacks so that's interesting.

**LLNs and Linux**

by [Michael Richardson](http://www.sandelman.ca/mcr/)

A LLN is a "low-power lossy network". Some of these networks do 256
kbits/second, some of them are as slow as 9600 baud. He said at the end of the
talk that there are some wide-area networks (where you send data maybe
kilometers) where you might only be able to send 100 **bytes per day**.

He has a project called unstrung with has a really pretty website:
http://unstrung.sandelman.ca/.

some things I learned: 

* a thing that exists in the world is "kinetically powered lightswitches" --
  they only get power when you flip them, and only enough to maybe send a
  packet before they die. He said he's never actually seen one yet even though
  he's trying.
* maybe you use some of these mesh networking things to power a gas/water
  meter?
* the wifi in this room isn't working well because there are too many access
  points which are transmitting at too high power, and they're interfering with
  each other
* so when you have low powered devices like this, you want to only use as much
  power as you need to -- you can do sort of a binary search to figure out how
  much power you should be using

### Increasing Reliability in Data Center Network Configuration

by Tom Distler & Arthur Davis, from NetApp

They're working on a daemon that makes networking changes. This is pretty relevant
to my interests because I am paying some attention to Kubernetes right now
which makes changes to networking configuration all the time

design goals:

* provide ACID guarantees around network configuration
changes (so if you're creating 20 network interfaces, you want to get all of
them or none of them). That's a very worthy goal!
* if you crash, you should be able to recover
* applications can ask the networking daemon to make changes

The data model reflects the structures that exist in the kernel (interfaces,
routing tables, etc). They don't try to add any extra abstractions over what
the kernel provides.

When a client wants to make some changes to reconfigure the network, they fetch
the database from the daemon, make changes, and tell it to apply those changes.
So I guess this is kinda like tools like Terraform in a way? (you tell it what
the state you want it to end up in is, and then it works to apply that state?)

They said they looked at other systems that did similar things but didn't say
what they were.

The tool they're building isn't open source yet but I guess we'll see what it
looks like when it is open source!

### closing remarks

They said 25% of the people were from Canada! Lots of people from Montreal :).
The next netdev will be in South Korea in November.

### that's all

those are all my conference notes! blogging this conference has been fun and I
think it helped me learn a lot more. A+ would blog again.
