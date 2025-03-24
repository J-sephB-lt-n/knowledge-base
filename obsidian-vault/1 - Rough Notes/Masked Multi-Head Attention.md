---
created:
  - 2024-11-07T13:34
modified: 2025-03-19 08:50
tags:
  - nlp
  - natural-language-processing
  - llm
  - large-language-model
  - gpt
  - llama
type:
  - note
status:
  - in-progress
---
I didn't get to finish this exercise in documenting an intuitive explanation of attention, so I'm putting all of my python code here so that I can pick it up again later.

![](../7%20-%20assets/Masked%20Multi-Head%20Attention/toy_attention_example.png)

```python
from typing import Optional

import altair as alt
import numpy as np
from pydantic import BaseModel, ConfigDict

alt.renderers.enable("browser")


class DataPoint(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    name: str
    coords: np.ndarray
    group: str


word_embeddings: list[DataPoint] = [
    DataPoint(name="hope", coords=np.array([-1, 1]), group="word_embeddings"),
    DataPoint(name="exuberance", coords=np.array([1, 1]), group="word_embeddings"),
    DataPoint(name="hate", coords=np.array([-1, -1]), group="word_embeddings"),
    DataPoint(name="sycophant", coords=np.array([1, -1]), group="word_embeddings"),
]


def altair_scatterplot_with_point_labels(
    data: list[DataPoint],
    x_label: str,
    y_label: str,
    plot_title: str | dict,
    force_axis_ranges_match: bool = False,
) -> alt.LayerChart:
    """
    Creates an altair scatterplot in which each data point is annotated, coloured by label
    """
    plot_data: list[dict] = [
        {
            "word": data_point.name,
            "x": data_point.coords[0],
            "y": data_point.coords[1],
            "group": data_point.group,
        }
        for data_point in data
    ]
    if force_axis_ranges_match:
        min_value: np.float64 = min([min(x.coords[0], x.coords[1]) for x in data])
        max_value: np.float64 = max([max(x.coords[0], x.coords[1]) for x in data])
        x_scale = alt.Scale(
            domain=[min_value, max_value],
        )
        y_scale = alt.Scale(
            domain=[min_value, max_value],
        )
    else:
        x_scale = alt.Scale(
            domain=[
                min([float(x.coords[0]) for x in data]),
                max([float(x.coords[0]) for x in data]),
            ],
        )
        y_scale = alt.Scale(
            domain=[
                min([float(x.coords[1]) for x in data]),
                max([float(x.coords[1]) for x in data]),
            ],
        )
    scatter_plot: alt.Chart = (
        alt.Chart(alt.Data(values=plot_data))
        .mark_circle(size=60)
        .encode(
            x=alt.X("x:Q", title=x_label, scale=x_scale),
            y=alt.Y("y:Q", title=y_label, scale=y_scale),
            color=alt.Color("group:N", title="Group"),
        )
        .properties(title=plot_title)
    )
    plot_text: alt.Chart = scatter_plot.mark_text(
        align="left",
        dx=5,
        dy=-5,
    ).encode(text="word:N")
    line_x0 = alt.Chart().mark_rule(color="black").encode(x=alt.datum(0))
    line_y0 = alt.Chart().mark_rule(color="black").encode(y=alt.datum(0))
    scatter_plot = scatter_plot + plot_text + line_x0 + line_y0

    return scatter_plot


def altair_plotgrid(
    plots_list: list[alt.Chart | alt.LayerChart],
    n_plots_per_row: int,
) -> alt.VConcatChart:
    """
    Combines a list of altair plots into a single plot by laying them out in a grid
    """
    plot_rows: list[list[alt.Chart | alt.LayerChart]] = []
    for plot_num, plot in enumerate(plots_list):
        plot_row_num: int = plot_num // n_plots_per_row
        try:
            plot_rows[plot_row_num].append(plot)
        except IndexError:
            plot_rows.append([plot])
    return alt.vconcat(*[alt.hconcat(*plot_row) for plot_row in plot_rows])


altair_scatterplot_with_point_labels(
    data=word_embeddings,
    x_label="xlab",
    y_label="ylab",
    plot_title="title here",
    force_axis_ranges_match=True,
).display()


def random_attention_example(word_embeddings: list[DataPoint]) -> alt.VConcatChart:
    """Generates Key and Query matrices with random values and 
    displays the resulting attention values on a grid of altair plots
    """
    key_matrix: np.ndarray = np.random.uniform(low=-1, high=1, size=(2, 2))
    query_matrix: np.ndarray = np.random.uniform(low=-1, high=1, size=(2, 2))
    key_vectors: list[DataPoint] = [
        DataPoint(name=word.name, coords=word.coords @ key_matrix, group="key")
        for word in word_embeddings
    ]
    query_vectors: list[DataPoint] = [
        DataPoint(name=word.name, coords=word.coords @ query_matrix, group="query")
        for word in word_embeddings
    ]
    output_plots_list: list[alt.LayerChart] = []
    for query_vector in query_vectors:
        raw_attention_scores: dict[str, np.float64] = {
            key_vector.name: query_vector.coords @ key_vector.coords
            for key_vector in key_vectors
        }
        raw_attention_score_matrix: np.ndarray = np.array(
            list(raw_attention_scores.values()),
        )
        exp_values: np.ndarray = np.exp(
            raw_attention_score_matrix - np.max(raw_attention_score_matrix)
        )
        softmax_values: np.ndarray = exp_values / np.sum(exp_values)
        normalised_attention_scores: dict[str, np.float64] = {
            key: val for key, val in zip(raw_attention_scores.keys(), softmax_values)
        }
        attention_description_text: list[str] = []
        attention_description_text.append(
            f"Attention scores for query word '{query_vector.name}':"
        )
        for word, attention_score in normalised_attention_scores.items():
            attention_description_text.append(f"'{word}': {attention_score:.2f}")
        output_plots_list.append(
            altair_scatterplot_with_point_labels(
                data=key_vectors + [query_vector],
                x_label="xlab",
                y_label="ylab",
                plot_title={"text": attention_description_text},
                force_axis_ranges_match=True,
            )
        )

    return altair_plotgrid(
        plots_list=output_plots_list,
        n_plots_per_row=2,
    )


random_attention_example(word_embeddings).display()
```
## References
* Links to references (source material) go here
## Related
* [The GPT Architecture](The%20GPT%20Architecture.md)