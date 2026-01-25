---
created:
  - 2025-12-09T22:32
modified: 2026-01-19 16:06
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
## Basic Principles

- Use sub-agents for complex tasks: Instead of one monolithic prompt, decompose the problem. Use specialized prompts for sub-tasks like planning, identifying relevant files, and then generating the code.
- Use [intentional compaction](#Frequent%20Intentional%20Compaction%20(Research-Plan-Implement)): Actively manage and shrink your context to keep the agent focused on what's most important.
- Align language and naming: Use consistent naming conventions across your codebase to make it easier for the AI to understand the relationships between different parts.
- Review markdown docs to catch problems BEFORE implementation: Review the research and plan the agent creates to foster mental alignment and ensure it's on the right track.
- Practice exploratory coding: Work alongside your agent to build your own intuition and spot where the AI excels and where it needs guidance.
- CLAUDE.md > prompts > research > plans > implementation: Focus human effort on the highest-leverage parts of the pipeline.
- Phase 1 - Research: Understanding the problem and how the system works today, including filenames.
- Phase 2 - Planning: Building a step-by-step outline of the changes to make.
- Phase 3 - Implementation: Executing the plan, testing as you go, ready for surprises along the way.
## Why obsess over context?

The contents of the context window is the ONLY thing under our control which can affect the output quality of an AI coding agent.

## What the context window should be optimised for

- **Correctness** (information is all true)
- **Completeness** (all required information is present)
- **Size** (context window not too full)
- **Trajectory** ()
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

It consists of a series of steps. Each step might be repeated multiple times:
1. Research
2. Plan
3. Implement

## References
* [original presentation (YouTube video)](https://www.youtube.com/watch?v=rmvDxxNubIg)
* https://github.com/humanlayer
* [Getting AI to work in complex codebases (HackerNews discussion)](https://news.ycombinator.com/item?id=45347532)
* [Getting AI to work in complex codebases (original article)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)
* https://github.com/humanlayer/12-factor-agents
* https://github.com/ai-that-works/ai-that-works/tree/main/2025-08-05-advanced-context-engineering-for-coding-agents
## Related
* [Effective harnesses for long-running agents (Anthropic Engineering Blog)](Effective%20harnesses%20for%20long-running%20agents%20(Anthropic%20Engineering%20Blog).md)