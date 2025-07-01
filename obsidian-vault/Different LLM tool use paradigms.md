---
created:
  - 2025-04-15T12:04
modified: 2025-04-15 12:29
tags:
  - llm
  - large-language-model
  - agent
  - agentic
  - ai
  - genAI
  - tool
  - tool-use
  - tool-calling
  - function-calling
type:
  - note
status:
  - in-progress
---
There are many ways to enable Large Language Models (LLMs) to use tools.

Below is an in‐depth overview of each approach along with a table that summarizes evaluations on key dimensions. I’ve also provided a brief discussion explaining the reasoning behind each assessment.

---

### 1. Parsing Function Calls Manually

**Overview:**  
This approach involves instructing your language model (via prompts) to output tool calls as JSON blocks. You then write custom code to extract and process these calls.

**Pros:**

- **Flexibility/Customizability:** You can design your own format and logic exactly as you need it.
    
- **Minimal External Dependencies:** No need for third‑party libraries, which may simplify integration in some contexts.
    

**Cons:**

- **Maintainability:** Hand‑rolled parsing logic can become complex and harder to maintain as requirements evolve.
    
- **Standardization & Support:** Since it’s a custom solution, there isn’t an ecosystem or community behind it, which can lead to potential pitfalls in long‑term support.
    
- **Robustness & Error Handling:** Error handling must be explicitly built, and edge cases may be easily missed.
    

---

### 2. Using Open Source Python Libraries

**Overview:**  
Libraries such as LangChain, Haystack, pydanticAI, or Atomic Agents provide frameworks for tool integration, often including abstractions that simplify the creation, validation, and routing of tool calls.

**Pros:**

- **Standardization & Ecosystem:** Many of these libraries are widely used and have active communities.
    
- **Support & Community:** They typically come with documentation, examples, and community support.
    

**Cons:**

- **Dependencies & Integration:** Adding new libraries increases dependencies, and you must ensure compatibility with your existing stack.
    
- **Learning Curve:** Some frameworks can be complex and require familiarity with their patterns and abstractions.
    

---

### 3. Using the Tool‑Calling Functionality of the Model API

**Overview:**  
Some providers now offer built‑in tool‑calling capabilities directly within their model APIs. This offloads the parsing, validation, and routing logic to the provider.

**Pros:**

- **Maintainability & Robustness:** The heavy lifting is managed by the provider, resulting in robust error handling and high reliability.
    
- **Ease of Use:** Lower learning curve since you’re leveraging managed services rather than developing custom code.
    

**Cons:**

- **Flexibility/Customizability:** You may be constrained by the provider’s API design and may not be able to tweak behaviors as deeply as with a custom solution.
    
- **Standardization:** The approach differs by provider, which can become an issue if you need multi‑provider support.
    

---

### 4. Parsing Tool Calls Out of Structured Output

**Overview:**  
Here the model is instructed to generate output that already conforms to a predefined schema (for example, via libraries like the instructor python library). The tool calls are embedded within this structured schema.

**Pros:**

- **Robustness & Error Handling:** The structured schema can enforce required fields, reducing ambiguities.
    
- **Maintainability:** Schemas and associated validation libraries tend to lead to code that is easier to maintain over time.
    
- **Flexibility:** Allows for pre‑defined contracts for tool calls, making integration predictable.
    

**Cons:**

- **Dependencies & Learning Curve:** Requires integrating with and learning specific schema libraries, which adds overhead.
    
- **Standardization & Community:** Although structured output is a promising approach, standardized schemas are still an evolving area and may lack universal adoption.
    

---

### 5. Model Context Protocol

**Overview:**  
The [Model Context Protocol](https://modelcontextprotocol.io/) is an emerging standard aimed at defining a structured, interoperable means for passing context (including tool calls) between models and external systems.

**Pros:**

- **Flexibility/Customizability:** Designed to be adaptable across various implementations and future‑proof your integrations if the standard is widely adopted.
    
- **Maintainability:** A standardized protocol can simplify long‑term support and reduce custom maintenance overhead.
    

**Cons:**

- **Learning Curve:** It is a new concept, so teams may face a steep learning curve and integration hurdles.
    
- **Support & Community:** As an emerging standard, its community and ecosystem are still in development, which may limit immediate support and resources.
    
- **Dependencies & Robustness:** Depending on the maturity of implementations, robustness and error‑handling mechanisms might be less battle‑tested compared to established providers.
    

---

### Summary Evaluation Table

Below is a table summarizing the assessments across the various dimensions:

Rating scale:
- ✅ – Strong/Good
- 🤷 – Mixed/Passable
- ❌ – Weak/Negative 

|Dimension|Manual Parsing (1)|Open Source Python Libraries (2)|Model API Tool-Calling (3)|Structured Output (4)|Model Context Protocol (5)|
|---|---|---|---|---|---|
|**Flexibility/Control/Customizability**|✅|🤷|🤷|✅|✅|
|**Maintainability**|🤷|🤷|✅|✅|✅|
|**Security**|🤷|🤷|✅|✅|🤷|
|**Robustness & Error‑Handling**|🤷|🤷|✅|✅|🤷|
|**Dependencies & Integration**|✅|❌|✅|🤷|🤷|
|**Learning Curve/Complexity**|🤷|🤷|✅|🤷|❌|
|**Standardisation/Ecosystem**|❌|✅|🤷|🤷|🤷|
|**Support and Community**|❌|✅|🤷|🤷|❌|

---

### Final Remarks

Each approach carries its own balance of trade-offs:

- **Manual parsing** can be very flexible and dependency‑light but may end up being hard to maintain and support in the long run.
    
- **Open source libraries** offer rich ecosystems and community support but introduce additional dependencies and potential integration complexities.
    
- **Using built‑in tool‑calling APIs** simplifies error‑handling and lowers the learning curve, though at the cost of customization and vendor lock‑in.
    
- **Structured output parsing** leverages schema definitions for more robust integrations yet may require more initial setup and familiarity with the tooling.
    
- **The Model Context Protocol** is an exciting, emerging approach that promises standardization and flexibility but currently comes with challenges related to maturity, community support, and a steeper learning curve.
    
Ultimately, the best approach depends on your application's scale, required flexibility, and long-term maintenance plans.
## Generation of this note
I generated the version version of this note using ChatGPT o3-mini using the following prompt:

```
I'm not sure what the best way is to enable Large Language Models to use tools ("function-calling") in my production AI applications.

Can you please provide me insightful and varied pros and cons for each of the following approaches:

1. Parsing function calls manually from the text model response (i.e. including in the model prompt something like "for each required tool call, output a JSON markdown block in format '...'")

2. Using one of the open source python libraries (e.g. pydanticAI, langchain, atomic agents, haystack etc.)

3. Using the tool-calling functionality of the model API (differs per provider)

4. Parsing tool calls out of structured output (the model generates structured output using for example the instructor python library, and tool calls are included in the schema of this response)

5. Model Context Protocol (please refer directly to https://modelcontextprotocol.io/)

Please include in your output a table in which each cell contains one of the following:

- ✅ – Strong/Good

- 🤷 – Mixed/Passable

- ❌ – Weak/Negative

Please evaluate these on the following dimensions:

- flexibility/control/customizability

- maintainability

- security

- robustness and error-handling

- dependencies and integration

- learning curve/complexity

- standardisation/ecosystem

- support and community
```
## References
* https://modelcontextprotocol.io/
## Related
* Links to other notes which are directly related go here