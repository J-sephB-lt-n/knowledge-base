---
created:
  - 2024-10-19T14:13
modified: 2024-10-19 23:47
tags:
  - llm
  - large-language-model
  - genAI
  - ai
  - survey
  - agent
  - llm-agents
type:
  - paper
status:
  - in-progress
---
Link to the (open access) paper: https://link.springer.com/article/10.1007/s11704-024-40231-1

Contents of this note:
1. [Agent Profile/Persona](#Agent%20Profile/Persona)
2. [Agent Memory Module](#Agent%20Memory%20Module)
3. [Agent Planning Module](#Agent%20Planning%20Module)
4. [Agent Action Module](#Agent%20Action%20Module)
## Agent Profile/Persona

## Agent Memory Module

## Agent Planning Module
_Planning_ means the ability of LLM agents to break down a complex task into a sequence of smaller (easier) subtasks.
There are 2 broad approaches: 
* [Agent Planning without Feedback](#Agent%20Planning%20without%20Feedback)
* [Agent Planning with Feedback](#Agent%20Planning%20with%20Feedback)
#### Agent Planning without Feedback
- "Single-path reasoning" approaches coerce the model (most often via the prompt) into solving the problem via a cascading sequence of subtasks (i.e. 1 step at a time with no branching). Examples are [Chain of Thought (CoT)](https://arxiv.org/abs/2201.11903), [zero-shot CoT](https://arxiv.org/abs/2205.11916), [Plan Generation via Re-prompting](https://openreview.net/pdf?id=cMDMRBe1TKs)
- "Multi-path reasoning" approaches coerce the model (most often via the prompt) into exploring multiple (possibly branching ) reasoning paths. Examples are [Self-consistent CoT (CoT-SC)](TODO), [Tree of Thoughts (ToT)](https://arxiv.org/abs/2305.10601), [Graph of Thoughts (GoT)](https://arxiv.org/abs/2308.09687),   

#### Agent Planning with Feedback

## Agent Action Module 


## References
* [A survey on large language model based autonomous agents](https://link.springer.com/article/10.1007/s11704-024-40231-1)
* [# Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903) 
* [Large Language Models are Zero-Shot Reasoners](https://arxiv.org/abs/2205.11916)
* [Planning with Large Language Models via Corrective Re-prompting](https://openreview.net/pdf?id=cMDMRBe1TKs)
## Related
* [LLM Agents](LLM%20Agents.md)