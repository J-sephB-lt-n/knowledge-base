---
created:
  - 2026-04-15T20:48
modified: 2026-04-16 06:13
tags:
  - llm
  - chatbot
  - chat-gpt
  - strategy
  - business-strategy
  - bias
  - llm-bias
type:
  - note
status:
  - completed
---
This is an article from 2026-03-16 published by Harvard Business Review (HBR).
Across a large number of experiments using frontier models, the findings of the article are:
- It's uniformly a bad idea to ask LLMs for advice on business strategy
- LLMs reliably recommend the same business strategy regardless of your business context (they ignore your context and always give the same recommendation). They are strongly biased towards trendy business strategy approaches and buzzwords which dominate their training data. The researchers dub this "trendslop"
  e.g. *"strategies to “collaborate” and to seek “long-term sustainability” will surface again and again as recommendations, not because the specific business problem demands them, but because these terms align with contemporary business culture."*
- Better prompting and more quality context helps, but not very much.
- Allowing models to answer without requiring them to make a binary choice often resulted in the "hybrid trap", where the model recommends both. *"On the surface, this sounds sophisticated and balanced. In practice, it often reflects strategic confusion and high likelihood of failure."*

The article says that these findings do not mean that LLMs are useless for strategic advice, and provides the following recommendations:
- Use LLMs to expand/discover/explore options and tradeoffs, but not to make decisions.
- Actively counteract known biases e.g. use 2 independent prompts to get the LLM to individually defend each position, and then make the final choice yourself.
- Actively counteract potential biases: *"Before prompting the LLM to provide strategic advice, ask it to first surface concrete examples such as companies that succeeded or failed using each of the strategic options. Then think on your own how this would apply to your specific situation."*
- Remain alert to changing biases - new models mean potentially new biases.
- Beware the "hybrid trap". Hedging rather than committing to a binary decision is in itself a strategy which must be critically evaluated.
- Don't rely on context alone - this is not enough to negate the LLMs biases.
- Don't lose your edge - you are responsible for the strategic decision.
## References
* [Links to references (source material) go here](https://hbr.org/2026/03/researchers-asked-llms-for-strategic-advice-they-got-trendslop-in-return)
## Related
* Links to other notes which are directly related go here