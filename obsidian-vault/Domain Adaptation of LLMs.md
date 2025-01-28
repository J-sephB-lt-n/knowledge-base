---
created:
  - 2025-01-27T12:39
modified: 2025-01-28 10:15
tags:
  - llm
  - fine-tuning
  - large-language-model
  - gpt
  - nlp
  - lora
  - qlora
  - prompt-engineering
  - in-context-learning
  - zero-shot
  - zero-shot-learning
  - few-shot-learning
  - few-shot
  - domain-adaptation
type:
  - note
status:
  - in-progress
---
Main body of note goes here

## Possible approaches to LLM Domain Adaptation

In decreasing order of difficulty:

| Approach                                               | Description                                                                                                                | Use-Case                                                                                                                                                                                                                                                                                                                                                                                                        | Cons                                                                                                                                                                                                                         |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pretraining                                            | Training a new foundation model 100% from scratch for your task                                                            | You are OpenAI                                                                                                                                                                                                                                                                                                                                                                                                  | Prohibitively expensive (computation, data and money)                                                                                                                                                                        |
| Continued pretraining                                  | Carry on training of the foundation model in the same self-supervised manner as pretraining, but with new unseen data      | There is a massive amount of unlabeled data very relevant to the domain, which was unavailable during *pretraining*                                                                                                                                                                                                                                                                                             | - Prohibitively expensive.<br>- Prone to "catastrophic forgetting" i.e. the model losing existing skills and knowledge previously learned                                                                                    |
| Fine-tuning                                            | Modify the model weights in a supervised manner (using annotated examples)                                                 | For changing base LLM behaviour/tone:<br>- Tone, style or output format customisation (e.g. instruction following)<br>- Increased skill in specific niche tasks<br>- General performance in a niche domain missing from LLM's pretraining data (e.g. a rare human language)<br>-  Distill a bigger model into a smaller model (a smaller fine-tuned LLM can outperform a bigger general LLM on a specific task) | - Not very effective at introducing new knowledge to the model (rather use RAG)<br>- Computationally expensive<br>- Requires a large amount of labelled examples<br>- Can also sometimes result in "catastrophic forgetting" |
| Parameter-efficient fine-tuning (PEFT)                 | Same as fine-tuning, but only updates a subset of the weights (or a small set of added weights)                            | Same as *fine-tuning*, but cheaper and less prone to "catastrophic forgetting" (and sometimes less effective)                                                                                                                                                                                                                                                                                                   | - Same as *fine-tuning*, but sometimes PEFT is less effective                                                                                                                                                                |
| Retrieval-Augmented Generation (RAG)                   | Provides context to the LLM by putting user query into a search engine then including the search results in the LLM prompt | - Reducing hallucinations<br>- Increased model trust and transparency (can produce references)<br>- Underlying knowledge base changes often                                                                                                                                                                                                                                                                     | - Requires implementation and maintenance of a knowledge base (e.g. database) and retrieval (search) system<br>- Increased token cost<br>- Increased inference time                                                          |
| In-context Learning (ICL)<br>A.K.A. prompt-engineering | Adding examples or other instructions in the LLM prompt directly <br>(e.g. few-shot learning, ReACT, Chain-Of-Thought)     | Quickest and easiest way to quickly modify model behaviour                                                                                                                                                                                                                                                                                                                                                      | - Increased token cost<br>- Increased inference time<br>- If too many examples/instructions are given, LLM may start to ignore some of them                                                                                  |

## Choosing the Correct Domain Adaptation Method

![](../7%20-%20assets/Possible%20approaches%20to%20LLM%20Domain%20Adaptation/choose_domain_adaptation_method.png)
Source: https://ai.meta.com/blog/adapting-large-language-models-llms/
## Use-cases

## Other notes

Algorithms like LoRA and QLoRa make tuning large models more feasible
## References
* [(meta blog part 1) Methods for adapting large language models](https://ai.meta.com/blog/adapting-large-language-models-llms/)
	* [(meta blog part 2) To fine-tune or not to fine-tune](https://ai.meta.com/blog/when-to-fine-tune-llms-vs-other-techniques/)
* [LoRA Land: 310 Fine-tuned LLMs that Rival GPT-4, A Technical Report](https://arxiv.org/abs/2405.00732)
* https://www.llama.com/docs/how-to-guides/fine-tuning/
## Related

* Links to other notes which are directly related go here