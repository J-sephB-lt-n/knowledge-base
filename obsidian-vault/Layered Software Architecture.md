---
created:
  - 2025-11-27T12:58
modified: 2026-04-29 10:41
tags:
  - software-architecture
  - architecture
  - architecture-pattern
  - architecture-style
  - software
  - software-engineering
type:
  - note
status:
  - in-progress
---
## TLDR

- The app is organised as a stack of layers
- In strict layered architecture, a layer can only use the layer directly below it
- Variants include cross-cutting concerns (functionality shared by different layers) or lower layers communicating with higher layers via callbacks (initiated by the higher layer).
## Pros
- Modifiability, Portability, Reusability - since only neighbouring layers are connected, it is easy to swap or emulate all of the other disconnected layers (source: [Just Enough Software Architecture - A Risk-Driven Approach](Just%20Enough%20Software%20Architecture%20-%20A%20Risk-Driven%20Approach.md) )
## Cons

- Performance - all communication must travel sequentially through the layers (source: [Just Enough Software Architecture - A Risk-Driven Approach](Just%20Enough%20Software%20Architecture%20-%20A%20Risk-Driven%20Approach.md) )

## Good Use-Cases

## Bad Use-Cases


## References
* https://dev.to/yasmine_ddec94f4d4/understanding-the-layered-architecture-pattern-a-comprehensive-guide-1e2j
## Related
* [Software Application Architectures](Software%20Application%20Architectures.md)