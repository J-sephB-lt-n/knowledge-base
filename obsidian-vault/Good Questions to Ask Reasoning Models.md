---
created:
  - 2025-09-30T22:10
modified: 2025-09-30 22:14
tags:
  - reasoning
  - llm
  - large-language-model
  - deepseek
  - o1
  - think
  - thinking
  - agent
type:
  - note
status:
  - ongoing
---

```
given the function type signature

foo : Int -> [Int] -> [Int] -> [Int]

and example outputs

- foo 2 [1,0,1] [] == [0,1]
- foo 1 [1,0] [] == [1]
- foo 0 [1,0] [] == []
- foo 3 [0,1,1,0,1] [] == [1,1,0]

Explain what the function is doing.
```
Answer: `foo n [list] [discard] -> [first n items in list, in reverse order]`
Source: https://www.reddit.com/r/LocalLLaMA/comments/1i9mhlx/what_questions_have_you_asked_reasoning_models_to/
## References
* Links to references (source material) go here
## Related
* Links to other notes which are directly related go here