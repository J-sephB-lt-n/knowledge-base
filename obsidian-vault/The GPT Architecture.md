---
created:
  - 2024-10-16T10:14
modified: 2024-10-17 16:40
tags:
  - llm
  - gpt
  - transformer
  - neural-network
  - deep-learning
  - architecture
type:
  - note
status:
  - in-progress
---
Main body of note goes here

## The Basic GPT Architecture

![source: "Build a Large Language Model (From Scratch)" by Sebastian Raschka](../7%20-%20assets/The%20GPT%20Architecture/gpt_architecture_illus.png)

| Layer/step                  | Brief Explanation                                                                |
| --------------------------- | -------------------------------------------------------------------------------- |
| Output                      |                                                                                  |
| Linear output layer         |                                                                                  |
| Dropout                     |                                                                                  |
| Feed forward                |                                                                                  |
| LayerNorm 2                 |                                                                                  |
| Masked multi-head attention | refer to section [Masked multi-head attention](#Masked%20multi-head%20attention) |
| LayerNorm 1                 |                                                                                  |
| Positional embedding layer  |                                                                                  |
| Token embedding layer       |                                                                                  |
| Tokenized text              |                                                                                  |

## Masked multi-head attention

![source: "Build a Large Language Model (From Scratch)" by Sebastian Raschka](../7%20-%20assets/The%20GPT%20Architecture/attention_illus.png)

## References
* [Build a Large Language Model (From Scratch)](Build%20a%20Large%20Language%20Model%20(From%20Scratch).md)
## Related
* [LLM Strengths & Weaknesses](LLM%20Strengths%20&%20Weaknesses.md)