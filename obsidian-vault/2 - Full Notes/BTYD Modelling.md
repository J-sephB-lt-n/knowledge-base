---
created:
  - 2024-11-06T09:42
modified: 2024-11-06 11:55
tags:
  - btyd
  - cltv
  - lifetime-value
  - customer-lifetime-value
  - churn
  - custom
  - statistics
  - model
  - bayesian
  - bayes
  - pymc
  - gamma
  - rfm
  - clv
type:
  - note
status:
  - in-progress
---
_Buy 'Til You Die_ (BTYD) is a family of highly interpretable probabilistic models used to estimate/forecast [Customer Lifetime Value (CLV,CLTV)](Customer%20Lifetime%20Value%20(CLV,CLTV).md) from basic RFM metrics.
Wikipedia describes them as ["a class of statistical models ... designed to capture the behavioral characteristics of non-contractual customers"](https://en.wikipedia.org/wiki/Buy_Till_you_Die).

BTYD models typical assumptions/workings are as follows:
- Customers continue to buy (in a stochastic but predictable way) until a certain point, at which point they cease to buy (i.e. churn or, from the perspective of the model, "die").
- Each of a customer's... 
	- frequency of purchasing
	- purchase amounts
	- probability of being churned/dead 
- ...are assumed drawn from probabilistic univariate distributions estimated uniquely for each customer.
## References
* [lifetimes (python package)](https://github.com/CamDavidsonPilon/lifetimes)
* [PyMC-Marketing (python package)](https://github.com/pymc-labs/pymc-marketing?tab=readme-ov-file)
* [The Gamma-Gamma Model of Monetary Value](http://www.brucehardie.com/notes/025/gamma_gamma.pdf)
## Related
* [Customer Lifetime Value (CLV,CLTV)](Customer%20Lifetime%20Value%20(CLV,CLTV).md)