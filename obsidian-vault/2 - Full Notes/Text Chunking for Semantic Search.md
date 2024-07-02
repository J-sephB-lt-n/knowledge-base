---
created:
  - 2024-07-01T12:21
modified: 2024-07-01 22:49
tags:
  - embedding
  - rag
  - search
  - retrieval-augmented-generation
  - semantic-search
  - semantic
  - nlp
  - large-language-model
  - personal-project
type:
  - note
status:
  - completed
---
The way that the input text is split (_chunked_) has a material impact on the performance and usability of the semantic search (e.g. RAG) application.

Here are some approaches:

| Approach                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Fixed-Size Chunks               | Divide text into chunks of the same fixed length (e.g. 100 characters each). These chunks can be made be made to overlap, or not.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| Split by separator              | Split the text on a specific separator pattern e.g. <br><ol> <li>Sentence end punctuation {., ?, !}</li> <li>Newline "\n"</li> <li>Paragraph break (double new line) "\n\n"</li> </ol>                                                                                                                                                                                                                                                                                                                                                                                                           |
| Document-format-based splitting | Use the explicit structure in the document to split the content (e.g. by HTML tag, or by markdown header etc.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Semantic splitting              | Embed each sentence into a semantic space, then start a new chunk whenever the distance (e.g. cosine distance) between 2 consecutive sentence embeddings is large (this could be by a chosen threshold, or by some other algorithmic method). To reduce noise, one usually uses a rolling window approach (e.g. compare embedding of combined sentences {1,2,3} to combined embedding of sentences {2,3,4} and so on)                                                                                                                                                                            |
| LLM Agent                       | Instruct a Large Language Model to chunk the text (e.g. work sequentially through the text, deciding where the break points should be, as a human would).                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Alternative Representation      | Convert the raw data into another form, more suitable for querying. Examples:<br><ol><li>Replace paragraphs with LLM-generated summaries of those paragraphs</li><li>Convert pronouns ("he","it","this","that" etc.) into their named entities (e.g. "Professor Plum", "Harvard University") - see "Dense.X Retrieval"</li><li>Use an LLM to extract useful searchable metadata from each paragraph (e.g. questions answered, title generation, keyword extraction, named entity extraction etc.)- see https://docs.llamaindex.ai/en/stable/module_guides/indexing/metadata_extraction/</li><ol> |

## References

- <https://github.com/FullStackRetrieval-com/RetrievalTutorials/blob/a4570f3c4883eb9b835b0ee18990e62298f518ef/tutorials/LevelsOfTextSplitting/5_Levels_Of_Text_Splitting.ipynb>
- <https://docs.llamaindex.ai/en/stable/module_guides/indexing/>

## Related

- [[personal-projects (github repo)]]
- [[semantic-search-engine (github repo)]]


