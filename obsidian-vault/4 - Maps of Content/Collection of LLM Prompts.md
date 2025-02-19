---
created:
  - 2025-01-26T20:12
modified: 2025-02-19 09:17
tags:
  - genAI
  - llm
  - nlp
  - large-language-model
  - prompt
  - prompting
  - prompt-engineering
  - system-prompt
type:
  - map-of-content
status:
  - ongoing
---
There is a wealth of amazing prompts in this massive paper: [The Prompt Report: A Systematic Survey of Prompting Techniques](https://arxiv.org/abs/2406.06608).
## Contents

| Prompt Name                                                   | Description                                                                                       |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| [Solo Performance Prompting](#Solo%20Performance%20Prompting) | Elicits reasoning behaviour by simulating a conversation/debate between multiple different people |
| [Plan-and-Solve Prompting](#Plan-and-Solve%20Prompting)       | An improved zero-shot Chain-Of-Thought prompt                                                     |
### Solo Performance Prompting
Elicits reasoning behaviour by simulating a conversation/debate between multiple different people.

Source: [Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration](https://arxiv.org/abs/2307.05300) (with associated git repo https://github.com/MikeWangWZHL/Solo-Performance-Prompting)

```
When faced with a task, begin by identifying the participants who will contribute to solving the task. Then, initiate a multi-round collaboration process until a final solution is reached. The participants will give critical comments and detailed suggestions whenever necessary. 

Here are some examples: 

--- Example Task 1: Use numbers and basic arithmetic operations (+ - * /) to obtain 24. You need to use all numbers, and each number can only be used once. 
Input: 6 12 1 1 

Participants: AI Assistant (you); Math Expert 

Start collaboration! 

Math Expert: Let's analyze the task in detail. You need to make sure that you meet the requirement, that you need to use exactly the four numbers (6 12 1 1) to construct 24. To reach 24, you can think of the common divisors of 24 such as 4, 6, 8, 3 and try to construct these first. Also you need to think of potential additions that can reach 24, such as 12 + 12. 
AI Assistant (you): Thanks for the hints! Here's one initial solution: (12 / (1 + 1)) * 6 = 24 
Math Expert: Let's check the answer step by step. (1+1) = 2, (12 / 2) = 6, 6 * 6 = 36 which is not 24! The answer is not correct. Can you fix this by considering other combinations? Please do not make similar mistakes. 
AI Assistant (you): Thanks for pointing out the mistake. Here is a revised solution considering 24 can also be reached by 3 * 8: (6 + 1 + 1) * (12 / 4) = 24. 
Math Expert: Let's first check if the calculation is correct. (6 + 1 + 1) = 8, 12 / 4 = 3, 8 * 3 = 24. The calculation is correct, but you used 6 1 1 12 4 which is not the same as the input 6 12 1 1. Can you avoid using a number that is not part of the input? 
AI Assistant (you): You are right, here is a revised solution considering 24 can be reached by 12 + 12 and without using any additional numbers: 6 * (1 - 1) + 12 = 24. 
Math Expert: Let's check the answer again. 1 - 1 = 0, 6 * 0 = 0, 0 + 12 = 12. I believe you are very close, here is a hint: try to change the "1 - 1" to "1 + 1". 
AI Assistant (you): Sure, here is the corrected answer: 6 * (1+1) + 12 = 24 
Math Expert: Let's verify the solution. 1 + 1 = 2, 6 * 2 = 12, 12 + 12 = 12. You used 1 1 6 12 which is identical to the input 6 12 1 1. Everything looks good! 

Finish collaboration! 

Final answer: 6 * (1 + 1) + 12 = 24 

--- Example Task 2: Write a poem that meets the following requirements: (1) the poem has seven lines and the first letters of each line forms the word "CHATGPT"; (2) the poem is about explaining what is a quantum computer. (3) the poem needs to be easy to understand by a ten years old kid. 

Participants: AI Assistant (you); Poet; Computer Scientist; Ten year old child 

Start collaboration!

Poet: Make sure that you write the poem with seven lines, and the first letters of the lines should be C, H, A, T, G, P, T. 
Computer Scientist: A quantum computer is an advanced computing device that uses the principles of quantum mechanics to process and store information. Unlike classical computers that use bits to represent information as 0s and 1s, quantum computers use quantum bits or qubits. Qubits can exist in multiple states simultaneously, due to a quantum phenomenon called superposition. You can consider using these information for the poem. 
Ten year old child: I hope the poem to be fun and easy to understanding. I don't want to see a lot of jargons or complicated concepts. 
AI Assistant (you): Thanks for the guidance! Here's my initial attempt at the poem: 
Computational wonder of our age, 
Harnessing the quantum world's strange ways, 
Atoms dance, entwined in dual state, 
Tapping secrets hidden in their haze. 

Grand power to solve, simulate, 
Profound problems that perplex the wise, 
Transforming our future, we await. 

Poet: Let's verify if the poem meets the requirements. The first letters are CHATGPT which is correct! And the poem rhymes well. Good job! 
Computer Scientist: Everything looks good to me! 
Ten year old child: I don't know what does perplex mean. Can you make the use of words easier to understand? 
AI Assistant (you): Sure, let me revise the poem by using more common words. Check out the revised version: 

Curious machine of our time, 
Harnessing the quantum realm's odd ways, 
Atoms play, two states they embrace, 
Taking secrets from their puzzling maze. 

Great power to solve and imitate, 
Problems that confuse the brightest minds, 
Transforming our future, we await. 

Poet: Let's check again if the poem meets the requirements. The first letters are C H A T G P T. And now the poem is more accessible to children. Everything looks good to me. 
Computer Scientist: Looking good! 
Ten year old child: I like this version a lot! 

Finish collaboration! 

Final answer: 
Curious machine of our time, 
Harnessing the quantum realm's odd ways, 
Atoms play, two states they embrace, 
Taking secrets from their puzzling maze. 

Great power to solve and imitate, 
Problems that confuse the brightest minds, 
Transforming our future, we await. 

--- Now, identify the participants and collaboratively solve the following task step by step: 
{{ Task-specific Formating Instruction }} 
Task: {{ Task input }}
```


# Plan-and-Solve Prompting

This is a proposed improvement to the original zero-shot chain-of-thought prompt.

```
Let’s first understand the problem and devise a plan to solve it. Then, let’s carry out the plan and solve the problem step by step
```

Source: [Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://arxiv.org/abs/2305.04091)

## Related
* [LLM Prompting Strategies](LLM%20Prompting%20Strategies.md)
* [CIDI Prompting Strategy](CIDI%20Prompting%20Strategy.md)
* [LLM ReAct Prompting](LLM%20ReAct%20Prompting.md)
* [ChatGPT Prompt Engineering for Developers (DeepLearning.AI course)](ChatGPT%20Prompt%20Engineering%20for%20Developers%20(DeepLearning.AI%20course).md)
* [LLM Chain-of-Thought Prompting](LLM%20Chain-of-Thought%20Prompting.md)
* [How to see the GPT-4 System Prompt](How%20to%20see%20the%20GPT-4%20System%20Prompt.md)

## References
* [The Prompt Report: A Systematic Survey of Prompting Techniques](https://arxiv.org/abs/2406.06608)
* [Unleashing the Emergent Cognitive Synergy in Large Language Models: A Task-Solving Agent through Multi-Persona Self-Collaboration](https://arxiv.org/abs/2307.05300)
* [Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://arxiv.org/abs/2305.04091)