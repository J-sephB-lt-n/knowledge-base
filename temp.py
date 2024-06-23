import matplotlib.pyplot as plt
import numpy as np

LABEL_MAP = {-1: "label_unknown", 0: "class-1", 1: "class-2", 2: "class-3"}
LABEL_PLOT_COLOUR_MAP = {-1: "grey", 0: "red", 1: "blue", 2: "green"}
data = np.array(
    # each entry is {x, y, label}
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
        [18, 10, 1],
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
        [35, 4, -1],
        [38, 2, -1],
        [41, 0, -1],
        [43, 0, -1],
        [48, 0, -1],
        [35, 6, -1],
        [39, 6, -1],
        [41, 6, -1],
        [45, 6, -1],
        [50, 6, 0],
        [28, 8, -1],
        [43, 10, -1],
        [37, 8, -1],
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
