---
created:
  - 2025-12-10T12:56
modified: 2026-07-23 20:58
tags:
  - llm-agents
  - claude-code
  - coding
  - ai-coding
  - coding-agent
  - cursor
  - agentic
  - IDE
  - software-development
  - software-engineering
type:
  - note
status:
  - ongoing
---
## General Instructions
- Never read any files before explicitly asking my permission first.
- When reporting information to me, be extremely concise and sacrifice grammar for the sake of concision. 

## General Software Principles
- You must always write code that (where relevant) fulfils all of the requirements of high quality code:
	- **System Complexity is Minimised**: The architecture as whole must keep the codebase easy to understand and maintain.
		- Making a small change must not require editing code/files in lots of different places.
		- A developer should not need to hold a lot of information in their head at once to make a simple change.
		- All knowledge required to make a small change must be visible at the change site (no unknown unknowns). i.e. **important information should be obvious**
	- **Functionality (correctness)** : Works as expected and fulfills its intended purpose.
	- **Readability**: Is easy for humans to quickly comprehend (code is optimised for clarity).
	- **Documentation**: Clearly explains its purpose and usage.
	- **Standards Compliance**: Adheres to conventions and guidelines (e.g. PEP 8 for python code).
	- **Reusability**: Can be used in different contexts without modification.
	- **Maintainability**: Allows for modifications and extensions without introducing bugs.
	- **Robustness**: Handles errors and unexpected inputs effectively.
	- **Testability**: Can be easily verified for correctness.
	- **Efficiency**: Optimizes time and resource usage.
	- **Scalability**: Handles increased data loads or complexity without degradation.
	- **Security**: Protects against vulnerabilities and malicious inputs.
- Aim for high cohesion within modules and low coupling between them.
- If you encounter any inconsistencies or contradicting information in your task requirements, always bring this to my attention.

## Code Style
- Unless you are only providing a single argument and it is obvious what that argument is, always use named arguments when calling a function. 
- Use assert statements frequently as lightweight validation of the expected state of the system.
	- Always include a short assert message.
- Very long `.py` scripts are a code smell. Over 500 lines is a warning, but generally still ok if there is a good reason. Python scripts over 1000 lines require a strong justification. Obviously, one expects HTML, template files, data files like CSV etc. to be very long.
- Code should not be platform-specific e.g. filepaths should use `Path(...)` from `pathlib` not windows path strings.
- Python imports should always appear at the top of the *.py* script (e.g. not within functions etc.), unless there is a strong justification for it.
- NEVER use relative pathing logic like `Path(__file__).resolve().parent.parent.parent` - this indicates a project organisation failure. All python scripts should be executed from the same project directory.
- Don't use module-level constants (`_SOME_VAR=...`) unless that constant genuinely needs to be shared by multiple functions/classes in the module. Unnecessary module-level constants make the code harder to read (code reviewer needs to jump back and forth to understand the behaviour, for no good reason).
## Module Architecture
- Modules should be deep, not shallow i.e. functions/classes/methods should have a simple interface (with good defaults) and hide it's complexity from the caller inside it's implementation code.

## Type Annotation
- Type annotate everything.
- Make the type annotations as readable as possible (prioritise readability over comprehensiveness).
- Don't use typing.Dict, typing.List, typing.Tuple etc. (you can use the base types dict, list, tuple etc. in type annotations on python 3.9+).
- After working on a piece of code, use `uv run ty check` to check that your type annotations are correct (you may need to install `ty` using `uv add --dev ty`)
- Never use `from __future__ import annotations` - just quote forward references directly (`foo: "Bar"`) or use `from typing import TYPE_CHECKING`
- Use `typing.NewType` or value objects rather than base types so that complex type annotations become self-documenting e.g. `dict[UserId, UserMetadata]` rather than `dict[str, dict]`

## Documentation
- All codebases should have a README.md file at the project root. It must be a brief but  information dense document (optimised for human-readability) containing important context for understanding the application, intended to provide new developers with sufficient information to begin contributing to the codebase. It should include:
	  - The name of the application
	  - A high-level description of the primary goal(s) of the application
	  - Instructions on how to setup and run the application (and test suite).
	  - A filetree-style illustration of the layout of the codebase, with comments explaining the role of each module (or a link to another document containing this) 
- All modules, classes and functions must have google-style docstrings.
	- Function and method docstrings should include an explanation of each argument, the return type, any side effects and possible exceptions raised.  
- Comments (and all other code documentation) should describe things which aren't obvious from the code itself. 
- Comments should be used sparingly. As far as possible, code should be self-documenting. Here are some general principles which often help:
	- Descriptive naming.
	- Complex logic broken down into well-named single-responsibility chunks (clean abstractions).
	- No magic numbers (use named constants instead).
- In any other places where documentation is optional (e.g the "description" argument in `pydantic.Field` on attributes in a `pydantic.BaseModel`, the "help" argument in `argparse.ArgumentParser().add_argument()`, always provide useful documentation).
- For pydantic models, use `Field(description=...)` for documenting attributes rather than a block in the class docstring.

## Software Testing
- I don't believe in 100% test coverage, but please identify parts of the code which would be made more robust by adding tests and raise these with me.
- The test suite is going to consist of hundreds of tests, so ensure that no individual unit test takes more than 1 second to run.
- You are never allowed to delete or modify existing tests. If you have a compelling reason to do so, ask me directly for permission first.

## Error Handling 
- Exceptions are an important signal and should not be thoughtlessly suppressed.
- Unexpected program behaviour must raise an exception (don't try to catch developer mistakes with error-handling code).
- A bare try/except may only be used at the topmost end-user-facing level of the application (if at all). All other exceptions must bubble up.
- Always log the full stack trace (e.g. use *logger.exception()* rather than *logger.error(..., exc_info=True)*)
- Don't add unnecessary handling code for rare or impossible scenarios.  

## Package Dependencies
- Never add dependencies to a `pyproject.toml` directly - use the package manager (e.g. `uv add` or `poetry add` etc.).
- When adding new dependencies, don't pin versions explicitly - let the package manager download the latest package version.
- Never add package dependencies without asking me first for explicit permission.

## User Inputs 
- User inputs should always be assumed to be malicious.

## Red Flags
- ALWAYS ask permission before using any of the following functions/keywords:
	- exec
	- eval
	- global

## Environment Variables
- Never print or log secrets
- Always use `override=True` in `dotenv.load_dotenv()`, to avoid using existing global secrets by accident.

## Large Language Models (LLMs)
- When using a LLM to generate structured data, always use the structured output functionality of the LLM client (don't ask for structured data in a free-text chat completion and then manually parse out the data).

## References
* https://realpython.com/python-code-quality/
## Related
* [Code Assessment Rubric](Code%20Assessment%20Rubric.md)
* [Thoughts on LLM Application Development](Thoughts%20on%20LLM%20Application%20Development.md)
* [Approaches to LLM app development](Approaches%20to%20LLM%20app%20development.md)
* [No Vibes Allowed - Solving Hard Problems in Complex Codebases Dex Horthy HumanLayer (presentation at AI Engineer 2025)](No%20Vibes%20Allowed%20-%20Solving%20Hard%20Problems%20in%20Complex%20Codebases%20Dex%20Horthy%20HumanLayer%20(presentation%20at%20AI%20Engineer%202025).md)