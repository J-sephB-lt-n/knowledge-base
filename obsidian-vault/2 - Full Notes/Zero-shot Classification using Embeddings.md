---
created:
  - 2024-08-01T13:23
modified: 2024-08-01 13:27
tags:
  - classification
  - zero-shot
  - zero-shot-learning
  - embedding
  - latent
  - unsupervised
  - nlp
  - large-language-model
type:
  - note
status:
  - completed
---
One can do zero-shot classification of documents by comparing each embedded label to the embedded document (using the same embedding model), and assigning the label closest to the document in the embedding space 

I read a blog post by Han Xiao from jina.ai who describes how turning each label into a sentence rather than a label (e.g. label "negative" to a sentence like "this review is negative") can improve classification performance (he showed a best increase of 19% in F1 score).
## References
* https://jina.ai/news/rephrased-labels-improve-zero-shot-text-classification-30/