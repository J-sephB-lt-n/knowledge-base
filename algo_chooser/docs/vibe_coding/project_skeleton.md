I'm building a python project which does the following:

1. Has a single page streamlit frontend
2. Allows the user to choose a (large language) model
3. Allows the user to specify a base URL and API key
4. Allows the user to describe a business problem in plain text. The model then evaluates several possible algorithmic solutions to the problem, one at a time. Example solutions are mathematical optimisation, clustering, regression modelling, label propagation, causal modelling etc. The model decides how applicable each possible algorithm is and assigns a single relevance label.
5. As part of the model prompt given to the model, a comprehensive definition of the algorithm is given to the model. These comprehensive algorithm definitions are going to be stored as individual human-readable markdown files in the project (one file per algorithm).
6. Interactions with the large language model must be managed through a wrapper class around the `openai.OpenAI()` client, providing a simplified interface.

Please suggest an ideal folder structure for this project. This code will form part of a large high quality enterprise python codebase which follows established software best practice. If you produce low quality code, I might lose my job.
