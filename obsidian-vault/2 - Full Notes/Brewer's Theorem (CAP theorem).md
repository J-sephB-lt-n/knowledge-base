---
created:
  - 2024-08-17T20:25
modified: 2024-08-17 20:30
tags:
  - distributed
  - data
  - database
  - system-design
  - architecture
type:
  - note
status:
  - completed
---
Brewer's (or _CAP_) theorem states that a distributed data store can provide at most 2 of the following 3 guarantees:

| Guarantee           | Definition                                                                                                                      |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| Consistency         | Clients see the same data at the same time, no matter which node they connect to                                                |
| Availability        | A data request always receives a response, even if some nodes are failing i.e. all working nodes always return a valid response |
| Partition Tolerance | The system continues to work despite communication failures between the nodes                                                   |
