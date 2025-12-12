---
created:
  - 2025-11-27T09:42
modified: 2025-11-28 12:02
tags:
type:
  - map-of-content
status:
  - in-progress
---
It's worth remembering [Conway's Law](https://en.wikipedia.org/wiki/Conway%27s_law):

```
[O]rganizations which design systems (in the broad sense used here) are constrained to produce designs which are copies of the communication structures of these organizations.

— Melvin E. Conway, How Do Committees Invent?
```

i.e. the systems we design end up having the same structure as our organization's communication structure.

I identified architecture styles giving a few variations of this prompt to a few different Large Language Models:  

```
What are the main philosophies governing how I should lay out my enterprise codebase? e.g. MVC, vertical slice etc. give me pros and cons of each approach
```

Below are the high-level concepts/architectures which I've identified:
Note also that:
1. These philosophies/approaches can be combined within the same codebase
2. A codebase can evolve from one approach to another as the project grows and it's requirements change.

| Architecture                                    | Description                 |
| ----------------------------------------------- | --------------------------- |
| [Layered](Layered%20Software%20Architecture.md) |                             |
| Model View Controller (MVC)                     |                             |
| Vertical Slice                                  |                             |
| Domain Driven Design (bounded contexts)         |                             |
| Hexagonal (ports and adapters)                  |                             |
| Onion                                           | might be same as hexagonal? |
| Microservices                                   |                             |
| modular monolith                                |                             |
| clean architecture                              |                             |

- Clean
- Command Query Responsibility Segregation (CQRS)
- Event-driven
- Service-Oriented
- Modular monolith
- Ports and adapters (hexagonal)
- n-tier
- layered
- MVC
- vertical slice
- domain-driven design
- onion
- microservices

## References

* Links to references (source material) go here
## Related

* Links to other notes which are directly related go here