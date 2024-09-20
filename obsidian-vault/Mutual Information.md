---
created:
  - 2024-09-19T15:57
modified: 2024-09-20 10:27
tags:
  - shannon
  - mutual-information
  - entropy
  - kl-divergence
type:
  - note
status:
  - in-progress
---
_Mutual Information_ is a measure of the dependency between 2 random variables $X$, $Y$.

It is defined as the distance between the joint distribution $P_{X,Y}(x,y)$ and the outer product distribution $P_X \otimes P_Y$, where the distance between the distributions is measured using [Kullback-Leibler Divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence). 

For the outer product distribution $P_{X\otimes Y}$, the probability of a point $(x,y)$ is the product of the univariate probabilities $P_{X\otimes Y}(x,y)=P_X(x) P_Y(y)$.   

If $X$ and $Y$ are independent, then $P_{X,Y}$ is the same as $P_{X\otimes Y}$.

_Mutual Information_ is defined:

$$\begin{array}{lcl}
I(X;Y) &=& D_{KL}\Big(P_{X,Y}\Bigl|\Bigl|P_X\otimes P_Y\Big) \\
&=& \displaystyle\sum_{y\in Y} \sum_{x\in X} P_{X,Y}(x,y) log_b \Bigg(\frac{P_{X,Y}(x,y)}{P_X(x)P_Y(y)}\Bigg) \\
&=& H(X) + H(Y) - H(X,Y) \quad \text{(relationship to entropy)} \\
\end{array}$$
## References
* https://en.wikipedia.org/wiki/Mutual_information
## Related
* [[Shannon Entropy]]