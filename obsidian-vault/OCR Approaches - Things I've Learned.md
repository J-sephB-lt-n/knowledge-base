---
created:
  - 2026-08-19T08:44
modified: 2026-08-19 09:51
tags:
  - ocr
  - information
  - information-extraction
  - data
  - extract
  - data-extraction
  - extraction
  - llm
type:
  - note
status:
  - ongoing
---
- By far the highest quality PDF-to-text approach I have found (which preserves text layout well in most cases) is [poppler](https://poppler.freedesktop.org/):
	  ```bash
	  pdftotext -enc UTF-8 -eol unix -layout input.pdf output.txt
	  ```
	  **much** better text layout than pymupdf in all cases (even with pymupdf refinement).
- If each document has a deterministic (static) expected format, don't use approximate methods like ML or LLMs
	- You can see an example of this approach here: https://github.com/J-sephB-lt-n/pdf-bank-statement-parser
- I've explored loads of open source ML approaches, and I haven't found one good enough yet:
	- Most are very dependency-bloated (millions of unmaintained python dependencies) 
	- [docling](https://github.com/docling-project/docling) is very dependency-bloated, slow, resource-hungry, the documentation isn't great, and I found it making things up in some cases.
	- [marker](https://github.com/datalab-to/marker) seems better than docling, but it has license restrictions for companies with too much revenue.
	- There are millions of other options - I've explored a fair amount and haven't found anything good enough yet, but I definitely haven't tried everything.
- LLM-based approaches:
	- Bear in mind that LLMs are generative models - I have seen them invent/modify data before on OCR tasks (e.g. adding dollar signs to numbers where there are none in the source). But with frontier models since end of 2025 it seems like this is becoming more rare (but it will never go away).
		- For approximate OCR approaches like this, you need to build an eval set against which you measure your accuracy. This also helps you track improvement/regression as you modify your system.
	- For small PDFs (<50 pages), you can just give the whole PDF to the LLM as page images, or give both the images and the page text.
		- The images must be size-gated and optimally compressed/processed to not lead to context rot.
	- For bigger PDFs, I've had decent success with the following approaches (the first - agentic - approach I think is higher quality):
		- Give the agents tools for exploring the document themselves (view_page_text, view_page_image, search_text)
		- Use a sequence of targeted agents which share a knowledge base (e.g. first agent finds only the Table-of-Contents and required sections, later parallel agents extract specific information informed by the findings of the section agent)
    

3. Use an LLM agent flow:
    

4. Give the agents tools for exploring the document themselves (view_page_text, view_page_image, search_text)
    
5. Use a sequence of targeted agents which share a knowledge base (e.g. first agent finds only the Table-of-Contents and required sections, later parallel agents extract specific information)
## References
* Links to references (source material) go here
## Related
* Links to other notes which are directly related go here