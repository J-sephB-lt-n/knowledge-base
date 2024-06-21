---
created:
  - 2024-06-21T14:19
modified: 2024-06-21 23:03
tags:
  - inference
  - machine-learning
  - graph
  - small-data
  - scikit-learn
  - transductive-learning
  - semi-supervised-learning
type:
  - algorithm
status: 
---
This algorithm was first proposed by Zhu & Ghahramani (2002), although more modern variants exist. 
At a high level, the algorithm works as follows:
1. TO
2. DO

```shell
$ python -m venv venv && source venv/bin/activate && pip install scikit-learn matplotlib
```

```python
import matplotlib.pyplot as plt 
import numpy as np 

data = np.array(
	[
		[5,15]
	]
) 
plt.scatter(data[:, 0], data[:, 1], color='blue', marker='o')
plt.show()
```

## References
* https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html
* "Boosting vs. semi-supervised learning" (Vincent Warmerdam) https://www.youtube.com/watch?v=2eU_8ExBzDw
* "Learning from Labeled and Unlabeled Data with Label Propagation" (Xiaojin Zhu, Zoubin Ghahramani 2002). https://pages.cs.wisc.edu/~jerryzhu/pub/CMU-CALD-02-107.pdf
## Related 
* [[Machine Learning on Small Datasets]]
* [[Radial Basis Function]]
* [[Scikit-Learn]]