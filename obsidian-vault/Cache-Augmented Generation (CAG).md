---
created:
  - 2025-03-24T20:28
modified: 2025-03-31 22:27
tags:
  - rag
  - package-management
  - llm
  - large-language-model
  - retrieval
  - retrieval-augmented-generation
  - information-retrieval
  - gpt
type:
  - note
status:
  - in-progress
---
As an alternative to [Retrieval-Augmented Generation (RAG)](Retrieval-Augmented%20Generation%20(RAG).md), [Cache-Augmented Generation (CAG)](Cache-Augmented%20Generation%20(CAG).md) involves preloading the entire knowledge base into the large language model's context window (this can be done once and then stored in a *KV cache* for reuse). 

Here are some comparison points between RAG and CAG:

| Situation                                    | Preference                          |
| -------------------------------------------- | ----------------------------------- |
| Inference speed is critical                  | CAG is faster (after initial cache) |
| Dynamic knowledge base (changes frequently)  | RAG is better                       |
| Knowledge base doesn't fit in context window | Have to use RAG                     |
| Accuracy is critical                         | RAG is better                       |
| Simpler architecture/code                    | CAG is better                       |

A novel idea: CAG and RAG can even be combined e.g. RAG performs an initial fetch of relevant data (e.g. full medical history for a specific patient), and then all of this information can be cached into the context window and repeatedly queried. 
## References
* [(youtube) RAG vs. CAG: Solving Knowledge Gaps in AI Models](https://www.youtube.com/watch?v=HdafI0t3sEY)
* [A Deep Dive into Cache Augmented Generation](https://adasci.org/a-deep-dive-into-cache-augmented-generation-cag/)
## Related
* [Information Retrieval (Search) Strategies](Information%20Retrieval%20(Search)%20Strategies.md)
* [Retrieval-Augmented Generation (RAG)](Retrieval-Augmented%20Generation%20(RAG).md)
* [Searching for Best Practices in Retrieval-Augmented Generation (paper)](Searching%20for%20Best%20Practices%20in%20Retrieval-Augmented%20Generation%20(paper).md)