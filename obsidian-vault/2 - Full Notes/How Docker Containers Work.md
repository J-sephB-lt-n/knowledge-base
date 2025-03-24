---
created:
  - 2024-10-26T23:11
modified: 2024-10-28 22:39
tags:
  - docker
  - container
  - image
  - containerisation
  - vm
  - virtual-machine
  - hypervisor
  - os
  - package-management
  - build
  - deploy
  - virtualisation
  - virtualization
type:
  - note
status:
  - completed
---
**Virtualisation** means a single machine partitioning it's resources to simulate there being multiple independent machines (this is what GCP VMs and AWS EC2s are).
Each partition (VM) has it's own OS.

| Level |    VM 1     |        VM 2        |    VM 3     |
| ----- | :---------: | :----------------: | :---------: |
| VM    | Application |    Application     | Application |
| VM    |  Libraries  |     Libraries      |  Libraries  |
| VM    |  Guest OS   |      Guest OS      |  Guest OS   |
| Host  |     --      |     HYPERVISOR     |     --      |
| Host  |     --      | Host Hardware & OS |     --      |

**Containerisation** (e.g. Docker) isolates everything except the OS i.e. containers run strictly on the same OS as the host machine. Therefore, linux containers can only run on linux, and windows containers can only run on windows.

| Level |    VM 1     |        VM 2        |    VM 3     |
| ----- | :---------: | :----------------: | :---------: |
| VM    | Application |    Application     | Application |
| VM    |  Libraries  |     Libraries      |  Libraries  |
| Host  |     --      |  Container Engine  |     --      |
| Host  |     --      | Host Hardware & OS |     --      |
## References
* https://www.freecodecamp.org/news/how-docker-containers-work/
## Related
* Links to other notes which are directly related go here