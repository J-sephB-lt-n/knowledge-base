---
created:
  - 2025-03-31T22:17
modified: 2025-06-23 09:56
tags:
  - llm
  - gpt
  - chat-gpt
  - large-language-model
  - nlp
  - natural-language-processing
  - genAI
  - ai
  - probability
  - distribution
  - token
  - tokenisation
  - transformer
type:
  - note
status:
  - completed
---
The output of a GPT Large Language Model (LLM) is a vector of scores, containing one score $y_i$ for each possible next token in the sequence.

The final output probability $p_i$ of each token is calculated as 

$$p_i\quad=\quad\displaystyle\frac{e^{\frac{y_i}{T}}}{\displaystyle\sum_{j}e^{\frac{y_j}{T}}}$$
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

![](../7%20-%20assets/LLM%20logprobs%20and%20temperature/example_temperature_plot.png)


```python
import numpy as np
import matplotlib.pyplot as plt

# Raw logits for the 3 tokens
logits = np.array([1.0, 2.0, 3.0])

# Temperature values from 0.01 to 2 (avoid 0 to prevent divide-by-zero)
temperatures = np.linspace(0.01, 2, 200)

# Compute probabilities for each temperature
probs = []
for T in temperatures:
    scaled_logits = logits / T
    exp_logits = np.exp(scaled_logits - np.max(scaled_logits))  # for numerical stability
    prob = exp_logits / exp_logits.sum()
    probs.append(prob)

probs = np.array(probs)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(temperatures, probs[:, 0], label="token1")
plt.plot(temperatures, probs[:, 1], label="token2")
plt.plot(temperatures, probs[:, 2], label="token3")

plt.axvline(x=1.0, color='gray', linestyle='--', label='temperature=1')

plt.xlabel("Temperature")
plt.ylabel("Token Probability")
plt.title("Effect of Temperature on Token Probabilities")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("example_temperature_plot.png")
```

## References
* Links to references (source material) go here
## Related
* [The GPT Architecture](The%20GPT%20Architecture.md)