---
created:
  - 2024-10-26T20:03
modified: 2024-10-26 22:31
tags:
  - nlp
  - embedding
  - transformer
  - text
  - sentiment-analysis
  - semantic
  - semantic-search
  - classification
  - text-classification
  - question-answering
  - language
  - named-entity-recognition
  - paraphrase-detection
  - text-summarisation
type:
  - note
status:
  - completed
---
Bidirectional Encoder Representations from Transformers (BERT) is a pretrained encoder-only language model based on the transformer architecture. 

The paper originally introducing BERT is [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2019)](https://arxiv.org/abs/1810.04805).

It is a deep neural network model designed to learn a rich, general representation of language. It is pretrained on BooksCorpus (800M words) and English Wikipedia (2,500M words).

The BERT model is intended to be used as a base model to be extended in order to perform specific downstream NLP tasks such as:

| Task                                                                      | Explanation                                                                                                                         |
| ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| Sentiment Analysis                                                        |                                                                                                                                     |
| Text Classification                                                       |                                                                                                                                     |
| Question-answering                                                        | Given a question and a passage of text, the model is used to identify which part of the passage contains the answer to the question |
| [Named Entity Recognition (NER)](Named%20Entity%20Recognition%20(NER).md) |                                                                                                                                     |
| Paraphrase Detection                                                      |                                                                                                                                     |
| Semantic Search                                                           |                                                                                                                                     |
| [Extractive text summarisation](https://arxiv.org/abs/1906.04165)         |                                                                                                                                     |
In order to be used in a specific NLP task, BERT can either be fined-tuned (i.e. a single classification layer is added to the end of the BERT model and all of the weights in the entire model are tuned based on the specific downstream task), or a portion of the features in the BERT model are used as is in another model (i.e. BERT provides only a text embedding).   

## References
* [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding (2019)](https://arxiv.org/abs/1810.04805).
* [Leveraging BERT for Extractive Text Summarization on Lectures](https://arxiv.org/abs/1906.04165)
## Related
* [Named Entity Recognition (NER)](Named%20Entity%20Recognition%20(NER).md)