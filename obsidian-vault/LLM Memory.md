---
created:
  - 2025-06-08T20:51
modified: 2025-09-11 11:15
tags:
  - llm
  - gpt
  - large-language-model
  - context
  - context-window
  - agent
  - llm-agents
  - memory
  - conversation
  - chatbot
  - chat
type:
  - map-of-content
status:
  - in-progress
---
[LLM Memory](LLM%20Memory.md)

## Types of Agent Memory

| Name                                                                         | Example                                                                                        |
| ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Information Extraction                                                       | Can you remind me what you told me earlier about pasta                                         |
| Multi-session Reasoning                                                      | How many times have we discussed jazz, and what were the specific topics which we discussed?   |
| Temporal Reasoning (changes in user info over time)                          | How long has it been since I broke up with my girlfriend?                                      |
| Knowledge Updates (user state has reversed/changed)                          | What is my opinion on autonomous AI coding?                                                    |
| Abstention (LLM can identify when information is not in memory/chat history) | Please remind me what you told me earlier about X.<br>Assistant: "We have not spoken about X?" |
|                                                                              |                                                                                                |

## Approaches (memory types)

Multiple of these different memory types/modules/paradigms can be implemented in the same AI/LLM agent at once (e.g. a recursive conversation summary, a knowledge graph and working memory with custom templates).

| Name                                    | Description                                                                                                                                                                                                                                                                  |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Semantic Recall (vector memory)         | Save memories as vectors (dense embedding and/or keyword based like BM25). At generation time, fetch semantically most relevant memories and inject them into the prompt.                                                                                                    |
| Knowledge Graph                         |                                                                                                                                                                                                                                                                              |
| Working Memory with Custom Templates    | LLM manages it's own memory within a custom (e.g. markdown) template (with different sections for different memories e.g. `user preferences`, `user info`, `chat metrics` etc.).<br>This is powerful since it forces the LLM to structure it's thinking in a predefined way. |
| Self-Managed Memory (e.g. MemGPT, Mem0) | LLM agent is given tools ...TODO<br>This could also include storing memories in a SQL database which the agent can directly query.                                                                                                                                           |
| Recursive Summarisation                 | Older chat history is periodically incorporated into a rolling summary text.<br>There could also be multiple recursive summaries kept (e.g. each with a different topic, very similar to `Working Memory with Custom Templates` discussed above)                             |

## Frameworks 

| Name           | Summary | Link                                                                                                                                                                        |
| -------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MemEngine      |         | [MemEngine](MemEngine.md)                                                                                                                                                   |
| MemGPT (Letta) |         | [MemGPT](MemGPT.md)                                                                                                                                                         |
| Mem0           |         | [Mem0 - Building Production-Ready AI Agents with Scalable Long-Term Memory](Mem0%20-%20Building%20Production-Ready%20AI%20Agents%20with%20Scalable%20Long-Term%20Memory.md) |
| Zep            |         | [Zep - A Temporal Knowledge Graph Architecture for Agent Memory](Zep%20-%20A%20Temporal%20Knowledge%20Graph%20Architecture%20for%20Agent%20Memory.md)                       |
|                |         |                                                                                                                                                                             |

## Optimisations Observed by Mastra

Taken from [this youtube presentation](https://www.youtube.com/watch?v=FTokJt1ioeg).
The following were observed to improve performance on LongMemEval:
1. LLM writes it's own custom template for working memory based on it's task.
2. Granular memory updates (don't make LLM replace pieces of memory text in the memory template, just edit the specific relevant piece).
3. Adding a date/timestamp into the prompt allows the LLM to do temporal reasoning.
4. Data structures matter a lot. They moved from a simple JSON dump to
   ```
	 On July 1st 2025:
		 At 2:00pm in conversation ID {session_id}: {json.dumps(messages[0])}
		 At 2:57pm in conversation ID {session_id}: {json.dumps(messages[1])}
	 On July 3rd 2025:
		 ...
	 ```
	 and saw a 6 percentage point improvement.
 5. Configuration matters. e.g. the number of retrieved memories *k* matters a lot.

## Other Notes
## References
* [Using LongMemEval to Improve Agent Memory](https://www.youtube.com/watch?v=FTokJt1ioeg)
* LongMemEval
## Related
* [MemEngine](MemEngine.md)
* [MemGPT](MemGPT.md)
* [Mem0 - Building Production-Ready AI Agents with Scalable Long-Term Memory](Mem0%20-%20Building%20Production-Ready%20AI%20Agents%20with%20Scalable%20Long-Term%20Memory.md)
* [Zep - A Temporal Knowledge Graph Architecture for Agent Memory](Zep%20-%20A%20Temporal%20Knowledge%20Graph%20Architecture%20for%20Agent%20Memory.md)