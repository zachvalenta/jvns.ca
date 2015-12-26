---
layout: post
title: "Winning the bias-variance tradeoff"
date: 2015-12-26 08:53:20 -0500
comments: true
categories: 
---

Machine learning is a strange mix of math and weird heuristics. When I started studying machine learning, I was SO FRUSTRATED. Everything was "well it works in practice" and so little of it was math. I drew my feelings in a picture. 

The bias-variance decomposition is a small piece of math that actually explains why some things in machine learning work!!!!

<img src="https://pbs.twimg.com/media/CWPOF1-UYAEdpQ2.jpg">

The bias-variance decomposition gives you a framework for how to think about model error and overfitting, and it explains why techniques like model ensembles and ridge regression work (the tradeoff is a tradeoff you can WIN). I finally learned about it last week and it felt life-changing. I think it's going to help me build better models, and it can help you too!

I've annotated each section by whether it's math or whether it a "works in practice" heuristic (aka bullshit, but useful bullshit).

### Bias and variance (math)

I first took a machine learning class in 2011. I understood what bias and variance were last week, after reading [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/), which is an excellent book along with [its more advanced companion](http://statweb.stanford.edu/~tibs/ElemStatLearn/).

**The setup**: Suppose we have all of the possible training data for a model, and a model training method (like linear regression). We're going to look at what happens for a specific training point $$x_0$$ if we train models using different training sets.

Now take a list of all training sets, and for each training set train a model $$M$$. Then we can look at the distribution of predictions $$M(x_0)$$ for each model. (see [Statistical learning theory](https://en.wikipedia.org/wiki/Statistical_learning_theory) if you're super interested in the theoretical foundations for machine learning)

The best case scenario: $$M(x_0)$$ is always the same no matter what training set we picked, and always correct. The worst case scenario: it's always changing and always totally wrong. In reality: you have some probability distribution of predicted values. (put graph here)

**Variance** is the variance of this probability distribution of predictions across all models (how different are the values from each other?)

This is incredibly important: if every model you train makes totally different predictions, you're in big trouble! Those predictions are definitely not correct.

**On variance & overfitting:** I keep hearing that high variance and overfitting are the same thing, and it makes sense to me. Overfitting is an idea, not a well-defined quantity, and if your modelling method gives you completely different results for every set of training data -- I'd call that overfit. So I'm okay defining overfitting and variance to be the same thing.

**Measuring variance**: Variance is cool because you have some prayer of approximating it for your actual models! You could imagine training your model on different training subsets, and seeing how different the predictions are.

**Bias** is the difference between the mean of this probability distribution and the actual correct value. Do the models on average predict the right thing for that point?

Worst case: If you have a relationship that is totally nonlinear, and you try to use a linear model, your bias is definitely going to be high. It's impossible to fit a correct model!

Best case: If you have a true linear relationship, and you fit a linear model with least squares regression, your bias for every point is **zero**. 0! unbiased! On average you're always going to be exactly correct. But that doesn't mean least squares regression is the best method! We'll explain why in the next section =D =D

**On complexity & bias**: People say that more complex models (with more parameters) have lower bias. As far as I can tell this is something that's likely to be true but does not have any math behind it. If there is math that says this is true I would [love to know](https://twitter.com/b0rk).

**Measuring bias**: I have no idea how to measure bias in the real world. My impression is people mostly guess at whether a model's bias is high or low.

### The bias-variance decomposition (math)

This is a theorem that you can find in [An Introduction to Statistical Learning](http://www-bcf.usc.edu/~gareth/ISL/). This is math so it will never let us down ❤.  It basically says that the error at a point is the 

```
Err(x) = Bias^2 + Variance + Irreducible Error
```

This is **awesome**. It means that every time we have error, it's either because of bias or because of variance.

**Heuristic warning**: From now on, I'm going to talk about the bias and variance of a model. If you've reading carefully, you'll notice that this doesn't quite make sense: we've only defined bias and variance for a modelling method and a specific input to that model (we took the variance of $$M(x_0)$$ over all models $$M$$). All the arguments we're going to make from now on are heuristic and not math, so we're going to start being sloppy with the math.

### The bias-variance tradeoff (heuristic)

Now we get to the cool part: the bias-variance tradeoff! As with many cool things in machine learning, the theoretical foundation here is a little shaky.

There's no math reason I know of you have to have a tradeoff between bias and variance (if you know one, [tell me!](https//twitter.com/b0rk)). In an ideal world, you could just train a model with low variance and low bias and win at life.

In the real world, however, we do not have magical model training methods :(. And often what people observe in practice is that as you increase the complexity of a kind of model (by training deeper decision trees, for instance), the bias decreases and the variance increases. This is the "bias-variance tradeoff"!

But just knowing that isn't useful. So what?

From now on, I'm going to talk about the bias and variance of a model. If you're reading carefully

### Winning the bias-variance tradeoff: Ensembles!

The whole reason we're talking about this is so we can build better models and win at life. Machine learning people frequently use ensembles: take 10 or 100 models and average their results together to get a better model. For the longest time I had no idea why it worked! Here's why.

Ensembles are based on math! If I have $$n$$ independent samples from a probability distribution with variance $$\sigma$$ and mean $$\mu$$, and I average them, then the new mean is the same ($$\mu$$), but the new variance will be reduced! ($$\frac{\sigma}{n}$$).

Now, suppose you have a way to generate a model which has low bias and high variance. The canonical example of this is supposedly a deep decision tree, though I'm not aware of any real evidence that decision trees have low bias.

Then if you can "average" 100 models generated in the same way, then your final model should have the same bias, but lower variance! Because of the bias-variance decomposition, this means that it's BETTER. Yay! The amount of variance reduction you get depends on the correlation between the 100 models.

This is why random forests work! Random forests take a bunch of decision trees (low bias, high variance), average them (lower variance!). And they use an extra trick (select a random subset of features when splitting) to reduce the correlation between the trees (extra lower variance!!!).

Understanding why ensembles work is awesome -- it means that if an ensemble method isn't helping you, you can understand why! It's probably because the correlation between the models in your ensemble is too high.


### Winning the bias-variance tradeoff: Regularization!

And there's a second way to win! I honestly don't totally understand [regularization](https://en.wikipedia.org/wiki/Regularization_(mathematics)) yet, so I'm not going to try to explain the math (try [Elements of Statistical Learning](http://statweb.stanford.edu/~tibs/ElemStatLearn/) instead).

But I can talk about the idea for a minute! First, the [James–Stein estimator](https://en.wikipedia.org/wiki/James%E2%80%93Stein_estimator). Suppose you're trying to estimate the mean of a bunch of random vectors. The normal (unbiased!) way to estimate the true mean is to, well, take the mean! Awesome. You might expect that you can't do better. BUT YOU CAN. The James-Stein estimator is a way to estimate the mean that gives you lower error. It's a biased estimator (so on average it won't give you a correct result), but its error is lower. This is amazing.

Model regularization is has the same effect -- basically you solve a different optimization where you constrain the parameters you're allowed to use. You end up increasing your bias and lowering the variance. And  then you can end up winning and ending up with a lower overall error, if you've lowered the variance by more than you increased the bias!

I also don't know how to debug regularization (if you try regularization and it doesn't making your model better, how can you tell why not?!)

### yay

I still find it kind of frustrating how heuristic most of these arguments are. Machine learning is an empirical game! But knowing a little more of the math makes me feel a little more comfortable. Not knowing how machine learning methods work means I can't debug them, and that means I can't be amazing. which obviously isn't acceptable :D

If you know more math that helps you debug your machine learning models, please tell me!

{% include katex_render.html %} 
