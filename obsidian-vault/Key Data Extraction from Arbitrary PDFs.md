---
created:
  - 2026-07-02T12:58
modified: 2026-07-02 13:46
tags:
  - pdf
  - extract
  - data
  - parse
  - parsing
  - text-parsing
  - pdf-parsing
  - document
  - data-extraction
type:
  - note
status:
  - in-progress
---
Main body of note goes here
## Ideas 

- Make this into a user interface for data extraction rather than an automated pipeline e.g. LLM or something finds the data you are looking for and then you have an interface for saying accept/reject (with a confidence indicator)
- This is prime territory for an evaluation set (and DSPy for prompt optimisation over the training subset of it)

## To check out

- https://github.com/google/langextract: "A Python library for extracting structured information from unstructured text using LLMs with precise source grounding and interactive visualization."
- DSPy for prompt optimisation
- LlamaIndex
- Haystack 2

## ChatGPT recommends

```
PDF
    │
    ▼
Docling
    │
    ▼
Document object
    │
    ├── pages
    ├── tables
    ├── figures
    ├── layout
    ▼
Agent
    │
    ▼
Locate relevant sections
    │
    ▼
LLM extraction
(Instructor/Pydantic model)
    │
    ▼
Validation
    │
    ▼
Retry if needed
    │
    ▼
DTOs

BalanceSheet
IncomeStatement
CashFlow
CompanyMetadata
Footnotes
...
```
## References

* Links to references (source material) go here
## Related

* Links to other notes which are directly related go here