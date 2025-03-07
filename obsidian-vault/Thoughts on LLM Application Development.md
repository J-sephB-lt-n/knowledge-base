---
created:
  - 2025-03-06T14:22
modified: 2025-03-06 14:55
tags:
  - llm
  - large-language-model
  - gpt
  - genAI
  - ai
  - dev
  - app
  - job-application
  - software
type:
  - note
status:
  - ongoing
---
- Frame every design decision in the context of how LLMs work:
	- They are auto-regressive probabilistic next-token predictors (they are essentially autocomplete with a massive amount of contextual understanding). 
		- This means their outputs always look great, even when they are wrong.
	- They are usually trained on large portions of the internet and/or books and/or papers and/or synthetic data (their predictions are good on knowledge prevalent in their training data and unstable on knowledge rare/missing from their training data).
	- They have typically been fine-tuned to follow instructions and not output anything unethical/dangerous/rude.
- Set model temperature to 0 for deterministic tasks (tasks requiring no creativity)
- Limit the LLM's decision space (limit the number and complexity of the decisions the model must make as far as possible)
- For a model which is frequently updated/modified, maintain a static evaluation process (similar to software unit tests), which output a reproducible and objective measure of model quality at any given point in time. *Vibe checking* is not good enough.
- A good LLM application is the same as a good software application - all of the same principles apply (monitoring, scalability, performance, cost, security, documentation, error recovery etc.)
- Few-shot prompting works very well
- Models can forget things in the middle of a long prompt (put the most important content at the beginning or end of the prompt, or repeat it multiple times in different places)
- Run any LLM-generated code in an access-restricted environment (e.g. LLM-generated SQL code to be run by a resource-constrained database user with read-only access).
- I really like the *"human employee test"* - can a human with no context other than your prompt easily complete the required task?
- Be painfully unambiguous in your prompt. 
	- If one were to follow the instructions to the letter, it would be impossible to mess it up.
	- The instructions should not require any interpretation, or for assumptions to be made
	- Make the required task painfully easy/straightforward - like an idiot could do it
- Do not include any irrelevant information in the prompt
- Use structures and style that are extremely common in the model's training data (you can probably assume that was the internet) e.g. html, json, markdown
- Break down complex problems into as many straightforward subtasks as possible
	- Run each subtask in a different independent chat completion. Be intentional about what context each subtask has access to (don't include irrelevant information).
	- Subtasks which can be performed deterministically without using genAI should not use genAI.
	- You can run validation (and retry patterns) on each individual subtask, not allowing the full pipeline to proceed if a single subtask fails.
- Robustness can be achieved by doing the same thing using different methods and then verifying that the outputs agree (e.g. parse the text from an image using different models and then compare their outputs)
- Give end-users insight into what the model output means, or how it was generated.
	- e.g. Run a separate LLM to explain what a generated SQL query is doing, with no context of the original user request.
	- i.e. Give the end-user tools which they can use to evaluate the system output and make an informed decision on whether it is correct/incorrect. 
- LLMs are sensitive to emotional language. Telling them that something is "critical" or "you will lose your job if they get it wrong" can have a material impact on the quality of their output (read [Large Language Models Understand and Can be Enhanced by Emotional Stimuli](https://arxiv.org/abs/2307.11760))
## References
* Links to references (source material) go here
## Related
* [LLM Strengths & Weaknesses](LLM%20Strengths%20&%20Weaknesses.md)
* [LLM Prompting Strategies](LLM%20Prompting%20Strategies.md)
* [CIDI Prompting Strategy](CIDI%20Prompting%20Strategy.md)