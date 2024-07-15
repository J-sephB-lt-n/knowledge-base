---
created:
  - 2024-06-26T20:52
modified: 2024-07-15 13:30
tags:
  - llm
  - nlp
  - large-language-model
  - llm-agents
type:
  - note
status:
  - completed
---
(paper) ReAct: Synergizing Reasoning and Acting in Language Models (https://arxiv.org/abs/2210.03629)

_ReAct prompting_ is a prompting style used to induce reasoning from LLMs in an [[LLM Agents]] system. 

_ReAct prompting_ involves inducing the large language model to solve a problem through multiple _thought-action-observation_ steps. This is achieved through _few-shot prompting_ i.e. including several examples of how it the task should be solved within the prompt, before giving the model the actual task.

Here is an example prompt from the original paper:
(this is just showing the model a single example - the real prompt should contain multiple examples):
__QUESTION__: Were Pavel Urysohn and Leonid Levin known for the same type of work?
__THOUGHT 1__: I need to search Pavel Urysohn and Leonid Levin, find their types of work,
then find if they are the same.
__ACTION 1__: Search[Pavel Urysohn]
__OBSERVATION 1__: Pavel Samuilovich Urysohn (February 3, 1898 - August 17, 1924) was a Soviet
mathematician who is best known for his contributions in dimension theory.
__THOUGHT 2__: Pavel Urysohn is a mathematician. I need to search Leonid Levin next and
find its type of work.
__Action 2__: Search[Leonid Levin]
__Observation 2__: Leonid Anatolievich Levin is a Soviet-American mathematician and computer
scientist.
__Thought 3__: Leonid Levin is a mathematician and computer scientist. So Pavel Urysohn
and Leonid Levin have the same type of work.
__Action 3__: Finish[yes]

## Related
* [[Applied Large Language Model Concepts]]
## References
* ReAct: Synergizing Reasoning and Acting in Language Models https://arxiv.org/abs/2210.03629