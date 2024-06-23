---
created:
  - 2024-06-21T14:19
modified: 2024-06-23 20:50
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
This is a [[Classification]] algorithm. It is well-suited for problems in which there is a lot of feature data ($\mathbf{x}$), but very few labelled data points ($y$). 
The algorithm diffuses ("propagates") the known labels from the labelled samples into the population of unlabelled samples using the structure present in the feature data.

There a different variants of this algorithm, but the general concept is: 
1. The samples in the data are represented as nodes in a graph. 
2. Either the graph is fully connected (every node connects to every other node) or each node connects to it's *k* nearest neighbours (nearest in the feature space $\mathbf{X}$, by some chosen distance measure e.g. [[Euclidean Distance]]).
3. The edges joining the nodes are undirected.
4. The weight of the edge joining the 2 nodes is a function of the distance between the 2 nodes (samples) in the feature space ($\mathbf{X}$). i.e. edges between samples which are less alike have less weight.
5. Each node has a distribution over the classification labels. This distribution for the known labels propagates through the network by traversing the edges. Where distributions meet, they are mixed together (e.g. as a weighted average). *Weak* (low weight) edges dilute the distribution information, making it more likely to be dominated by distribution information that has travelled from higher-weight edges.

Here is an example using [[Scikit-Learn]] in [[Python]]:

Environment setup:
```shell
$ python -m venv venv && source venv/bin/activate && pip install scikit-learn matplotlib
```

Create the data:
```python
import matplotlib.pyplot as plt
import numpy as np

LABEL_MAP = {-1: "label_unknown", 0: "class-1", 1: "class-2", 2: "class-3"}
LABEL_PLOT_COLOUR_MAP = {-1: "grey", 0: "red", 1: "blue", 2: "green"}
data = np.array(
    # each entry has format {x, y, label}
    [
        # J #
        [3, 20, -1],
        [6, 20, 0],
        [8, 20, -1],
        [15, 20, -1],
        [12, 20, -1],
        [9, 15, -1],
        [9, 10, -1],
        [9, 2, -1],
        [6, -2, -1],
        [4, -2, 0],
        [2, 1, -1],
        [0, 5, -1],
        # O #
        [18, 10, -1],
        [18, 5, -1],
        [20, 15, -1],
        [22, 18, 1],
        [24, 18, -1],
        [20, 0, -1],
        [22, -2, -1],
        [24, -2, 1],
        [26, 0, -1],
        [28, 5, -1],
        [28, 10, -1],
        [26, 15, -1],
        # e #
        [40, 4, -1],
        [43, 2, -1],
        [46, 0, -1],
        [48, 0, -1],
        [52, 0, -1],
        [40, 6, -1],
        [44, 6, -1],
        [46, 6, -1],
        [50, 6, -1],
        [55, 6, 0],
        [53, 8, -1],
        [48, 10, -1],
        [42, 8, -1],
        # underline #
        [2, -8, -1],
        [7, -8, -1],
        [12, -8, 2],
        [18, -8, -1],
        [23, -8, -1],
        [28, -8, 2],
        [32, -8, -1],
        [37, -8, -1],
        [42, -8, -1],
        [45, -8, -1],
        [51, -8, -1],
    ]
)

fig, ax = plt.subplots(figsize=(10, 5))

def legend_without_duplicate_labels(ax):
    # https://stackoverflow.com/questions/19385639/duplicate-items-in-legend-in-matplotlib
    handles, labels = ax.get_legend_handles_labels()
    unique = [
        (h, l) for i, (h, l) in enumerate(zip(handles, labels)) if l not in labels[:i]
    ]
    ax.legend(*zip(*unique))

for example in data:
    ax.scatter(
        x=example[0],
        y=example[1],
        color=LABEL_PLOT_COLOUR_MAP[example[2]],
        label=LABEL_MAP[example[2]],
        marker="o",
    )

legend_without_duplicate_labels(ax)
ax.set_title("Training Data")
plt.show()
```

![Train Data](../7%20-%20assets/Label%20Propagation%20Algorithm/train_data.png)

Fit the model:
```python
from sklearn.semi_supervised import LabelPropagation

label_propagation_model = LabelPropagation()
label_propagation_model.fit(data[:, :2], data[:, 2])
predictions = label_propagation_model.predict(data[:, :2])
predicted_probs = label_propagation_model.predict_proba(data[:, :2])

plt.figure(figsize=(10, 5))
plt.scatter(
    x=data[:, 0],
    y=data[:, 1],
    color=np.vectorize(LABEL_PLOT_COLOUR_MAP.get)(predictions),
)
plt.title("Label Predictions")
plt.show()
```

![Model Predictions](../7%20-%20assets/Label%20Propagation%20Algorithm/model_preds.png)

## References
* https://scikit-learn.org/stable/modules/generated/sklearn.semi_supervised.LabelPropagation.html
* "Boosting vs. semi-supervised learning" (Vincent Warmerdam) https://www.youtube.com/watch?v=2eU_8ExBzDw
* "Learning from Labeled and Unlabeled Data with Label Propagation" (Xiaojin Zhu, Zoubin Ghahramani 2002). https://pages.cs.wisc.edu/~jerryzhu/pub/CMU-CALD-02-107.pdf
## Related 
* [[Machine Learning on Small Datasets]]
* [[Radial Basis Function]]
* [[Scikit-Learn]]