---
created:
  - 2026-01-24T23:05
modified: 2026-01-24 23:44
tags:
type:
  - note
status:
  - in-progress
---
I was a skeptic for a very long time, but it's become clear to me that I need to embrace AI-generated coding and become an expert in it (while not losing the ability to think for myself).

I've been very convinced this month by these 3 approaches to AI coding:
1. https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents
2. [# Getting AI to Work in Complex Codebases (Dexter Horthy)](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md)
3. 

Facts I consider to be true:

| Fact                                                                                                                                            | My confidence | Source | Implication for coding agents                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------- | ------------- | ------ | ----------------------------------------------------------------------------------------------------------------------------------------- |
| AI is majority hype and marketing but there is real value for code generation (and learning)                                                    | HIGH          |        |                                                                                                                                           |
| If I delegate all knowledge to LLMs then my own skills will stagnate                                                                            | HIGH          |        |                                                                                                                                           |
| All LLMs have a knowledge cutoff                                                                                                                | HIGH          |        |                                                                                                                                           |
| All LLMs base (pretraining) training data is the open internet                                                                                  | MEDIUM        |        | - LLMs perform best at things more common on the internet (e.g. python vs zig)<br>- LLMs inhabit bad habits (e.g. python bare try/except) |
| All LLMs have different base (pretraining) datasets and fine-tuning                                                                             |               |        |                                                                                                                                           |
| Coding AI agent products (e.g. Claude Code, Cursor, OpenAI codex) wrap the LLMs in a lot of their own custom prompting/tools/wrappers/ecosystem |               |        |                                                                                                                                           |
| All LLMs are auto-regressive next token predictors                                                                                              | HIGH          |        | Ordering of information in the context window matters                                                                                     |
| MCP, skills, subagents, background agents may or may not be useful                                                                              |               |        |                                                                                                                                           |
| AI providers are running at a loss trying to capture market share                                                                               | MEDIUM        |        |                                                                                                                                           |

# Gemini 2.5 Pro

Excellent question. Stepping into the mindset of 2026, where AI coding assistants have matured significantly beyond their 2024 capabilities, the conversation has shifted from "how to write a good prompt" to "how to architect and verify AI-generated systems."

Here are the commonly accepted facts in 2026 about effective prompting approaches for guaranteeing robust, high-quality code.

---

### **Fact 1: "Prompting" Is an Obsolete Term; We Practice "Specification-Driven Generation."**

The 2024 model of writing a long, natural-language prompt in a chat window is considered an elementary, first-generation technique. In 2026, high-quality code generation is achieved through a structured **"Living Specification"** file (e.g., `spec.ai.md` or `architect.yml`) that co-exists with the codebase.

*   **How it works:** This spec file is a formal, yet human-readable, document that the AI agent continuously references. It defines the system's architecture, core entities, invariants (rules that must never be broken), security constraints, and performance budgets. The developer's primary job is to maintain this specification, not to write individual prompts for every function.
*   **Why it guarantees quality:** The AI isn't just fulfilling a one-off request; it's working to keep the entire codebase compliant with an authoritative specification. When a developer asks for a new feature, the agent's first step is to propose an update to the spec file for approval.

### **Fact 2: Test-First Prompting (TFP) Is the Industry Standard.**

Inspired by Test-Driven Development (TDD), Test-First Prompting is non-negotiable for robust systems. You never ask an AI to "write a function that does X." Instead, you provide the AI with a complete set of unit, integration, and property-based tests first.

*   **Example Prompt Structure (2026 style):**
    ```yaml
    # In: user_auth.spec.ai.md
    
    Action: GenerateModule
    Target: 'src/services/authentication.ts'
    
    Description: >
      Create an authentication service that handles user login via password
      and generates a JWT.
    
    Constraints:
      - Must use 'argon2' for password hashing.
      - JWT payload must not contain sensitive data like password hash.
      - Function execution time must not exceed 50ms under standard load.
    
    Tests:
      Unit:
        - 'Asserts a valid user can log in.'
        - 'Asserts an invalid password fails.'
        - 'Asserts the generated JWT can be decoded with the public key.'
      PropertyBased:
        - 'For any given valid username string and password string, the login function either returns a valid JWT or throws a specific AuthenticationError.'
    ```
*   **Why it guarantees quality:** The AI's success condition is explicitly defined and automatically verifiable. The agent will write the code, run the provided tests, and iteratively self-correct until all tests pass. This eliminates ambiguity and ensures correctness by definition.

### **Fact 3: Declarative over Imperative Prompts Are Mandatory.**

You do not tell the AI *how* to write the code (the algorithm). You declare *what* the final state and properties of the code must be. The AI, with its vastly improved reasoning and access to immense libraries of optimal patterns, is far better at selecting the implementation details.

*   **2024 (Imperative):** "Write a for loop that iterates through the users, finds the one with the matching ID, and then returns their name."
*   **2026 (Declarative):** "Define a query function `getUserName(userId)` that retrieves the name for a given ID. This function must be O(1) if backed by a hash map, or O(log n) if backed by a sorted data structure. Ensure it is resilient to non-existent IDs by returning `null`."
*   **Why it guarantees quality:** This forces the developer to think like an architect, specifying outcomes and constraints, while leveraging the AI to handle the rote implementation. It prevents the developer from accidentally "prompting in" a suboptimal or buggy algorithm.

### **Fact 4: Constraint-Based Generation Is More Important Than Feature Generation.**

The biggest leap in quality came from realizing that the most critical part of a prompt isn't the feature description, but the **list of constraints.**

*   **Common Constraints in 2026:**
    *   **Security:** "This module must be free of the OWASP Top 10 vulnerabilities. Sanitize all inputs according to the project's `security.policy` file."
    *   **Performance:** "This data transformation pipeline must process 1M records/sec on a standard `m6i.large` instance."
    *   **Style & Maintainability:** "Adhere to the project's `linting.rc` and complexity rules. All public functions must have documentation with a cyclomatic complexity of less than 5."
    *   **Resource:** "This function should not consume more than 256MB of RAM."
*   **Why it guarantees quality:** Specialized sub-agents (security auditors, performance profilers, etc.) are invoked by the primary coding agent to verify each constraint has been met *before* the code is committed. Code that is functional but violates a constraint is considered a failure.

### **Fact 5: The "Human-in-the-Loop" Is a Verifier, Not a Writer.**

The developer's role has permanently shifted from writing line-by-line code to being the **Chief Architect and Verifier.** Your time is spent on three key activities:

1.  **Authoring the Specification:** Defining the system's "constitution."
2.  **Reviewing the AI's Proposals:** The AI proposes code changes, test plans, and spec modifications. The developer's job is to approve or reject them, providing high-level Socratic feedback ("What are the security implications of this change?" "Is there a more memory-efficient data structure we could use here?").
3.  **Auditing the Final System:** Running final high-level checks and using expert intuition to spot architectural flaws the AI might have missed.

*   **Why it guarantees quality:** It's the ultimate guarantee. The process leverages the AI for near-infinite productivity and correctness on a micro level, while retaining human expert oversight at the macro, architectural level. The "guarantee" is a product of this robust, multi-layered verification process, not a magic prompt.

---

In summary, the key to "guaranteed" high-quality code in 2026 is the acceptance that AI is not a magical intern you boss around in English. It is a formal system that excels within a structured, verifiable, and constraint-heavy development paradigm. The prompt is no longer a request; it's a precise, test-backed specification.

# Claude 4 Sonnet

Here are the main points that are broadly accepted by 2026 among practitioners who use AI coding agents seriously (GitHub Copilot, ChatGPT-Code, Claude Code, etc.) and want *reliably high‑quality* output. None of these guarantees perfection, but they are treated as “best practice” to get robust results.

---

## 1. Clear, concrete specs beat vague requests

**Accepted practice:**
- The more specific your requirements, the better the code.
- Good prompts specify:
  - **Goal / behavior** (what the function or module should do)
  - **Inputs and outputs** (types, formats, edge cases)
  - **Constraints** (performance, memory, security, style rules)
  - **Context** (framework, version, architecture, existing APIs)

**Commonly accepted as true:**
- “Write a function to sort users” → mediocre and generic.
- “In a Django 4.2 app, write a function `get_sorted_users(queryset, *, active_only: bool) -> list[UserDTO]` that sorts by last_name then first_name, excludes soft-deleted users, and is stable. Include tests.” → consistently better.

---

## 2. Provide code context; don’t ask in a vacuum

**Accepted practice:**
- Show the agent relevant:
  - Existing files or snippets
  - Interfaces, types, and schemas
  - Error messages or stack traces
  - Test descriptions or failing tests

**Commonly accepted as true:**
- Agents perform much better when they see the *actual* environment instead of having to guess.
- For refactors and bug fixes, pasting the real function or file dramatically improves correctness.

---

## 3. Ask for tests, invariants, and edge cases explicitly

**Accepted practice:**
- Prompt for:
  - Unit tests (and sometimes property-based tests)
  - Edge case handling
  - Preconditions/postconditions
  - Specific failure modes

**Commonly accepted as true:**
- “Also write tests” produces better, more careful logic than a code-only request.
- Asking “list edge cases first, then write code that passes tests for them” improves robustness.
- Agents can invent tests, but you must still *review* them; they can test the wrong thing.

---

## 4. Use step-by-step reasoning prompts for non-trivial logic

**Accepted practice:**
- Instruct the agent to:
  - Plan before coding (“First outline the approach, then implement”)
  - Explain decisions (“Explain how this handles concurrency issues”)
  - Break down large tasks into smaller subproblems

**Commonly accepted as true:**
- Chain-of-thought or structured reasoning (sometimes hidden, sometimes explicit) *improves correctness* for complex algorithms, protocol implementations, and tricky data transformations.
- For simple CRUD scaffolding it matters less; for anything subtle, it matters a lot.

---

## 5. Iterative refinement beats one-shot prompting

**Accepted practice:**
- Use a loop:
  1. Ask for solution.
  2. Run or scan it.
  3. Paste errors or concerns.
  4. Ask for revisions.

- Treat the AI like a senior-but-fallible collaborator, not an oracle.

**Commonly accepted as true:**
- First draft is rarely the final version for complex tasks.
- Having the agent *fix its own errors* given compiler output, stack traces, or test failures reliably improves quality.

---

## 6. Constrain scope and size of each request

**Accepted practice:**
- Ask for:
  - One function or one file at a time
  - Or one logical change set at a time
- For big tasks:
  - Ask it to propose a plan / task breakdown
  - Then implement each piece in separate turns

**Commonly accepted as true:**
- Very large “rewrite my entire system” prompts lead to brittle, inconsistent code.
- Smaller, composable requests produce more reliable results and are easier to review.

---

## 7. Make style, language, and environment explicit

**Accepted practice:**
- Specify:
  - Language and version (`Python 3.11`, `TypeScript 5`, `C++20`)
  - Framework and versions (`FastAPI`, `Spring Boot 3`, `React 18`)
  - Style rules (PEP 8, ESLint config, naming conventions)
  - Tooling (pytest, JUnit, Jest, Playwright, etc.)

**Commonly accepted as true:**
- Agents will otherwise choose defaults that may conflict with your stack.
- Being explicit reduces mismatches in imports, semantics, and idioms.

---

## 8. Ask for safety and security considerations

**Accepted practice:**
- Prompt for:
  - Input validation
  - Resource cleanup
  - Thread/process safety
  - Secure defaults (e.g., prepared statements, CSRF handling)

**Commonly accepted as true:**
- If you don’t explicitly ask for security and robustness, the agent often optimizes for “simple, illustrative code.”
- Security, error handling, and resilience improve when explicitly requested (or when your prompt includes internal security guidelines).

---

## 9. Use “review mode” and self-critique

**Accepted practice:**
- After getting code, ask the agent to:
  - Review it as if it were written by someone else
  - Identify possible bugs, edge cases, and performance issues
  - Suggest improvements without rewriting everything unnecessarily

**Commonly accepted as true:**
- Self-review prompts (or “critic then fix” loops) materially improve quality.
- Having the agent explain *why* the code is correct often surfaces hidden mistakes.

---

## 10. Ground the agent on real tools and feedback

**Accepted practice:**
- Combine AI with:
  - Compiler/interpreter errors
  - Static analysis (mypy, ESLint, flake8, SonarQube)
  - Test results
- Paste outputs back into the conversation and ask for fixes.

**Commonly accepted as true:**
- The best reliability comes from AI + automated tools + human review.
- When given real tool feedback, agents are much better at converging to correct, idiomatic solutions.

---

## 11. Use system / “role” instructions to set global behavior

**Accepted practice:**
- Establish up front:
  - “You are a senior backend engineer in Python.”
  - “Prioritize readability over micro-optimizations.”
  - “Never use network access; assume offline operation.”

**Commonly accepted as true:**
- Clear role + priorities at the start of the session improves consistency across many turns.
- It reduces the need to restate preferences in every prompt.

---

## 12. No prompt guarantees perfection; human review remains essential

**Accepted practice:**
- Always:
  - Review logic manually for important code
  - Run and extend tests
  - Inspect edge cases that weren’t considered
- Treat AI drafts as high-quality scaffolding, not final truth.

**Commonly accepted as true:**
- Even with excellent prompting, AI can:
  - Misinterpret ambiguous requirements
  - Produce subtly wrong logic
  - Use APIs incorrectly in edge cases
- “Guaranteed robust high-quality code” isn’t achievable solely via prompting; it requires verification.

---

If you want, I can turn these into a concrete “prompt template” you can reuse when asking coding agents for non-trivial features or refactors.


# Claude 4.5 Opus

# Commonly Accepted Facts About Prompting AI Coding Agents (as of 2025)

I should note that I can only speak to what's established through my knowledge cutoff in early 2025, not 2026. Here's what has become generally accepted:

## Widely Accepted Principles

**1. Specificity beats vagueness**
- Explicit constraints (language version, frameworks, error handling requirements) produce more reliable output than open-ended requests

**2. Examples work**
- Providing input/output examples or code style samples significantly improves consistency

**3. Decomposition helps**
- Breaking complex tasks into smaller, sequential prompts yields better results than single monolithic requests

**4. Context windows matter but aren't magic**
- More context helps, but relevant context beats large dumps of irrelevant code

**5. Verification is non-negotiable**
- No prompting technique *guarantees* robust, high-quality code—human review and testing remain essential

## What's Still Contested or Unclear

- Whether "chain of thought" prompting reliably improves code correctness
- Optimal prompt structure (there's no universal template that dominates)
- Whether persona prompts ("you are a senior engineer...") have real effects or are placebo

## Important Caveat

The phrase **"guaranteed robust high quality code"** remains aspirational, not achievable through prompting alone. The 2025 consensus is that prompting improves *probability* of good output, but testing, review, and iteration remain mandatory.

Would you like me to elaborate on any specific technique?

## References
* [Effective harnesses for long-running agents (Anthropic engineering blog)](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
## Related
* [No Vibes Allowed - Solving Hard Problems in Complex Codebases Dex Horthy HumanLayer (presentation at AI Engineer 2025)](No%20Vibes%20Allowed%20-%20Solving%20Hard%20Problems%20in%20Complex%20Codebases%20Dex%20Horthy%20HumanLayer%20(presentation%20at%20AI%20Engineer%202025).md)