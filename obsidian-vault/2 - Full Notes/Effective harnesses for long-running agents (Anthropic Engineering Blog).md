---
created:
  - 2025-12-12T12:32
modified: 2025-12-12 13:33
tags:
  - ai
  - ai-dev
  - code
  - coding
  - coding-agent
  - context
  - context-window
  - long-running-agents
  - anthropic
  - claude
  - claude-code
  - llm
  - llm-agents
  - agent
  - agentic
  - agent-memory
  - ai-coding
  - ai-development
  - software-development
  - dev
type:
  - note
status:
  - completed
---
This blog post describes a specific approach to coding agents which work on software projects much larger than their context window. 

The core approach is as follows:
1. Define a framework/workflow within which the coding agents must work. The environment (assets) for this are set up once at the beginning by an *initializer* agent. 
   An example of this initial environment might be:
	- Makes the project into a git repo.
	- An `init.sh` script which starts up the app.
	- A `agent-progress.txt` file keeping a concise log of notable development events/insights. 
	- A `feature_list.json` file enumerating the required application features, as well as the status of each.
2. Over and over again, a fresh *coding* agent (i.e. an agent with an empty context window) works on the codebase. The idea is that every new agent makes marginal incremental progress towards the defined end goal(s) without stuffing up the existing code, and that the coding agents update defined assets (like docs) where they record their progress (that the next fresh agent can then review to get up to speed).
3. Every *coding* agent follows a defined workflow something like this:
	- Run `pwd` to see the directory you're working in. You may only edit files in this directory.
	- Read the git logs and progress files (e.g. `agent-progress.txt`) to get up to speed on what was recently worked on.
	- Read the features list (e.g. `feature_list.json`) and choose the highest-priority feature that’s not yet done to work on.
	- Run the `init.sh` and try using the app a bit (to see if the app is broken). If there's a bug then fix it rather than working on a new feature.
	- Writes code and commits changes to git
	- Records it's work in the `feature_list.json` and `agent-progress.txt` file 

| Observed Problem                                          | Initializer Agent                                                                                   | Coding Agent                                                                                                                                                                            |
| --------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Coding agent prematurely considers the task completed     | Creates a `feature_list.json`  listing all required app features (correct feature/task granularity) | - Reads the feature list at session start.<br>- Only works on 1 feature.                                                                                                                |
| Coding agent leaves the code in a broken state            | - Sets up project as a git repo<br>- Creates progress notes file                                    | - Reads git logs and progress notes file at session start<br>- Tests the app before starting to write code<br>- Ends its sessionwith a git commits and write to the progress notes file |
| Coding agent considers features done prematurely          | Creates the `feature_list.json` file.                                                               | Agent self-verifies all features - only mark as passing after careful testing.                                                                                                          |
| Coding agent wastes tokens working out how to run the app | Create an `init.sh` script which launches the app                                                   | Run `init.sh` at the start of the session to start the app.                                                                                                                             |

## References
* https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
* [Claude 4 Prompting Guide](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-4-best-practices#multi-context-window-workflows)
## Related
* [No Vibes Allowed - Solving Hard Problems in Complex Codebases Dex Horthy HumanLayer (presentation at AI Engineer 2025)](No%20Vibes%20Allowed%20-%20Solving%20Hard%20Problems%20in%20Complex%20Codebases%20Dex%20Horthy%20HumanLayer%20(presentation%20at%20AI%20Engineer%202025).md)
* [Approaches to LLM app development](Approaches%20to%20LLM%20app%20development.md)
* [Thoughts on LLM Application Development](Thoughts%20on%20LLM%20Application%20Development.md)