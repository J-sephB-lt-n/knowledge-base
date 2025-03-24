---
created:
  - 2024-07-11T16:03
modified: 2024-10-01 20:53
tags:
  - rag
  - retrieval-augmented-generation
  - llm
  - nlp
  - search
type:
  - paper
status:
  - completed
---
Arxiv link: https://arxiv.org/abs/2407.01219
Authors: [Xiaohua Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+X), [Zhenghua Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Z), [Xuan Gao](https://arxiv.org/search/cs?searchtype=author&query=Gao,+X), [Feiran Zhang](https://arxiv.org/search/cs?searchtype=author&query=Zhang,+F), [Yixin Wu](https://arxiv.org/search/cs?searchtype=author&query=Wu,+Y), [Zhibo Xu](https://arxiv.org/search/cs?searchtype=author&query=Xu,+Z), [Tianyuan Shi](https://arxiv.org/search/cs?searchtype=author&query=Shi,+T), [Zhengyuan Wang](https://arxiv.org/search/cs?searchtype=author&query=Wang,+Z), [Shizheng Li](https://arxiv.org/search/cs?searchtype=author&query=Li,+S), [Qi Qian](https://arxiv.org/search/cs?searchtype=author&query=Qian,+Q), [Ruicheng Yin](https://arxiv.org/search/cs?searchtype=author&query=Yin,+R), [Changze Lv](https://arxiv.org/search/cs?searchtype=author&query=Lv,+C), [Xiaoqing Zheng](https://arxiv.org/search/cs?searchtype=author&query=Zheng,+X), [Xuanjing Huang](https://arxiv.org/search/cs?searchtype=author&query=Huang,+X)

Conclusions:
1. Incorporate a _query classification module_ (i.e. a model trained to classify whether a given user query requires retrieval at all, or if the LLM can respond accurately without external information). This can improve accuracy of the system.
2. If efficiency matters, use "Hybrid Search" (i.e. a weighted average of BM25 on a sparse bag-of-word vector and a dense embedding vector). If accuracy is all that matters, use "Hybrid Search with HyDE" (https://arxiv.org/abs/2212.10496) i.e. the same thing but replacing the dense embeddings with hypothetical document embeddings.
3. If efficiency matters, use TILDEv2 (https://arxiv.org/abs/2108.08513) for reranking. If accuracy is all that matters, use monoT5 (https://arxiv.org/abs/2003.06713) for reranking.
4. Repack retrieved results in reverse (ascending order of relevancy score i.e. most relevant last, closest to the query).
5. Use Recomp (https://arxiv.org/abs/2310.04408) for summarisation. 

## Related
* [[Applied Large Language Model Concepts]]
* [[Advanced RAG Techniques]]