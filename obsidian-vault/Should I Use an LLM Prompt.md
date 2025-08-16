---
created:
  - 2025-07-01T22:44
modified: 2025-07-08 15:35
tags: 
type: 
status: 
---
I have created this prompt for assessing whether a Large Language Model (or LLM agents, reasoning LLMs, semantic search, BERT etc.) is a suitable solution to a proposed problem.

Here is my prompt: 

```
<problem-description>
Describe your problem here (include whichever of these are useful/relevant). Could also have a back-and-forth with the LLM to refine the problem description. 
- **Title**: give your problem a succinct name
- **Problem Statement**: precisely what is going wrong? (short and to the point, and only observable facts, not opinions). 
- **Background**: what events, data or trends led to this issue?
- **Impact**: who is affected, and what are the business/user costs?
- **Root Cause**: identify the root cause of your problem by continuing to ask "why?" until no further meaningful "why" can be asked (ask "why" at least 5 times). This is designed to elicit the root cause rather than the symptoms.
- **Previous Solutions**: what previous solutions have been attempted? What worked/did not work?
- **Desired State**: what outcome would fully solve the problem? How will success be measured?
- **Stakeholders**: who cares about this? Who decides? Who implements?
- **Scope and Constraints**: what is in/out of scope?
- **Assumptions**: what assumptions are we making about the problem?
- **Risks**: what are known risks surrounding this prolem?
</problem-description>
```

You are helping to evaluate the appropriateness of using Large Language Models within a solution to the problem described. Your task is to fill in `yes` or `no` (in the `Answer`) field for every question in the rubric below.

Please also fill in the `Score` field:
- If `Dimension` is `LLM strength` then `Answer=yes` results in a `Score` of 1 (otherwise 0)
- If `Dimension` is `LLM weakness` then an `Answer` of `yes` results in a `Score` of -1 (otherwise 0)

| Dimension    | Question                                                                                                                        | Answer | Score |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------- | ------ | ----- |
| LLM strength | Will a significant portion of the solution to this problem require the interpretation or generation of natural language (text)? |        |       |
| LLM weakness | Does the solution likely require very low latency (extremely quick responses?)                                                  |        |       |
| LLM strength | Does the solution require summarisation of natural language?                                                                    |        |       |
| LLM weakness | Does the solution require numbers as input or output?                                                                           |        |       |
| LLM strength |                                                                                                                                 |        |       |
| LLM weakness | Is solution explainability important in this problem domain?                                                                    |        |       |

## References

* Links to references (source material) go here
## Related

* Links to other notes which are directly related go here