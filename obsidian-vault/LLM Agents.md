---
created:
  - 2024-07-15T10:05
modified: 2024-07-15 13:31
tags:
  - llm
  - large-language-model
  - llm-agents
  - retrieval-augmented-generation
  - rag
type:
  - note
status:
  - in-progress
---
_LLM-based agents_ is a reasoning engine based on large language models. 
_LLM-based agents_ refers to a system in which LLMs execute complex tasks through sequential reasoning, and their augmentation with additional modules such as planning, memory, [[Retrieval-Augmented Generation (RAG)]], code interpreter, [tool usage](#tool-usage) etc.

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
* https://www.promptingguide.ai/research/llm-agents
* https://python.langchain.com/v0.1/docs/modules/agents/ 
* A Survey on Large Language Model based Autonomous Agents https://arxiv.org/abs/2308.11432
