---
created:
  - 2026-05-06T14:10
modified: 2026-05-07 09:10
tags:
  - llm
  - large-language-model
  - agent
  - agentic
  - pattern
  - ai
  - ai-agent
type:
  - note
status:
  - completed
---
Microsoft described these 2 new alternative agent patterns for deep research, which they added to their Microsoft 365 Copilot deep research agent in early 2026.

- **CRITIQUE PATTERN**: 2 separate agents on a deep research task - one explores and creates structured output and the other agent is dedicated to validation, improving presentation, source reliability assessment, completeness, evidence grounding etc. (in [the microsoft article](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-multi-model-intelligence-in-researcher/4506011) their screenshot of copilot shows them using openai for generation and claude for refinement)
- **COUNCIL PATTERN**: Multiple models research in parallel. Then the different results are presented to a judge agent, who summaries the agreements and discrepancies between the different research findings (in [the microsoft article](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-multi-model-intelligence-in-researcher/4506011) their screenshot of copilot shows them running 2 initial parallel research agents - openai and claude - in parallel)
## References
* https://techcommunity.microsoft.com/blog/microsoft365copilotblog/introducing-multi-model-intelligence-in-researcher/4506011
## Related
* Links to other notes which are directly related go here