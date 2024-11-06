---
created:
  - 2024-11-04T21:25
modified: 2024-11-06 09:42
tags:
  - llm
  - large-language-model
  - prompt
  - prompting
  - nlp
  - natural-language-processing
  - prompt-engineering
type:
  - note
status:
  - in-progress
---
Although I've been generally disparaging of the field of "prompt engineering" (especially the inclusion of the word "engineering"), I actually really enjoyed and would recommend this short course.

This note is my own brief summary of the course content.

- Guidelines
	- Principle 1: Write clear and specific instructions
		- Tactic 1: Use delimiters to clearly separate different parts of the input. [example](#Guidelines%20>>%20Principle%201%20>>%20Tactic%201%20Use%20delimiters%20to%20clearly%20separate%20different%20parts%20of%20the%20input)
		- Tactic 2: Request structured output from the LLM (e.g. HTML, JSON, XML). [example](#Guidelines%20>>%20Principle%201%20>>%20Tactic%202%20Request%20structured%20output%20(e.g.%20HTML,%20JSON))
		- Tactic 3: Ask the model to explicitly check whether certain conditions are satisfied [example](#Guidelines%20>>%20Principle%201%20>>%20Tactic%203%20Ask%20the%20model%20to%20explicitly%20check%20whether%20certain%20conditions%20are%20satisfied)
		- Tactic 4: Few shot prompting. TODO 
	- Principle 2: TODO 
- Iterative Prompt Development
		- Treat the creation of the prompt as you would training of a Machine Learning model i.e. iteratively improve the prompt, at each step comparing/evaluating the model output against a predefined set of test cases and/or metrics
		- Be structured about iterative development. Keep a record of what was tried and what the outcome was
		- Possibly consider also a train/test split so that the prompt is not overfit to a small specific set of evaluation examples 
# Examples 

### Guidelines >> Principle 1 >> Tactic 1 : Use delimiters to clearly separate different parts of the input
```python
prompt = f"""
Summarize the text delimited by triple apostrophes into a single sentence.
'''{input_text}'''
"""
```

### Guidelines >> Principle 1 >> Tactic 2 : Request structured output (e.g. HTML, JSON)
```python
prompt = """
Generate a list of three made-up book titles along with their authors and genres. 
Provide them in JSON format with the following keys: 
book_id, title, author, genre.
"""
```

### Guidelines >> Principle 1 >> Tactic 3: Ask the model to explicitly check whether certain conditions are satisfied
```python
prompt = f"""
Translate the text contained within angle brackets <> into French.
<{input_text}>
If no text is provided, or if the input is not in English, then respond (in English) with "I am unable to process your request" and provide the reason that you cannot process it. 
"""
```

## References
* https://learn.deeplearning.ai/courses/chatgpt-prompt-eng
## Related
* [LLM Prompting Strategies](LLM%20Prompting%20Strategies.md)