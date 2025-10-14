---
created:
  - 2025-10-10T21:09
modified: 2025-10-11 20:11
tags:
  - pdf
  - rag
  - agent
  - agentic
  - llm
  - ai
  - docs
  - document
  - question-answering
  - postgres
  - psql
  - postgresql
  - sql
  - large-language-model
type:
  - note
status:
  - in-progress
---
I'm building a PDF Q&A app at the end of 2025 and this note is a summary of my thoughts and plans. By *PDF Q&A app* I mean a program which you can upload a PDF file to and ask questions about it's contents.

Inspired by the success of the Claude Code CLI agent in 2025, I am implementing a conversational RAG agent. Claude Code showed that an agent with a few thoughtful tools can perform better than a whole lot of clever and involved indexing and preprocessing.
By RAG agent, I mean that the agent can explore a document using it's tools.

Pros of a RAG agent (vs traditional RAG):
- Can control it's own context (e.g. can fetch more data if it hasn't found a satisfactory answer yet)
- Can be guided by the user
- Can self-recover from errors (e.g. failed tool calls)
Cons of a RAG agent (vs traditional RAG):
- More expensive
- Slower
- More complex (e.g. need to build tools, manage agent memory, conversation length etc.)

I am giving my agent the following core tools:

| Tool                    | Description                                                                   |
| ----------------------- | ----------------------------------------------------------------------------- |
| view_page               | View the text of a chosen page                                                |
| view_document_structure | View the hierarchy of sections (i.e. Table of Contents) of the document       |
| search_text             | Search the document for a given query string (FTS, semantic or hybrid search) |

## Decision: Pages vs Chunks

With traditional RAG, one would typically inject the *k* most relevant text chunks into the context window.
I've chosen to let the agent add a single page to it's context at a time.
**Pros of this approach (page at a time)**:
- Agent is consuming the document as a person would (documents are often intentionally structured around page breaks)
- Simplifies the implementation (agent code)
- Easier for the agent to understand is going on
- Gives the agent grounding in the actual document structure
**Cons of this approach (page at a time)**:
- More likely to include irrelevant information in the agent's context window (i.e. fill up useful space with distractions)
- Agent might miss relevant information that is on the previous or next page (e.g. only see part of the relevant section)

## Approach for PDFs with Table of Contents

1. For each item in the table of contents, find which part of the text it's pointing to (allowing for small whitespace and case discrepancies, and noting that a single heading can span multiple lines). When the match is found, turn the heading in the text into a markdown-style heading (i.e. *###* For a level 3 heading etc.)
## Approach for PDFs with no Table of Contents

Here are the approaches that I am considering:

| Approach                                                                                       | Pros                                                                                                                     | Cons                                                                                                                                                                                        | Cost | Notes                                                                                                                                             | Feasibility<br>(my opinion) |
| ---------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| Extract headings by showing every page image to a LLM (1 at a time)                            | - High quality extraction<br>- Understands visual cues                                                                   | - Slow<br>- Expensive<br>- Some LLM mistakes/inconsistencies (e.g. footers as headers)<br>- No heading levels (flat  hierarchy)                                                             |      | Could include the page text too (image + text)                                                                                                    | 💪 strong                   |
| Consider each page a "section", auto-generating a section name                                 | - Conceptually simple<br>- Fits neatly into the existing TableOfContents paradigm<br>- Deterministic<br>- Parallelisable | - How to name each page? (LLM-generated, keyword extraction?)<br>- True document sections are obfuscated/split (dangerous)<br>- Generated "section" headings are less useful for navigation |      |                                                                                                                                                   |                             |
| Just chunk the whole document and do normal RAG                                                | - Easy to implement<br>- Lots of tooling for this                                                                        | - Search tool behaves differently depending on whether the document has a TableOfContents or not.<br>- Loss of hierarchical context (where am I in the document?)                           |      | see [Notes on "Just chunk the whole document and do normal RAG"](#Notes%20on%20"Just%20chunk%20the%20whole%20document%20and%20do%20normal%20RAG") | 💪 strong                   |
| Look for a table of contents in the document text and extract the heading hierarchy from there | - Potentially very structured<br>- Ground-truth, if it exists                                                            | - Not guaranteed to exist<br>- Expensive<br>- Might result in a non-valid heading hierarchy                                                                                                 |      | Maybe good for a first pass (check if it exists)                                                                                                  | 💪 strong                   |
| Extract headings programmatically                                                              | - Fast<br>- Deterministic                                                                                                | - PDFs heading formats are far too varied<br>- Brittle<br>- An endless rabbit-hole of disappointment                                                                                        |      |                                                                                                                                                   | 💩                          |
| Auto-identify sections using semantic chunking                                                 | - Could make more appropriate sections than "each page a section"                                                        | - No guarantee of overlap with the actual sections<br>- True document sections are obfuscated (dangerous)<br>- A bit more of a mission to implement robustly                                |      |                                                                                                                                                   | 🦴 weak                     |
| Put the whole PDF into a LLM at once to get the heading hierarchy                              | - Wow, this would be easy if it worked                                                                                   | - Is there a file size limit?<br>- What is the model doing?<br>- Can the LLM API do this?<br>- Is it using it's own knowledge?<br>- No page numbers (hallucinated garbage)                  |      |                                                                                                                                                   | 💩                          |

### Notes on "Just chunk the whole document and do normal RAG"

If I do this, then what does the result of the **search_text()** tool look like? Possible options are:
1. Just returns the content of all of the chunks directly in a big block of text (or list of texts).
2. Returns a compressed/summarized form of the chunks (e.g. [RECOMP](https://arxiv.org/abs/2310.04408))

Other notes:
- Could do agentic chunking 
## References

* Links to references (source material) go here
## Related

* [Agentic RAG](Agentic%20RAG.md)
* [Advanced RAG Techniques](Advanced%20RAG%20Techniques.md)
* [Retrieval-Augmented Generation (RAG)](Retrieval-Augmented%20Generation%20(RAG).md)
* [Searching for Best Practices in Retrieval-Augmented Generation (paper)](Searching%20for%20Best%20Practices%20in%20Retrieval-Augmented%20Generation%20(paper).md)