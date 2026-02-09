---
created:
  - 2025-09-27T21:31
modified: 2025-09-30 10:31
tags:
  - ai
  - agent
  - agentic
  - gpt
  - llm-agents
type:
  - note
status:
  - in-progress
---
TLDR: the best middle ground for me is check out all of the libraries and frameworks. Pull in things that are light, well-maintained and too complex to build, and build the rest myself.

| Goal                                          | Best Choice                |
| --------------------------------------------- | -------------------------- |
| Working POC as fast as possible               | Existing framework/library |
| Less code to maintain (less boilerplate code) | Existing framework/library |
| Flexibility                                   | Build yourself             |
| Clarity                                       | Build yourself             |
| Understanding of the underlying system        | Build yourself             |
| Good logging, tracing and debugging           | ?                          |
| Personal growth                               | Do both                    |
| Less maintenance burden                       | Build yourself             |
| Performance (e.g. latency, memory)            | Build yourself             |
| Portability (no lock-in)                      | Build yourself             |

| Functionality                 | Should Use an existing AI library (in my opinion)                                        |
| ----------------------------- | ---------------------------------------------------------------------------------------- |
| Structured outputs            | Closed source models: Build yourself.<br>Open source models: Use *outlines*, or similar. |
| Tool calling                  | No. Build yourself.                                                                      |
| Agent tools                   | Simple tools: Build yourself<br>Complex tools: Outsource                                 |
| Agent loop                    | Quick: outsource<br>Performant: build yourself                                           |
| Retry loops                   | No. Build yourself                                                                       |
| Browser use                   | ?                                                                                        |
| System evaluation             | ?                                                                                        |
| Logging/tracing/observability | ?                                                                                        |
| Agent memory                  | Simple: build yourself.<br>Complex: outsource or copy 3rd party implementation.          |
|                               |                                                                                          |

## LangChain

- I started out with the LangGraph docs, since the community seems to like LangGraph a lot more than LangChain.
- The docs said that LangGraph (and LangChain) *v1* is coming out in October 2025 (next month). So I must choose between stable *< v1* or beta *v1*. I proceed with unstable beta *v1*.
- LangGraph docs link me to the LangGraph ReAct agent.
- I implement the LangChain ReAct agent (*create_react_agent*). It works perfectly pretty much out of the box.
- Tools which return image output don't work at all. I need to do a manual hack, editing the agent message history myself while iterating through each agent step.
- I want to log all request/response pairs to the OpenAI API. I see that Lang{Chain,Graph} uses LangSmith for tracing. Turns out you have to pay for LangSmith. I end up implementing a callback for logging. This is not straightforward, nor do the docs help much. I hack together something by combining bits of suggestions from gpt-5 and gemini-2.5-pro. Both models mix up different LangChain versions.
- The callback approach doesn't work because I'm using LangChain v1. 

## References

* Links to references (source material) go here
## Related

* Links to other notes which are directly related go here
- [Choosing a LLM Agent Framework](<Choosing%20a%20LLM%20Agent%20Framework.md>)
