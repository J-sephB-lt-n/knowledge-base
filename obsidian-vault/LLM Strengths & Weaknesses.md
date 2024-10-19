---
created:
  - 2024-08-27T09:21
  - 2024-08-29T20:01
modified: 2024-10-16 12:54
tags:
  - llm
  - large-language-model
  - nlp
  - gpt
  - llama
  - llama-cpp
type:
  - note
status:
  - in-progress
---
In this note, I am talking specifically about decoder-only autoregressive text generators (such as the GPT and LLama models).
Large Language Models (LLMs) are auto-regressive text generators (i.e. they generate text one word at a time). By applying additional logic, they can also act as agents, collaborate with each other and use tools (this is achieved by asking them in natural language what they would like to do - some are specifically fine-tuned to respond with structured output facilitating e.g. JSON output, API calls etc.). 
They are pretrained on massive amounts of existing text data (which means that they memorise superhuman amounts of information and complex language patterns - essentially the entire internet) and then are then fine-tuned on specific tasks such as chatting to a human, instruction-following, function-calling etc.

What language models are good at:

| Task                                                 | Reason                                                                                                                                                                                                                                          | Notes                                                                                                      |
| ---------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| Text generation                                      | LLMs are explicitly trained to generate plausible text in natural language. This is their greatest strength.<br>However, they will not perform well on niche domains (e.g. generating in languages not well-represented in their training data) | This includes generating code, which has many structural similarities with spoken language                 |
| Text summarisation                                   |                                                                                                                                                                                                                                                 |                                                                                                            |
| Zero-shot classification (based on natural language) | LLMs explicitly memorise a lot of information during their pretraining (i.e. have a lot of contextual understanding), and also have a nuanced "understanding" of natural language.                                                              | LLMs will not perform well on tasks in niche domains which are not well-represented in their training data |

What language models are bad at:

| Task                                                                                           | Reason                                | Notes                                                                                                                                                                                                              |
| ---------------------------------------------------------------------------------------------- | :------------------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Reasoning                                                                                      |                                       | LLMs can be tricked into behaviour which resembles reasoning through a combination of clever prompting (e.g. chain-of-thought, self-consistency, ReAct etc.), collaboration, self-evaluation and function-calling. |
| Achieving coherent structure when generating long documents                                    |                                       | There are algorithms (such as XXX which can partially alleviate this issue)                                                                                                                                        |
| Question-answering on knowledge sparsely represented in (or missing from) their training data  |                                       | This problem is addressed by Retrieval-Augmented Generation (RAG).                                                                                                                                                 |
| Working with numbers e.g. producing probability estimates, time series forecasting, regression | LLMs are trained on text and language | LLMs can however use tools and/or generate code which may perform these tasks very well                                                                                                                            |
## References

* Links to references (source material) go here
## Related

* Links to other notes which are directly related go here
## References
* https://www.promptingguide.ai/
## Related
* [[Applied Large Language Model Concepts]]
* [[LLM Agents]]