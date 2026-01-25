---
created:
  - 2026-01-19T13:20
modified: 2026-01-19 16:07
tags:
  - ai
  - llm
  - llm-agents
  - coding-agent
  - dev
  - ai-dev
  - cursor
  - claude-code
  - agentic
  - large-language-model
  - personal-development
type:
  - note
status:
  - ongoing
---
Workflow I'm thinking (using coding agent slash commands):
Some of these steps can be omitted depending on the coding task size 
1. `/init_task_context`
   Scaffold a context location (e.g. create a local `current_task/` folder with a `README.md` and a `agent_notes.md` file).
2. `/discuss_requirements`
   Read what is already in `current_task/README.md` for context
   Discuss what I want (elicit my requirements) and write them to `current_task/prd.md`
   Document in `current_task/README.md` what `current_task/prd.md` is
3. `/research`
   Read `current_task/README.md` and `current_task/agent_notes.md` for context
   Steal dex horthy's prompt
   Use subagents
   Add  research assets to `current_task/resources/docName.md` and document this in `current_task/README.md`
   Can add more detailed notes to `agent_notes.md`
4. `/plan_current_task`
   Read `current_task/README.md` and `current_task/agent_notes.md` for context
   Steal dex horthy's prompt
   Use subagents
5. `/discuss_potential_approaches`
   Give some different ideas for how I might solve the current task (or a piece of it), listing pros and cons of each approach.
6. `/code_next_feature`
    Read `current_task/README.md` and `current_task/agent_notes.md` for context
   Steal dex horthy's prompt
7. `/review_feature`

Add a `agent_dev_helper` bash alias explaining all of these slash commands.
## References
* Links to references (source material) go here
## Related
* [No Vibes Allowed - Solving Hard Problems in Complex Codebases Dex Horthy HumanLayer (presentation at AI Engineer 2025)](No%20Vibes%20Allowed%20-%20Solving%20Hard%20Problems%20in%20Complex%20Codebases%20Dex%20Horthy%20HumanLayer%20(presentation%20at%20AI%20Engineer%202025).md)
* [Effective harnesses for long-running agents (Anthropic Engineering Blog)](Effective%20harnesses%20for%20long-running%20agents%20(Anthropic%20Engineering%20Blog).md)
* [Dex Horthy's Research Codebase Prompt](Dex%20Horthy's%20Research%20Codebase%20Prompt.md)
* [Dex Horthy's Create Plan Prompt](Dex%20Horthy's%20Create%20Plan%20Prompt.md)
* 