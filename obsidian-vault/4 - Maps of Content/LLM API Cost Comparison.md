---
created:
  - 2025-01-30T09:25
modified: 2025-02-02 20:42
tags:
  - llm
  - large-language-model
  - cost
  - tokenisation
  - gpt
  - llama
  - nlp
  - optimisation
  - choice
  - choosing
type:
  - map-of-content
status:
  - ongoing
---
This is my own tracking of cost of Large Language Model inference under different API services which I use
(500 words is approximately the amount fitting onto an A4 page with reasonable margins and spacing):

| Last updated | Model                   | Provider  | Token Type | 1m tokens | 667 tokens (~500 words) | Relative Cost                                   |
| ------------ | ----------------------- | --------- | ---------- | --------- | ----------------------- | ----------------------------------------------- |
| 2025-Jan     | GPT-4o                  | OpenAI    | Input      | $2.5      | $0.00166750             | `*****`                                         |
| 2025-Jan     | GPT-4o                  | OpenAI    | Output     | $10       | $0.00667000             | `***************`<br>`*******`                  |
| 2025-Jan     | GPT-4o mini             | OpenAI    | Input      | $0.15     | $0.00010005             |                                                 |
| 2025-Jan     | GPT-4o mini             | OpenAI    | Output     | $0.6      | $0.00040020             | `*`                                             |
| 2025-Jan     | Claude 3.5 Sonnet       | Anthropic | Input      | $3        | $0.00200100             | `******`                                        |
| 2025-Jan     | Claude 3.5 Sonnet       | Anthropic | Output     | $15       | $0.01000500             | `***************`<br>`***************`<br>`***` |
| 2025-Jan     | Claude 3 Haiku (legacy) | Anthropic | Input      | $0.25     | $0.00016675             |                                                 |
| 2025-Jan     | Claud  3 Haiku (legacy) | Anthropic | Output     | $1.25     | $0.00083375             | `**`                                            |
| 2025-Jan     | Gemini 1.5 Flash        | Google    | Input      | $0.075    | $0.000050025            |                                                 |
| 2025-Jan     | Gemini 1.5 Flash        | Google    | Output     | $0.3      | $0.00020010             |                                                 |
| 2025-Jan     | Gemini 1.5 Pro          | Google    | Input      | $1.25     | $0.00083375             | `**`                                            |
| 2025-Jan     | Gemini 1.5 Pro          | Google    | Output     | $5        | $0.00333500             | `***********`                                   |

## References
* https://openai.com/api/pricing/
* https://www.anthropic.com/pricing#anthropic-api
* https://ai.google.dev/pricing
## Related
* Links to other notes which are directly related go here