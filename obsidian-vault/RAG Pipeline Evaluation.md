---
created:
  - 2024-11-07T21:32
modified: 2024-11-07 22:37
tags:
  - rag
  - retrieval-augmented-generation
  - llm
  - chatbot
  - retrieval
  - search
  - semantic-search
  - nlp
  - natural-language-processing
type:
  - note
status:
  - in-progress
---
There are 2 distinct parts of the RAG system to evaluate:
1. <**The Retriever**> The part of the RAG system which retrieves information
2. <**The Generator**> The part of the RAG system which parses the retrieved information and formats it for presentation to the end user

I found this beautiful image on https://github.com/amazon-science/RAGChecker and I couldn't resist stealing it:
![](../7%20-%20assets/RAG%20Pipeline%20Evaluation/amazon_ragchecker_metrics.png)

## General Metrics

| Metric Name | Description | Formula | Link(s) |
| ----------- | ----------- | ------- | ------- |
| Precision   |             |         |         |
| Recall      |             |         |         |
| F1 Score    |             |         |         |

## Retriever Metrics 

| Metric Name          | Description | Formula | Link(s)                                                                 |
| -------------------- | ----------- | ------- | ----------------------------------------------------------------------- |
| Context precision    |             |         | - https://docs.confident-ai.com/docs/metrics-contextual-precision<br>-  |
| Context recall       |             |         | https://docs.confident-ai.com/docs/metrics-contextual-recall            |
| Contextual relevancy |             |         | https://docs.confident-ai.com/docs/metrics-contextual-relevancy         |

## Generator Metrics 
| Metric Name      | Type         | Description | Formula | Link(s)                                                                                      |
| ---------------- | ------------ | ----------- | ------- | -------------------------------------------------------------------------------------------- |
| Answer Relevance |              |             |         | https://docs.confident-ai.com/docs/metrics-answer-relevancy                                  |
| Faithfulness     |              |             |         | https://docs.confident-ai.com/docs/metrics-faithfulness                                      |
| G-Eval           |              |             |         | - https://docs.confident-ai.com/docs/metrics-llm-evals<br>- https://arxiv.org/abs/2303.16634 |
| Summarisation    | LLM as judge |             |         | https://docs.confident-ai.com/docs/metrics-summarization                                     |

## References
* https://cookbook.openai.com/examples/evaluation/evaluate_rag_with_llamaindex
* https://docs.confident-ai.com/docs/getting-started
* https://docs.llamaindex.ai/en/stable/examples/evaluation/QuestionGeneration/
* https://github.com/amazon-science/RAGChecker
## Related
* [RagChecker (paper) - A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](RagChecker%20(paper)%20-%20A%20Fine-grained%20Framework%20for%20Diagnosing%20Retrieval-Augmented%20Generation.md)
* [RefChecker (paper) - Reference-based Fine-grained Hallucination Checker and Benchmark for Large Language Models](RefChecker%20(paper)%20-%20Reference-based%20Fine-grained%20Hallucination%20Checker%20and%20Benchmark%20for%20Large%20Language%20Models.md)