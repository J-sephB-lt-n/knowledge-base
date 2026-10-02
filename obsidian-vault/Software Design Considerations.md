---
created:
  - 2026-09-29T14:52
modified: 2026-10-02 11:05
tags:
  - software
  - software-development
  - software-engineering
  - architecture
  - software-architecture
  - architecture-pattern
type:
  - note
status:
  - ongoing
---
| Principle                                                                  | Motivation                                                                                                                                   | How to Implement                                                                                                  | Source                       |
| -------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | ---------------------------- |
| Modules should be decoupled                                                | Decoupled code is easier to change                                                                                                           | Minimise shared dependencies between modules                                                                      | Pragmatic Programmer 2nd ed. |
| Log messages should be structured                                          | This allows them to be efficiently filtered/search programmatically                                                                          | JSON logs in a chosen standard format                                                                             |                              |
| Log messages should contain all of the 5 Ws: "Who, What, When, Where, Why" | This gives sufficient context to work out precisely what actually happened and why                                                           |                                                                                                                   |                              |
| Log messages should be correlated                                          | Gives visibility into the sequence of events leading to the failure                                                                          | - Add a globally unique shared ID to all logs corresponding to the same request/pipeline-run/experiment/user/etc. |                              |
| No piece of information should have more than one source of truth          | Any piece of data/information/knowledge stored in more than 1 place WILL diverge.<br>This applies to data, config, documentation, everything |                                                                                                                   | Joe                          |
|                                                                            |                                                                                                                                              |                                                                                                                   |                              |
|                                                                            |                                                                                                                                              |                                                                                                                   |                              |

## References
* Links to references (source material) go here
## Related
* Links to other notes which are directly related go here