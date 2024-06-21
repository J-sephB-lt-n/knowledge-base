---
created:
  - 2024-06-21T14:19
modified: 2024-06-21 15:14
tags:
  - inference
  - machine-learning
  - graph
  - small-data
  - semi-supervised-learning
  - scikit-learn
type:
  - algorithm
status: 
---
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
## Related 
* [[Machine Learning on Small Datasets]]