---
created:
  - 2024-07-15T10:05
modified: 2025-09-04 09:38
tags:
  - llm
  - large-language-model
  - llm-agents
  - retrieval-augmented-generation
  - rag
  - agent
  - agentic
type:
  - note
status:
  - in-progress
---
_LLM-based agents_ is a reasoning engine based on large language models. 
_LLM-based agents_ refers to a system in which LLMs execute complex tasks through sequential reasoning, and their augmentation with additional modules such as planning, memory, [[Retrieval-Augmented Generation (RAG)]], code interpreter, [tool usage](#tool-usage) etc.

Andrew Ng describes the following 4 Agentic Reasoning Design Patterns in his [March 2024 presentation at Sequoia Capital](https://www.youtube.com/watch?v=sal78ACtGTc&t=695s):

| Agentic Design Pattern    | Description                                                                                                                                    | Resources               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| Reflection                | Asking the LLM to check and revise it's own work (or have another LLM(s) do it)                                                                | Self-Refine, Reflexion  |
| Tool use                  | Give the LLM access to external tools (e.g. search engine, wikipedia, code execution environment etc.) and give it examples of how to use them | MM-React                |
| Planning                  | Coerce or force LLM(s) to solve a task by decomposing it into subtasks                                                                         | Chain of Thought, ReAct |
| Multi-agent collaboration | Coerce/force LLMs to debate, collaborate, delegate etc. (like a human team)                                                                    | ChatDev, AutoGen        |
| [memory](LLM%20Memory.md) |                                                                                                                                                |                         |


## Tool Usage
Examples of tools:
* Access to a clean interface with a specific knowledge base (e.g. wikipedia, google)
* File-system access
* Ability to pause execution of a process to ask for human feedback ("please help me, I'm confused/stuck")
* A database/memory store (the LLM can explicitly choose to write specific information to a memory store, and choose to access it later)
* Access to python REPL (or other sandboxed environment where the agent can run code)
* Access to WolframAlpha

## Related
* [[Applied Large Language Model Concepts]]
* [[Retrieval-Augmented Generation (RAG)]]
## References
* https://github.com/zjunlp/LLMAgentPapers
* https://www.promptingguide.ai/research/llm-agents
* https://python.langchain.com/v0.1/docs/modules/agents/ 
* A Survey on Large Language Model based Autonomous Agents https://arxiv.org/abs/2308.11432
