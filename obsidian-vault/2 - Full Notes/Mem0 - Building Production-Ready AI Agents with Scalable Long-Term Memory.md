---
created:
  - 2025-06-08T20:54
modified: 2025-06-10 15:52
tags:
  - memory
  - llm
  - llm-agents
  - agent
  - agentic
  - retrieval-augmented-generation
type:
  - note
status:
  - completed
---
Mem0 is an open source (ish) python framework for managing assistant memory across long conversations. 

From [this github issue](https://github.com/mem0ai/mem0/issues/2901) it appears that the package may send usage telemetry data by default unless one opts out? For this reason, I wouldn't use this package, but the algorithm is simple and elegant. 

The algorithm works as follows:

1. User sends a message (message $m_{t-1}$) and the assistant responds (message $m_t$). The $k$ most relevant memories from the memories database are injected into the system prompt of this chat (the [mem0 paper](https://arxiv.org/pdf/2504.19413) says that they used $k=10$). Every user/agent interaction (2 messages pair) uses a new fresh chat completion (no messages history is retained, other than via the memories in the system prompt).
2. After each exchange (message $m_{t-1}$ and $m_t$), a LLM is used to extract *salient* (important) memories/facts $\Omega=\{ \omega_1, ..., \omega_n \}$ for possible inclusion in the memories database. These memories are extracted from the combination of $S$ (a full summary of the conversation so far) and the last $m$ messages ($\{m_{t-m},...,m_t\}$).
   The full conversation summary $S$ is periodically updated, asynchronously from the chat itself. 
3. For each extracted fact $\omega_i$ : the *s* (original paper uses $s=10$) most similar existing memories to $\omega_i$ are retrieved from the memory store and a LLM is used to decide what to do with $\omega_i$. The LLM must use one of the following tools:
	1. **ADD()** - add a new memory to the memory store
	2. **UPDATE()** - augment an existing memory in the memory store (add new info to it)
	3. **DELETE()** - delete an existing memory from the memory store (remove existing memory contradicted by this new information)
	4. NOOP() - don't add or remove anything from the memory store. (I'm not sure why a tool call is required for this, to be honest).
## References
* [original paper (arxiv)](https://arxiv.org/pdf/2504.19413)
## Related
* [MemGPT](MemGPT.md)
* [Zep - A Temporal Knowledge Graph Architecture for Agent Memory](Zep%20-%20A%20Temporal%20Knowledge%20Graph%20Architecture%20for%20Agent%20Memory.md)
* [LLM Memory](LLM%20Memory.md)
* [LLM Agents](LLM%20Agents.md)