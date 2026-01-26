---
created:
  - 2026-01-24T23:05
modified: 2026-01-26 17:02
tags:
type:
  - note
status:
  - in-progress
---
I was a skeptic for a very long time, but it's become clear to me that I need to embrace AI-generated coding and become an expert in it (while not losing the ability to think for myself).

I've been very convinced this month by these 3 approaches to AI coding:
1. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
2. [# Getting AI to Work in Complex Codebases (Dexter Horthy)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)
3. 

Facts I consider to be true:
(be careful if changing numbers here as these numbers are referenced later in this document)

|     | Fact                                                                                                                                                       | My confidence | Source                                                                                                   | Implication for coding agents                                                                                                                                                                                                                                                                                                                                                                     |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | AI content is drowning in hype and marketing but there is real value for code generation (and learning)                                                    | HIGH          | My own experience                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                   |
| 2   | If I delegate all knowledge to LLMs then my own skills will stagnate                                                                                       | HIGH          | My own experience                                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                   |
| 3   | All LLMs have a knowledge cutoff                                                                                                                           | HIGH          | Fundamental of the model architecture                                                                    |                                                                                                                                                                                                                                                                                                                                                                                                   |
| 4   | All LLMs base (pretraining) training data is primarily the public internet<br>(Anthropic also trained on millions of books, mostly pirated)                | MEDIUM        | - Common knowledge (e.g. common crawl)<br>- The big 2025 Anthropic law suit about pirated books          | - LLMs perform best at things that are commonly documented (e.g python vs zig). They are bad at niche tasks.<br>- LLMs inherit bad habits (e.g. python bare try/except). Can mitigate with prompting (e.g. AGENTS.md)<br>- Magic words like "vertical slice architecture" or "Test-Driven Development" or "John Ousterhout" convey a lot of context to a LLM (drastically change their behaviour) |
| 5   | Coding AI agent products (e.g. Claude Code, Cursor, OpenAI codex) wrap the LLMs in a lot of their own custom prompting/tools/wrappers/ecosystem            | HIGH          |                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                   |
| 6   | All LLMs are auto-regressive next token predictors                                                                                                         | HIGH          |                                                                                                          | Ordering of information in the context window matters                                                                                                                                                                                                                                                                                                                                             |
| 7   | MCP, skills, subagents, background agents may or may not be useful                                                                                         |               |                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                   |
| 8   | AI providers are running at a loss trying to capture market share                                                                                          | MEDIUM        |                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                   |
| 9   | LLMs hallucinate and are convincing liars<br>(this is what they are trained to do)                                                                         | HIGH          | - Common knowledge<br>- My own experience                                                                |                                                                                                                                                                                                                                                                                                                                                                                                   |
| 10  | Generating reasoning traces improves performance on complex tasks                                                                                          | HIGH          | Documented in many studies                                                                               | Choose reasoning ("thinking") models for more complex coding tasks                                                                                                                                                                                                                                                                                                                                |
| 11  | Coding agents don't do long-term planning or architecture thinking                                                                                         |               |                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                   |
| 12  | LLM are very good at using tools<br>(I'm sure they are fine-tuned for this)                                                                                | HIGH          | - My own experience                                                                                      | Give agents tools to use                                                                                                                                                                                                                                                                                                                                                                          |
| 13  | A small number of good agent tools is better than many rubbish tools                                                                                       | HIGH          | - My own experience<br>- This was the original concept behind Claude Code (i.e. bash vs custom indexing) | It is worth investing a lot of time in iterating on a single agent tool                                                                                                                                                                                                                                                                                                                           |
| 14  | More specific and unambiguous prompts work result in better code                                                                                           | HIGH          |                                                                                                          | - Work with a  template/framework which elicits good requirements (e.g. FURPS+)<br>- Use a chatbot to help refine prompts to make them more precise                                                                                                                                                                                                                                               |
| 15  | More relevant context leads to better code                                                                                                                 | HIGH          | - Common knowledge<br>- My own experience                                                                | Need to find an efficient way to manage context                                                                                                                                                                                                                                                                                                                                                   |
| 16  | LLMs' broad pretraining makes them great for discussing/exploring different possible approaches to a problem                                               | HIGH          | My own experience                                                                                        | Have an explicit agent which involves brainstorming different possible approaches                                                                                                                                                                                                                                                                                                                 |
| 17  | Structured reasoning (e.g. step-by-step reasoning, plan then execute, explain decisions, decompose into subproblems) improves performance on complex tasks | MEDIUM        |                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                   |
| 18  | Different LLMs need different prompting approaches                                                                                                         | LOW           | - Picked this up online                                                                                  |                                                                                                                                                                                                                                                                                                                                                                                                   |
| 19  | Coding agents do better on small (tightly scoped) tasks than on large (loosely defined) ones                                                               | MEDIUM        |                                                                                                          | Break up big tasks into smaller tightly scoped ones                                                                                                                                                                                                                                                                                                                                               |
| 20  | Iterative refinement works better than one-shot prompting                                                                                                  |               |                                                                                                          | - code review and QA (testing) agents<br>                                                                                                                                                                                                                                                                                                                                                         |
| 21  | Coding agents write code FAST.<br>Keeping the codebase under control is one of the biggest challenges.                                                     | HIGH          | - My own experience                                                                                      |                                                                                                                                                                                                                                                                                                                                                                                                   |
| 22  | Agents benefit from a clean environment                                                                                                                    | MEDIUM        | - My own experience                                                                                      | - If things are consistent in the codebase, then the agent can maintain that consistency (or be instructed to). i.e. make style, language, environment and architecture patterns explicit.<br>- The agent shouldn't need to waste tokens working out how to run the app/tests etc. correctly.                                                                                                     |
|     |                                                                                                                                                            |               |                                                                                                          |                                                                                                                                                                                                                                                                                                                                                                                                   |


My proposed coding agent workflow:
(all steps are optional)

|     | Step                                                                                                                                              | What it Does                                                                                                                                                                                                                                                                                         | Facts |
| --- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
|     | **/discuss_potential_approaches**<br>(standalone task that can be run at any time, maybe just in ChatGPT web)                                     |                                                                                                                                                                                                                                                                                                      |       |
|     | **/discuss_codebase_architecture**<br>(greenfield codebase: design then scaffold)<br>(brownfield: describe then document)                         | 1.                                                                                                                                                                                                                                                                                                   |       |
| 1   | **/discuss_prd**<br>(for greenfield coding task)<br>Create Product Requirements Document through a guided chat with a chatbot                     |                                                                                                                                                                                                                                                                                                      |       |
| 1   | **/discuss_requirements**<br>(brownfield or small coding task)<br>Define requirements using a template/framework through guided chat with chatbot | 1. Asks me which of a preset list of requirements elicitation frameworks should be included<br>2. Asks me to describe the problem I'm trying to solve.<br>3. Runs me through each elicitation framework.<br>4. Organises the requirements gathered into a document and asks where it should save it. |       |
|     | **/gather_context**                                                                                                                               | 1. Asks me what we're gathering context on.<br>2. Uses a research subagent to find all potentially relevant files.<br>3. Asks me which of the discovered files it should read.                                                                                                                       |       |
|     |                                                                                                                                                   |                                                                                                                                                                                                                                                                                                      |       |
|     | Add observed repeat bad agent behaviour to AGENTS.md                                                                                              |                                                                                                                                                                                                                                                                                                      |       |






**Accepted practice:**
- Prompt for:
  - Input validation
  - Resource cleanup
  - Thread/process safety
  - Secure defaults (e.g., prepared statements, CSRF handling)

**Commonly accepted as true:**
- If you don’t explicitly ask for security and robustness, the agent often optimizes for “simple, illustrative code.”
- Security, error handling, and resilience improve when explicitly requested (or when your prompt includes internal security guidelines).

---

## 9. Use “review mode” and self-critique

**Accepted practice:**
- After getting code, ask the agent to:
  - Review it as if it were written by someone else
  - Identify possible bugs, edge cases, and performance issues
  - Suggest improvements without rewriting everything unnecessarily

**Commonly accepted as true:**
- Self-review prompts (or “critic then fix” loops) materially improve quality.
- Having the agent explain *why* the code is correct often surfaces hidden mistakes.

---

## 10. Ground the agent on real tools and feedback

**Accepted practice:**
- Combine AI with:
  - Compiler/interpreter errors
  - Static analysis (mypy, ESLint, flake8, SonarQube)
  - Test results
- Paste outputs back into the conversation and ask for fixes.

**Commonly accepted as true:**
- The best reliability comes from AI + automated tools + human review.
- When given real tool feedback, agents are much better at converging to correct, idiomatic solutions.

---

## 11. Use system / “role” instructions to set global behavior

**Accepted practice:**
- Establish up front:
  - “You are a senior backend engineer in Python.”
  - “Prioritize readability over micro-optimizations.”
  - “Never use network access; assume offline operation.”

**Commonly accepted as true:**
- Clear role + priorities at the start of the session improves consistency across many turns.
- It reduces the need to restate preferences in every prompt.

---

## 12. No prompt guarantees perfection; human review remains essential

**Accepted practice:**
- Always:
  - Review logic manually for important code
  - Run and extend tests
  - Inspect edge cases that weren’t considered
- Treat AI drafts as high-quality scaffolding, not final truth.

**Commonly accepted as true:**
- Even with excellent prompting, AI can:
  - Misinterpret ambiguous requirements
  - Produce subtly wrong logic
  - Use APIs incorrectly in edge cases
- “Guaranteed robust high-quality code” isn’t achievable solely via prompting; it requires verification.

---

If you want, I can turn these into a concrete “prompt template” you can reuse when asking coding agents for non-trivial features or refactors.


# Claude 4.5 Opus

# Commonly Accepted Facts About Prompting AI Coding Agents (as of 2025)

I should note that I can only speak to what's established through my knowledge cutoff in early 2025, not 2026. Here's what has become generally accepted:

## Widely Accepted Principles

**1. Specificity beats vagueness**
- Explicit constraints (language version, frameworks, error handling requirements) produce more reliable output than open-ended requests

**2. Examples work**
- Providing input/output examples or code style samples significantly improves consistency

**3. Decomposition helps**
- Breaking complex tasks into smaller, sequential prompts yields better results than single monolithic requests

**4. Context windows matter but aren't magic**
- More context helps, but relevant context beats large dumps of irrelevant code

**5. Verification is non-negotiable**
- No prompting technique *guarantees* robust, high-quality code—human review and testing remain essential

## What's Still Contested or Unclear

- Whether "chain of thought" prompting reliably improves code correctness
- Optimal prompt structure (there's no universal template that dominates)
- Whether persona prompts ("you are a senior engineer...") have real effects or are placebo

## Important Caveat

The phrase **"guaranteed robust high quality code"** remains aspirational, not achievable through prompting alone. The 2025 consensus is that prompting improves *probability* of good output, but testing, review, and iteration remain mandatory.

Would you like me to elaborate on any specific technique?

## References
* [Effective harnesses for long-running agents (Anthropic engineering blog)](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
## Related
* [No Vibes Allowed - Solving Hard Problems in Complex Codebases Dex Horthy HumanLayer (presentation at AI Engineer 2025)](No%20Vibes%20Allowed%20-%20Solving%20Hard%20Problems%20in%20Complex%20Codebases%20Dex%20Horthy%20HumanLayer%20(presentation%20at%20AI%20Engineer%202025).md)