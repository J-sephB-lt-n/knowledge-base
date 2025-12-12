---
created:
  - 2025-12-10T12:56
modified: 2025-12-11 13:24
tags:
  - llm-agents
  - claude-code
  - coding
  - ai-coding
  - coding-agent
  - cursor
type:
  - note
status:
  - ongoing
---

You must always write code that (where relevant) fulfils all of the requirements of high quality code:
- **Functionality**: Works as expected and fulfills its intended purpose.
- **Readability**: Is easy for humans to understand.
- **Documentation**: Clearly explains its purpose and usage.
- **Standards Compliance**: Adheres to conventions and guidelines, such as PEP 8.
- **Reusability**: Can be used in different contexts without modification.
- **Maintainability**: Allows for modifications and extensions without introducing bugs.
- **Robustness**: Handles errors and unexpected inputs effectively.
- **Testability**: Can be easily verified for correctness.
- **Efficiency**: Optimizes time and resource usage.
- **Scalability**: Handles increased data loads or complexity without degradation.
- **Security**: Protects against vulnerabilities and malicious inputs.

Use assert statements frequently to validate the expected state of the system. Always include a short assert message.
## Error Handling 
- Exceptions are an important signal and should not be thoughtlessly suppressed.
- Unexpected program behaviour must raise an exception (don't try to catch developer mistakes with error-handling code).
- A bare try/except may only be used at the most top end-user-facing level of the application (if at all). All other exceptions must bubble up. 
## References
* https://realpython.com/python-code-quality/
## Related
* [Code Assessment Rubric](Code%20Assessment%20Rubric.md)
* [Thoughts on LLM Application Development](Thoughts%20on%20LLM%20Application%20Development.md)
* [Approaches to LLM app development](Approaches%20to%20LLM%20app%20development.md)
* [No Vibes Allowed - Solving Hard Problems in Complex Codebases Dex Horthy HumanLayer (presentation at AI Engineer 2025)](No%20Vibes%20Allowed%20-%20Solving%20Hard%20Problems%20in%20Complex%20Codebases%20Dex%20Horthy%20HumanLayer%20(presentation%20at%20AI%20Engineer%202025).md)