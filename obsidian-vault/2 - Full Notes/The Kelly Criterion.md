---
created:
  - " 2024-06-20 15:35"
tags:
  - "#kelly_criterion"
  - "#kelly"
  - "#investing"
  - "#probability"
  - "#statistics"
  - "#gambling"
status: completed
modified: 2024-06-20 15:45
---
The *Kelly Criterion* or *Kelly Strategy* is a result from probability theory. In a specific repeated game (which resembles some gambling games and investment scenarios), it is the strategy achieving maximum gain/reward in the long run.

The formulation is as follows:

In a single game:

- The player invests (risks) $100r\%$ of their total assets/portfolio/wealth $A$.

- With probability $w$, they earn a return of $100g\%$ on their investment/risk. i.e. $A_{t+1}=A_t(1+rg)$

- With probability $1-w$, they lose $100b\%$ of their investment/risk. i.e. $A_{t+1}=A_t(1-rb)$

After playing $n$ consecutive games, the expected value of their total assets/portfolio/wealth is:

$$P_n \quad=\quad A_0(1+rg)^{wn}(1-rb)^{(1-w)n}$$

The value of $r$ maximizing $P_n$ can be found by solving the equation

$$\frac{d}{d r}\frac{log(P_n)}{n} \quad=\quad 0$$

The solution is:

$$arg\space max_r\space P_n \quad=\quad \displaystyle\frac{w}{b} - \frac{1-w}{g}$$
## References

* [[Kelly Criterion (wikipedia page)]]