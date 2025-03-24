---
created:
  - 2024-09-17T21:14
modified: 2024-10-01 20:56
tags:
  - entropy
  - shannon
  - information-theory
  - information
  - mutual-information
  - probability
  - statistics
type:
  - note
status:
  - in-progress
---
The _information content_ (amount of 'surprise') of a random binary event $x$ can be represented as 
$$\begin{array}{lcl}
I(x) &:=& log_b \bigg(\displaystyle\frac{1}{p(x)}\bigg) \\
&=& -log_b \space p(x) \\
\end{array}$$(for chosen base $b$) 
where $p(x)$ is the probability of the event $x$ occurring. 

_Information_ (or _self-information_) [can be thought of as an alternative way of expressing probability, much like odds or log-odds, but which has particular mathematical advantages in the setting of information theory.](https://en.wikipedia.org/wiki/Information_content) 

_Information_ is sometimes described as the "amount of surprise" of a random event i.e. a more rare event occurring results in greater "surprise."

Here is a graph of the relationship between _information_ and event _probability_:
```r
p <- seq(0.001, 1, by = 0.001)
info <- -log(p)
plot(
  p, 
  info, 
  type = "l", 
  col = "blue", 
  lwd = 2,
  xlab = "Probability (p)", 
  ylab = "Information (-log p)",
  main = "Relationship between Probability and Information",
)
grid()
```

![Information vs Probability](../7%20-%20assets/Shannon%20Entropy/probability_vs_information.png)

_Information_ (or _self-information_) is [the unique function of probability that meets these three axioms (up to a multiplicative scaling factor):](https://en.wikipedia.org/wiki/Information_content#Definition)
1. An event with probability 1 (100% certainty) yields no _information_
2. Decreasing event probability leads to more _information_
3. The joint _information_ in observing 2 independent random events together is equal to the sum of their individual _informations_
   i.e. $I_{X,Y}(x,y)=-log_b\space p_{X,Y}(x,y)=I_X(x)+I_Y(y)$ for independent random variables $X$ and $Y$ 

The _entropy_ of a random variable $X$ is the expected ("average") _information_ content in measuring it. 
Intuitively, _entropy_ measures the "uncertainty" or "unpredictability" of a distribution.
The _entropy_ of a discrete random variable $X$ is defined: 

$$\begin{array}{lcl}
H(X) &=& E\Big[I_X(x)\Big]\\
&=&-\displaystyle\sum_{x \in X} p(x) \space log_b \space p(x)\\
\end{array}$$
If the log is base 2, then the entropy is expressed in _bits_. If the natural log (base _e_) then the entropy is expressed in _nats_.

_Information_ and _entropy_ have many practical applications. Here is a specific example:
- ["The limit of compression will always be the _entropy_ of the message source"](https://youtu.be/TxkA5UX4kis?t=203)
- This means that when encoding a message in order to send it through a communication channel (e.g. over a network), _entropy_ defines a lower achievable limit for how efficient the encoding can be.

It seems counterintuitive that higher _entropy_ means both "more unpredictability" and "more expected information," but what this means is that under a high _entropy_ distribution, predicting a specific outcome is more difficult and  


Some observations about the behaviour of _entropy_:
- Increasing the number of possible outcomes increases the _entropy_ (uncertainty) 
  e.g. the roll of a 6-sided die has more entropy than a coin flip.
- Outcome probabilities closer to uniform increase the _entropy_ (uncertainty) 
  e.g. a fair coin has more entropy than a biased coin
## References
* https://machinelearningmastery.com/what-is-information-entropy/
## Related
* [[Mutual Information as a measure of feature dependence]]