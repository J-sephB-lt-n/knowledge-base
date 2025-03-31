---
created:
  - 2025-03-31T22:17
modified: 2025-03-31 22:41
tags:
  - llm
  - gpt
  - chat-gpt
  - large-language-model
  - nlp
  - natural-language-processing
  - genAI
  - ai
type:
  - note
status:
  - completed
---
The output of a GPT Large Language Model (LLM) is a vector of scores, containing one score $x_i$ for each possible token.

The final output probability $p_i$ of each token is calculated as 

$$p_i\quad=\quad\displaystyle\frac{e^{\frac{x_i}{T}}}{\displaystyle\sum_{j}e^{\frac{x_j}{T}}}$$
..where $T$ is the temperature parameter.

When $T=1$, this is the standard [softmax function](https://en.wikipedia.org/wiki/Softmax_function).

Here is a simple example with 3 tokens:

| Token | score ($x_i$) | $p_i$ using ($T=1$) | $p_i$ using ($T=0.5$) | $p_i$ using ($T=0$) |
| ----- | ------------- | ------------------- | --------------------- | ------------------- |
| joe   | 1             | 0.09                | 0.0159                | 0                   |
| is    | 2             | 0.245               | 0.117                 | 0                   |
| cool  | 3             | 0.665               | 0.867                 | 1                   |

| Temperature value | Effect on token probabilities              |
| ----------------- | ------------------------------------------ |
| $T=1$             | Unaffected (standard softmax)              |
| $T>1$             | Flatter probabilities (more stochastic)    |
| $T<1$             | Sharper probabilities (more deterministic) |
## References
* Links to references (source material) go here
## Related
* Links to other notes which are directly related go here