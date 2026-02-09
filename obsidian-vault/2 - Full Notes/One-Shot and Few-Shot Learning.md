---
created:
  - 2024-06-26T21:07
modified: 2024-06-26 22:14
tags:
  - few-shot-learning
  - machine-learning
  - one-shot-learning
type:
  - note
status:
  - completed
---
One-shot learning means training a model on a single labelled (or completed) example before expecting the model to generalise (i.e. to produce output/predictions).

In the context of Large Language Models (LLMs), an example of one-shot-learning (or *one-shot-prompting*) would be providing a single completed example within the prompt before giving the model it's instruction. Here is an example a *one-shot-learning* prompt:
```
Complete the sentence: "The machines will take over "
Response: "The machines will take over many routine and repetitive tasks, allowing humans to focus on more creative, strategic, and complex problem-solving activities."
Complete the sentence: "Humans are "
Response: 
```

Similarly, few-shot learning means provides the model with a small number of labelled/completed examples. Here is an example of a *few-shot-learning* prompt:
```
Review="This film ruined my day" -> Classification="Negative"
Review="This was heart-warming" -> Classification="Positive"
Review="Like watching paint dry" -> Classification="Negative"
Review="Best thing ever" -> Classification="Positive"
Review="I'd rather wash the dishes than watch this" -> Classification=?
```

For more complex reasoning tasks, [[LLM Chain-of-Thought Prompting]] is probably a more effective approach.

## Related
* [[Applied Large Language Model Concepts]]
* [[LLM Chain-of-Thought Prompting]]
- [ChatGPT Prompt Engineering for Developers (DeepLearning.AI course)](<2%20-%20Full%20Notes/ChatGPT%20Prompt%20Engineering%20for%20Developers%20%28DeepLearning.AI%20course%29.md>)
- [LLM Chain-of-Thought Prompting](<2%20-%20Full%20Notes/LLM%20Chain-of-Thought%20Prompting.md>)
- [Applied Large Language Model Concepts](<4%20-%20Maps%20of%20Content/Applied%20Large%20Language%20Model%20Concepts.md>)
