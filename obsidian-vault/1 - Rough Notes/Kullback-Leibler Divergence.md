---
created:
  - 2024-09-22T20:23
modified: 2024-09-22 20:31
tags:
  - kl-divergence
  - kullback-leibler
  - shannon
  - entropy
  - information
  - information-theory
type:
  - note
status:
  - in-progress
---
[Kullback-Leibler Divergence](https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence) has the following alternative names:
- KL Divergence
- Relative Entropy
- I-divergence

_KL Divergence_ is a metric quantifying how different 2 probability distributions are from one another. For reference distribution $P$ and comparison distribution $Q$, _KL Divergence_ is defined:

$$\begin{array}{lcl} 
D_{KL}\Big(P\Bigl|\Bigl|Q\Big) &=& \displaystyle\sum_{x \in X} P(x) \hspace{2mm} log \bigg(\frac{P(x)}{Q(x)}\bigg) \\
\end{array}$$

## References
* Links to references (source material) go here
## Related
* [[Shannon Entropy]]
* [[Mutual Information]]
* [[Mutual Information as a measure of feature dependence]]