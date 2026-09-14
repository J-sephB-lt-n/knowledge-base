---
created:
  - 2026-08-06T22:13
modified: 2026-08-19 08:44
tags:
  - agent
  - harness
  - agent-harness
  - agent-skills
  - skills
  - apm
  - agent-package-manager
type:
  - note
status:
  - in-progress
---
Expected location for project-scoped skills: 

```bash
# opencode #
project-name/
└── .opencode/           # also recognises .agents/ or .claude/
    └── skills/
	    └── skill-name/
	        ├── SKILL.md
	        └── ...      # (optional) other files/folders for SKILL.md to reference
	        
# cursor #
project-name/
└── .cursor/             # also recognises .agents/ or .claude/
    └── skills/
	    └── skill-name/
	        ├── SKILL.md
	        └── ...      # (optional) other files/folders for SKILL.md to reference

# claude code #
project-name/
└── .claude/             
    └── skills/
	    └── skill-name/
	        ├── SKILL.md
	        └── ...      # (optional) other files/folders for SKILL.md to reference
```

| frontmatter field        | claude   | cursor | opencode |
| ------------------------ | -------- | ------ | -------- |
| name                     | required |        | required |
| description              | optional |        | required |
| license                  | optional |        | optional |
| compatibility            | optional |        | optional |
| metadata                 | optional |        | optional |
| when_to_use              | optional |        | ignored  |
| argument-hint            | optional |        | ignored  |
| arguments                | optional |        | ignored  |
| disable-model-invocation | optional |        | ignored  |
| user-invocable           | optional |        | ignored  |
| allowed-tools            | optional |        | ignored  |
| disallowed-tools         | optional |        | ignored  |
| model                    | optional |        | ignored  |
| effort                   | optional |        | ignored  |
| context                  | optional |        | ignored  |
| agent                    | optional |        | ignored  |
| background               | optional |        | ignored  |
| hooks                    | optional |        | ignored  |
| paths                    | optional |        | ignored  |
| shell                    | optional |        | ignored  |
|                          |          |        |          |


## References
* https://code.claude.com/docs/en/skills
* https://agentskills.io/home
* https://opencode.ai/docs/skills/
* https://cursor.com/docs/skills
## Related

* Links to other notes which are directly related go here