---
created:
  - 2024-09-11T09:15
modified: 2024-09-12 21:21
tags:
  - llm
  - nlp
  - gpt
  - prompt
  - prompting
  - large-language-model
  - ai
  - genAI
  - generative
  - ml
  - machine-learning
type:
  - map-of-content
status:
  - ongoing
---

| Prompting Technique    | Explanation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Link(s)                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- |
| Reverse Interviewing   | Prompting the LLM to ask us questions. This helps unlock our human creativity.                                                                                                                                                                                                                                                                                                                                                                                                                                     | https://openai.com/chatgpt/use-cases/writing-with-ai/                                        |
| LLM Prompt Review      | Instead of simply doing what you have told it to do, ask the LLM to comment on the quality/ambiguity of the task (prompt) that it has been given.<br>Possibly, ask the LLM to rewrite the required task (prompt) more clearly and unambiguously.<br>If the model gets a task wrong, ask it to explain why it got it wrong, and ask it to improve the prompt so that this mistake can be avoided in future.                                                                                                         | [Anthropic: AI prompt engineering: A deep dive](https://www.youtube.com/watch?v=T9aRN5JkmL8) |
| Iterate with the model | A multi-step back and forth conversation between the user and the model can lead to a much better final output.<br>You can ask the model why it made a particular decision.                                                                                                                                                                                                                                                                                                                                        |                                                                                              |
| Model Persona/Role     | Tell the LLM that they are a specific person or thing e.g. "You are a professional data analyst."<br>Note that this can sometimes degrade the quality of the model.                                                                                                                                                                                                                                                                                                                                                | [Anthropic: AI prompt engineering: A deep dive](https://www.youtube.com/watch?v=T9aRN5JkmL8) |
| Honesty                | Tell the model exactly what they are and what their context is e.g. "You are a large language model being used as a customer-facing chatbot on a banking website."                                                                                                                                                                                                                                                                                                                                                 | [Anthropic: AI prompt engineering: A deep dive](https://www.youtube.com/watch?v=T9aRN5JkmL8) |
| Treat it like a person | With a very large model, it's often worth prompting it as you would prompt an actual person to do a task.<br>Specifically, a very competent person (e.g. a consultant) with a lot of world knowledge, but no context about the problem that you want them to solve.                                                                                                                                                                                                                                                | [Anthropic: AI prompt engineering: A deep dive](https://www.youtube.com/watch?v=T9aRN5JkmL8) |
| Chain-of-Thought       | A prompting technique which involves trying to get the LLM to arrive at an answer via a _chain-of-thought_ i.e. a "_coherent series of intermediate reasoning steps that lead to the final answer_" (a step-by-step thought process).<br>The original paper proposed to achieve this by providing the model with a small number of examples before giving it its required task (i.e. include in its prompt a few example prompts+responses in which the answer was arrived at in a chain-of-thought fashion). <br> | https://arxiv.org/abs/2201.11903<br>                                                         |
| 1-shot and Few shot    | Including in the prompt one (or a small number) of examples of correctly solved tasks, prior to giving it its actual task.<br>This can be used to show the model the way that it should approach (or "think about") the task that it is required to solve.                                                                                                                                                                                                                                                         |                                                                                              |
## References
* [Anthropic: AI prompt engineering: A deep dive](https://www.youtube.com/watch?v=T9aRN5JkmL8)
* https://www.promptingguide.ai/
## Related
* [[Applied Large Language Model Concepts]]