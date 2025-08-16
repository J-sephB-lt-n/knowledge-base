---
created:
  - 2025-06-08T20:52
modified: 2025-08-16 22:31
tags:
  - gpt
  - transformer
  - large-language-model
  - llm
  - memory
  - agent
  - llm-agents
  - agent-memory
  - llm-memory
type:
  - note
status:
  - in-progress
---
[MemGPT](MemGPT.md) is a memory-management framework for LLM agents, designed to overcome the limitation of fixed context length.

Operating systems use *virtual memory*, meaning that they move data cleverly between disk and RAM to give programs the illusion of more RAM than there really is. [MemGPT](MemGPT.md) was inspired by this approach.

The main concept behind [MemGPT](MemGPT.md) is to give the LLM tools which it can use to manage it's own memory (add and remove things from it's own context).

The content of this note is based both on the [original MemGPT paper](https://arxiv.org/abs/2310.08560) and the [Letta](https://github.com/letta-ai/letta) implementation (e.g. see [this Letta prompt](https://github.com/letta-ai/letta/blob/main/letta/prompts/system/memgpt_base.txt)).     

The model context (i.e. the prompt received by the model on each chat completion call) looks like this:

$$
\begin{array}{@{} l @{\qquad} l @{}}
\left.\begin{array}{l}
\text{.........................}\\
\text{.........................}
\end{array}\right\} &
\begin{array}{l}
\textbf{SYSTEM PROMPT}\\
\text{(explains control flow, available memory types and tools)}
\end{array}
\\[10pt]
\left.\begin{array}{l}
\text{.........................}\\
\text{.........................}\\
\text{.........................}\\
\text{.........................}
\end{array}\right\} &
\begin{array}{l}
\textbf{WORKING CONTEXT (CORE MEMORY)}\\
\text{fixed-size block of unstructured text}\\
\text{can only be edited using MemGPT function calls (tools)}\\
\end{array}
\\[10pt]
\left.\begin{array}{l}
\text{.........................}\\
\text{.........................}\\
\text{.........................}\\
\text{.........................}
\end{array}\right\} &
\begin{array}{l}
\textbf{RECURSIVE CONVERSATION SUMMARY}\\
\text{concise summary of all old chat messages not in recent chat history}\\
\text{generated recursively (summary is periodically updated)}\\
\end{array}
\\[10pt]
\left.\begin{array}{l}
\text{USER: ..............}\\
\text{ASSISTANT: ...}\\
\text{USER: ..............}\\
\text{ASSISTANT: ...}\\
\text{SYSTEM: .........}\\
\text{USER: ...............}\\
\text{.........................}
\end{array}\right\} &
\begin{array}{l}
\text{RECENT CHAT HISTORY}\\
\text{rolling history of $n$ most recent chat messages}\\
\text{includes notifications (e.g. context limit warnings)}\\
\text{includes tool calls, results and errors}
\end{array}
\end{array}
$$


The tools available to the LLM agent are:

| Tool                   | Description                                                    |
| ---------------------- | -------------------------------------------------------------- |
| coversation_search     | Search over the full conversation history (stored in database) |
| core_memory_append     | Add something to working context                               |
| core_memory_replace    | Replace working context with new content                       |
| archival_memory_insert | Add a fact to long-term storage (e.g. vector database)         |
| archival_memory_search | Search in long-term storage (e.g. vector database)             |

I started writing some pseudo-code, but I haven't finished it:

```python
## Pseudo-code

```python
short_term_memory: list[ChatMessage] = []
short_term_memory.append(MAIN_SYSTEM_PROMPT)

while True:
	user_input = get_user_input()
	short_term_memory.append(
		ChatMessage(role="user", content=user_input)
	)
	
	if count_tokens(short_term_memory) > SHORT_TERM_LIMIT_CUTOFF_N_TOKENS:
	   short_term_memory = discard_oldest_messages(
			short_term_memory,
			fraction=0.5, # discard oldest 50% of messages
			# MAIN_SYSTEM_PROMPT is always kept as first message 
		)
	   
	if count_tokens(short_term_memory) > SHORT_TERM_LIMIT_WARNING_N_TOKENS:
	    short_term_memory.append(
			ChatMessage(
				role="system",
				content="""
					Short-term memory is almost full.
					...TODO
					"""
			)
		)
	)
	
	llm_response = llm.chat_completion(
		messages=short_term_memory
		tools = (
			...	
		)	
	)
	
	for tool, tool_kwargs in llm_response.tool_calls:
		tool_result: str | None = tool(
			short_term_memory,
			**tool_kwargs,
		)
		if tool_result:
			short_term_memory.append(
				ChatMessage(
					role="tool",
					content=tool_result	
				)
			)
```

## References
* [original paper (arxiv)](https://arxiv.org/abs/2310.08560)
## Related
* [LLM Memory](LLM%20Memory.md)
* [LLM Agents](LLM%20Agents.md)
* [Mem0 - Building Production-Ready AI Agents with Scalable Long-Term Memory](Mem0%20-%20Building%20Production-Ready%20AI%20Agents%20with%20Scalable%20Long-Term%20Memory.md)
* [MemEngine](MemEngine.md)
* [MemGPT](MemGPT.md)
* [Zep - A Temporal Knowledge Graph Architecture for Agent Memory](Zep%20-%20A%20Temporal%20Knowledge%20Graph%20Architecture%20for%20Agent%20Memory.md)