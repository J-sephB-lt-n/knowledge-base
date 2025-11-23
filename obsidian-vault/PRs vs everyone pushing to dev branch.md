---
created:
  - 2025-11-18T08:55
modified: 2025-11-20 11:35
tags:
  - git
  - github
  - PR
  - pull-request
  - dev
  - software
  - software-development
  - product-development
  - team
type:
  - note
status:
  - completed
---
Currently the team has only 2 branches: 
- `main`
- `dev`
And all of the developers in the team just push directly to `dev` (at the same time).
I want to propose rather doing a Pull Request (PR)-based system where each dev branches off of `dev` into a feature branch, and then merges their finished feature into `dev` via a PR.

Pros and Cons of each Approach:

| Everyone pushes straight to `dev`                                                   |                                                                                                    | Everyone PRs into `dev`                                                                     |                                                                                                                                         |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| **PROS**                                                                            | **CONS**                                                                                           | **PROS**                                                                                    | **CONS**                                                                                                                                |
| Simple mental model                                                                 | Single push can break everyone's codebase at the same time                                         | Better isolation of work                                                                    | Long-lived feature branches can make merge conflicts more painful (onus on the developer to integrate  `dev` into their feature branch) |
| Everyone sees all changes instantly<br>(integration issues are visible immediately) | Harder to track new features                                                                       | Cleaner history and traceability                                                            | Can become bureaucratic if CI rules are too strict                                                                                      |
|                                                                                     | Harder to perform rollbacks if something goes wrong                                                | Retains better feature context (linked tickets, feature description, comments, code review) |                                                                                                                                         |
|                                                                                     | Harder to enforce coding standards centrally (e.g. tests, linting).<br>Harder to run automatic CI. | Can run automatic CI on merge into `dev` (e.g. linting, test suite)                         |                                                                                                                                         |
|                                                                                     | Not possible to do formal code review (and no PR description or discussion trail)                  | Easier feature rollbacks                                                                    |                                                                                                                                         |
|                                                                                     | Unexpected pattern (software industry antipattern)                                                 | This is an established pattern in the industry (it is expected)                             |                                                                                                                                         |
|                                                                                     |                                                                                                    | Merge conflicts with `dev` branch are visible in the PR prior to merge                      |                                                                                                                                         |
## References
* Links to references (source material) go here
## Related
* Links to other notes which are directly related go here