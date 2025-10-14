---
created:
  - 2025-10-01T10:02
modified: 2025-10-01 10:24
tags:
  - structured
  - structured-output
  - structured-outputs
  - pydantic
  - schema
  - json
  - stable
  - robust
  - data
  - llm
  - large-language-model
  - agent
  - agentic
type:
  - note
status:
  - in-progress
---
Main body of note goes here

## BAML

https://github.com/BoundaryML/baml
https://boundaryml.com/blog/sota-function-calling

## Instructor

https://github.com/567-labs/instructor

## PydanticAI Structured Output

[pydantic-AI](https://github.com/pydantic/pydantic-ai) has 3 different available approaches: 
https://ai.pydantic.dev/output/

At the time of writing (September 2025), I see from intercepting the API calls to OpenAI that the langchain v1.0 `create_agent()` enforces structured output by including the desired output schema as an agent tool and forcing the agent to call a tool (which is the pydanticAI default too).
## References
* [(BAML) Beating OpenAI's structured outputs on cost, accuracy and speed — An interactive deep-dive](https://boundaryml.com/blog/sota-function-calling)
* https://github.com/567-labs/instructor
## Related
* Links to other notes which are directly related go here