---
created:
  - 2024-06-26T21:03
modified: 2024-07-15 13:18
tags:
  - llm
  - large-language-model
  - nlp
type:
  - note
status:
  - completed
---
(original paper) "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models" https://arxiv.org/abs/2201.11903

_Chain-of-Thought_ prompting is a variant of _few-shot prompting_ in which the language model is shown a few examples within it's prompt of how it should break down it's task in a logical way. 

Example prompt (from the original paper):
Q: Take the last letters of the words in "Elon Musk" and concatenate them.
A: The last letter of "Elon" is "n". The last letter of "Musk" is "k". Concatenating them is "nk". The answer is nk.
Q: Take the last letters of the words in "Larry Page" and concatenate them.
A: The last letter of "Larry" is "y". The last letter of "Page" is "e". Concatenating them is "ye". The answer is ye.
Q: Take the last letters of the words in "Sergey Brin" and concatenate them.
A: The last letter of "Sergey" is "y". The last letter of "Brin" is "n". Concatenating them is "yn". The answer is
yn.
Q: Take the last letters of the words in "Bill Gates" and concatenate them.
A:

## Zero-shot Chain-of-Thought Prompting
In the paper "Large Language Models are Zero-Shot Reasoners" (https://arxiv.org/abs/2205.11916), the authors observed that simply appending the text "Let's think step by step" to the end of the model prompt notably improved model performance. 
## Related
* [[Applied Large Language Model Concepts]]
* [[One-Shot and Few-Shot Learning]]
* [[LLM ReAct Prompting]]
## References
* (paper) Chain-of-Thought Prompting Elicits Reasoning in Large Language Models (https://arxiv.org/abs/2201.11903)
* https://www.promptingguide.ai/techniques/cot