---
created:
  - 2025-12-22T11:53
modified: 2025-12-30 22:33
tags:
  - agent
  - agentic
  - cursor
  - coding-agent
  - ai-coding
type:
  - note
status:
  - ongoing
---
In general, adding these to the cursor coding agent allowlist enables the agent to act completely autonomously:

| Risk      | Command |                                                                   Notes |
| --------- | ------: | ----------------------------------------------------------------------: |
| 🟢 Low    |     cat |                                                                         |
| 🟡 Medium |      cd | Context change can be dangerous (e.g. move working directory to /home/) |
| 🟡 Medium |    echo |                    With redirection (>), can be used to overwrite files |
| 🔴 High   |     git |                             Can overwrite history (even on remote repo) |
| 🟢 Low    |    grep |                                                                         |
| 🟢 Low    |    head |                                                                         |
| 🟢 Low    |      ls |                                                                         |
| 🟢 Low    |    tail |                                                                         |
| 🔴 High   |      uv |                Allows arbitrary package installation and code execution |
| 🟢 Low    |      wc |                                                                         |

I have a safer and more fine-grained version available here:  
## References
* Links to references (source material) go here
## Related
* Links to other notes which are directly related go here