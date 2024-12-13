---
created:
  - 2024-11-15T10:38
modified: 2024-11-15 11:49
tags:
  - llm
  - large-language-model
  - gpt
  - chat-gpt
  - chat-interface
  - nlp
  - natural-language-processing
  - prompt
  - prompting
  - prompt-engineering
type:
  - note
status:
  - completed
---
This is a simple prompt engineering approach I learned from [Gianluca Mauro](https://gianlucamauro.com/about).

The idea is to separate your prompt into [Context](#Context), [Instructions](#Instructions), [Details](#Details), [Input](#Input):
### Context
- Set the scene for the model - important background information framing the task.
- `Context` is designed to give the LLM a clear role and style.
- Example: “You are a copywriter at an ice cream company specialising in healthy ice creams, targeting affluent customers”
### Instructions
- `Instruction(s)` specify the task that you want the LLM to achieve
- Be assertive and crystal clear. The LLM doesn’t have feelings, so clarity trumps tact. 
- Example: “I am going to give you a message and you are going to write an instagram post containing this message”
### Details
- Think about what an ideal output would look like, and describe it here.
### Input 
- `Input` is information/data directly relevant to this specific request/task.
- `Input` differs from `context` in that `context` is the kind of information that may be reused with different `inputs`, whereas `input` is information specific to only this request/task.
- Example: “The message I want you to write an Instagram post about is 'we are releasing a new product called choco-early, which contains no dairy or cane sugar. The target audience for this post is middle-aged men.'”
## References
* Links to references (source material) go here
## Related
* [LLM Prompting Strategies](LLM%20Prompting%20Strategies.md)