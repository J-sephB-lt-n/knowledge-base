---
created:
  - 2025-12-09T22:32
modified: 2025-12-11 09:10
tags:
  - ai
  - agent
  - agentic
  - dev
  - ai-dev
  - ai-development
  - ai-coding
  - code
  - coding
  - llm
  - llm-agents
  - cursor
  - claude-code
type:
  - note
status:
  - in-progress
---
## Why obsess over context?

The contents of the context window is the ONLY thing under our control which can affect the output quality of an AI coding agent.

## What the context window should be optimised for

- Correctness
- Completeness
- Size
- Trajectory
## Compaction

Compaction means the distilling of the context window into optimised and information-dense structured artifacts which can be inserted into future fresh context windows (i.e. a LLM with a fresh slate).

As a rule of thumb, Dex Horthy recommends compacting when context usage reaches 40-60%. 
## Basic Intentional Compaction

```
Write everything we did so far to progress.md, ensure to note the end goal, the approach we're taking, the steps we've done so far, and the current failure we're working on.
```

## Subagents

One way to manage context is to delegate tasks to a subagent (in order to preserve the context window of the main agent).

What this means is for the main coding agent to delegate a task to a fresh agent (i.e. an agent with an empty context window), and then only insert the final output of this subagent into the main coding agent's context. 
## Frequent Intentional Compaction (Research-Plan-Implement)

This is the final proposed code generation workflow proposed by Dex Horthy in the blog post [Getting AI to Work in Complex Codebases](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md).

It consists of a s

## References
* [original presentation (YouTube video)](https://www.youtube.com/watch?v=rmvDxxNubIg)
* https://github.com/humanlayer
* [Getting AI to work in complex codebases (HackerNews discussion)](https://news.ycombinator.com/item?id=45347532)
* [Getting AI to work in complex codebases (original article)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)
* https://github.com/humanlayer/12-factor-agents
## Related
* Links to other notes which are directly related go here