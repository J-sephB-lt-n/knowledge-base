---
created:
  - 2024-11-04T21:25
modified: 2024-12-09 11:16
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
		- Tactic 3: Ask the model to explicitly check whether certain conditions are satisfied. [example](#Guidelines%20>>%20Principle%201%20>>%20Tactic%203%20Ask%20the%20model%20to%20explicitly%20check%20whether%20certain%20conditions%20are%20satisfied)
		- Tactic 4: Few shot prompting. Give the model a small number of (or even many) examples of what you want it to do. [example](#Guidelines%20>>%20Principle%201%20>>%20Tactic%204%20Few-Shot%20Prompting)
	- Principle 2: Give the model time to "think"
		- Tactic 1: Provide a list of explicit sequential steps for the model to follow. [example](#Guidelines%20>>%20Principle%202%20>>%20Tactic%201%20Provide%20a%20list%20of%20explicit%20sequential%20steps%20for%20the%20model%20to%20follow)
		- Tactic 2: Request output in a specific standard output format. [example](#Guidelines%20>>%20Principle%202%20>>%20Tactic%202%20Request%20output%20in%20a%20specific%20standard%20output%20format)
		- Tactic 3: Tell the model to perform the task itself first (and use this for comparison) rather than reviewing someone else's work directly. [example](#Guidelines%20>>%20Principle%202%20>>%20Tactic%203%20Tell%20the%20model%20to%20perform%20the%20task%20itself%20first%20(and%20use%20this%20for%20comparison)%20rather%20than%20reviewing%20someone%20else's%20work%20directly)
- Iterative Prompt Development
	- Treat the creation of the prompt as you would training of a Machine Learning model i.e. iteratively improve the prompt, at each step comparing/evaluating the model output against a predefined set of test cases and/or metrics
	- Be structured about iterative development. Keep a record of what was tried and what the outcome was
	- Possibly consider also a train/test split so that the prompt is not overfit to a small specific set of evaluation examples 
- Summarising
	- LLMs are amazing at interpreting natural language and manipulating text.
	- They can easily generate summaries of different types, or for different audiences e.g. "Your task is to summarise the following text, including only details relevant to the pricing department"
- Inferring
	- LLMs are very good at classification tasks based on raw text input e.g. sentiment analysis, labelling, categorisation, topic extraction, tagging, information extraction etc. They can do this via prompting alone i.e. no separate training or fine-tuning steps are required. [example](#Inferring)
- Transforming
	- LLMs are very good at mutating/reforming/translating text. Some example uses:
		- Identifying what language a piece of text is in
		- Translating between different languages (e.g. English -> Chinese)
		- Changing writing tone (e.g. informal to formal, verbose/academic to simple)
		- Translating between different computer formats e.g. html->markdown or XML->JSON etc.
		- Spelling, grammar and style checking
		  
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

### Guidelines >> Principle 1 >> Tactic 4: Few-Shot Prompting
```python
prompt = """
Your task is to answer in a consistent style.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest valley flows from a modest spring; the grandest symphony originates from a single note; the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience. 

<grandparent>: 
""".strip()
```

### Guidelines >> Principle 2 >> Tactic 1:  Provide a list of explicit sequential steps for the model to follow

```python
prompt = f"""
Perform the following actions: 
1 - Summarize the following text delimited by triple apostrophes with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following keys: french_summary, num_names.

Separate your answers with line breaks.

Text:
'''{text}'''

""".strip()
```

### Guidelines >> Principle 2 >> Tactic 2: Request output in a specific standard output format

```python
prompt = f"""
Your task is to perform the following actions: 
1 - Summarize the following text delimited by <> with 1 sentence.
2 - Translate the summary into French.
3 - List each name in the French summary.
4 - Output a json object that contains the following keys: french_summary, num_names.

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in summary>
Output JSON: <json with summary and num_names>

Text: <{text}>

""".strip()
```

### Guidelines >> Principle 2 >> Tactic 3:  Tell the model to perform the task itself first (and use this for comparison) rather than reviewing someone else's work directly

```python
prompt = f"""
Your task is to determine if the student's solution is correct or not.
To solve the problem do the following:
- First, work out your own solution to the problem including the final total. 
- Then compare your solution to the student's solution and evaluate if the student's solution is correct or not. 
Don't decide if the student's solution is correct until you have done the problem yourself.

Use the following output format:

Question:
~~~
original question here
~~~

Student's solution:
~~~
student's solution here
~~~

Actual solution:
~~~
steps to work out the solution and your solution here
~~~

Is the student's solution the same as actual solution just calculated?:
~~~
yes or no
~~~

Student grade:
~~~
correct or incorrect
~~~

Here is the student's solution:
{students_solution_text}
""".strip()
```

### Inferring

```python
prompt = f"""
Identify the following items from the review text: 
- Sentiment (positive or negative)
- Is the reviewer expressing anger? (true or false)
- Item purchased by reviewer
- Company that made the item

The review is delimited with triple backticks. 
Format your response as a JSON object with "Sentiment", "Anger", "Item" and "Brand" as the keys.
If the information isn't present, use "unknown" as the value.
Make your response as short as possible.
Format the Anger value as a boolean.

Review text: '''{review_text}'''
""".strip()
```
## References
* https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/
## Related
* [LLM Prompting Strategies](LLM%20Prompting%20Strategies.md)