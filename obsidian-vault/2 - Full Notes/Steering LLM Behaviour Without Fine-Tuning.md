---
created:
  - 2026-02-13T22:46
modified: 2026-02-14 23:09
tags:
  - llm
  - large-language-model
  - software-engineering
  - huggingface
  - transductive-learning
  - behaviour
  - fine-tuning
  - prompt
  - prompting
  - prompt-engineering
  - steer
  - steering
type:
  - note
status:
  - in-progress
---
I learned this concept from [this HuggingFace youtube video](https://www.youtube.com/watch?v=F2jd5WuT-zg) 

TLDR: 
- There are various ways to identify which model parameters are activated by a certain topic (looking at a specific model layer). You can then take this vector you've found (which in some sense is representative of this chosen topic), and simply add some chosen multiple of this vector at that layer at inference time.
- This results in the model being steered toward that topic, regardless of the actual model prompt. The amount of steering is completely controllable, although steering very hard breaks the model completely.
- In the youtube video, the model is steered toward (and at strong steering identifies as) the Eiffel tower.
- This obviously requires direct access to the model weights at internal model layers (i.e. not possible with Claude, OpenAI GPTs, Gemini etc.)
## References
- https://www.youtube.com/watch?v=F2jd5WuT-zg
## Related
* Links to other notes which are directly related go here