# Useful Algorithms List

When solving a new problem, I like to consult this list in order to identify algorithmic/software tools might be relevant to the problem

* [Algorithms List](#algorithms-list)

* [Learning Resources](#learning-resources)

* [Software Tools](#software-tools)

* [Literature](#literature)

* [Useful Linux Commands](#useful-linux-commands)

* [Useful Regex Patterns](#useful-regex-patterns)

# Algorithms List 
| Name                                   | Description              | Example Use Cases         | Useful Resources
|----------------------------------------|--------------------------|---------------------------|------------------
| Anomaly Detection                      |                          |                           |
| Bayesian Hierarchical Modelling        |                          |                           | 
| Bayesian Networks                      |                          |                           |  
| Causal (decision) Bayesian Networks    |                          |                           |
| Clustering                             |                          |                           | 
| Collaborative Filtering                |                          |                           | 
| Computer Vision: Image Classification  |                          |                           | https://huggingface.co/models
| Computer Vision: Image Segmentation    |                          |                           | https://huggingface.co/models
| Computer Vision: Object Detection      |                          |                           | https://huggingface.co/models
| Confidence/Credibility Intervals       |                          |                           | 
| Data Drift                             |                          |                           | see also: "Population Stability Index" (PSI), "KL Divergence"
| Dimension Reduction                    |                          |                           | 
| Document Question Answering            |                          |                           | https://huggingface.co/models
| Hypothesis Testing                     |                          |                           | 
| Image Generation (image variation)     |                          |                           | https://huggingface.co/models
| Image Generation (text prompt)         |                          |                           | https://huggingface.co/models
| Knowledge Graphs                       |                          |                           | 
| Mathematical Optimisation              |                          |                           | 
| Multi-Armed Bandit Algorithms          |                          |                           | 
| Optical Character Recognition (OCR)    | Read text from an image  |                           | https://github.com/kba/awesome-ocr (the [tesseract](https://github.com/tesseract-ocr/tesseract) engine is amazing)
| Sequential Hypothesis Testing          | Cost-effective experimentation through valid early stopping |                           | https://en.wikipedia.org/wiki/Sequential_analysis
| Shrinkage Estimators (e.g. James Stein)|                          |                           | 
| Supervised Learning                    |                          |                           |
| Survival Analysis                      |                          |                           |
| Topic Modelling (NLP)                  |                          |                           | 

# Learning Resources 

| Is Free | Name                    | Description                                            | Link(s)
|---------|-------------------------|--------------------------------------------------------|-------------------
| Yes     | Awesome Time Series     | A large curated list of time series resources          | https://github.com/lmmentel/awesome-time-series
| Yes     | Big Book of R           | A staggeringly large repository of Data Science, Machine-Learning and statistics books | https://www.bigbookofr.com
| Yes     | Causal Inference: The Mixtape| (book) Modeling techniques for causal inference   | https://mixtape.scunning.com/
| Yes     | The Effect              | (book) An Introduction to Research Design and Causality| https://theeffectbook.net/
| Yes     | Forecasting: Principles and Practice | A thorough summary of a wide range of time series forecasting topics (with R code) | https://robjhyndman.com/teaching/ or https://otexts.org/fpp3/
| Yes     | Google user authentication and password best practice |13 best practices for user account, authentication, and password management | https://cloud.google.com/blog/products/identity-security/account-authentication-and-password-management-best-practices
| Yes     | jwt.io                  | Amazing interactive resource for learning about Json Web Tokens (JWTs) | https://jwt.io
| Yes     | Made With ML            | Beautifully curated content (with code examples) on the full Data + Machine Learning Pipeline | https://madewithml.com/ | 
| Yes     | OWASP                   | A global open organization dedicated to cyber security | https://owasp.org
| Yes     | OWASP Cheat Sheet Series| Articles covering a large range of web security topics | https://github.com/OWASP/CheatSheetSeries
| Yes     | OWASP Web Security Testing Guide | Guide to assessing the security of a web application | https://github.com/OWASP/wstg
| Yes     | Relational Database Normalisation | A very clear explanation of the first 5 normal forms | https://www.youtube.com/watch?v=GFQaEYEc8_8
| Yes     | RestfulAPI.net          | A wealth of information on REST API architecture and design | https://restfulapi.net/
| Yes     | Tech Interview Handbook |                                                        | https://github.com/yangshun/tech-interview-handbook

# Open Source Software Tools

| Name               | Description                                                | Link(s)
|--------------------|------------------------------------------------------------|----------
| Black              | Auto-formatting (standardization) of python code           |
| Commitizen         | For standardizing git commit messages                      | https://github.com/commitizen-tools/commitizen (see also https://www.conventionalcommits.org/en/v1.0.0/)
| DuckDB             |                                                            |
| EGADS              | Open-source Java package to automatically detect anomalies in large scale time-series data | https://github.com/yahoo/egads
| Great Expectations |                                                            | https://github.com/great-expectations/great_expectations
| HuggingFace        |                                                            | https://huggingface.co
| ML Flow            | For managing Machine Learning models in production         |
| PyLint             | For automatic assessment of python code quality            |
| PyMC               | For bayesian modelling in python                           |
| Scalene            | Python program profiling (for speed/memory optimization)   | https://github.com/plasma-umass/scalene
| Sci-Kit Learn      | Established python Machine Learning framework              |
| Scrapy             | Established python framework for web scraping              | https://github.com/scrapy/scrapy 
| SQLite             | In-file SQL database                                       |
| Tesseract          | Extremely good Optical Character Recognition (OCR) engine  | https://github.com/tesseract-ocr/tesseract  
| TS Fresh           | Automatic extraction of relevant features from time series | https://github.com/blue-yonder/tsfresh

# Open-Source Data Annotation Tools
| Name                  | Description                                          | Link(s)
|-----------------------|------------------------------------------------------|------------------
| Brat                  | online environment for collaborative text annotation | https://brat.nlplab.org
| Docanno               |                                                      | https://github.com/doccano/doccano 
| Prodigy               |                                                      | https://prodi.gy
| INCEpTION             |                                                      | https://inception-project.github.io

# Literature
Name                                  | Description                                                | Link(s)
--------------------------------------|------------------------------------------------------------|----------------
Must-read papers on Recommender System| An extensive curated list of papers on recommender systems | https://github.com/hongleizhang/RSPapers

# Useful Linux Commands

| Task                                                            | Command
|-----------------------------------------------------------------|----------------------
| Convert hex string to utf-8                                     | <code>echo 54657374696e672031203220330 &#124; xxd -r -p</code>
| Find files by name (using regex)                                | ```find . -name "*.sql"```
| Remove all occurences of __pycache__ folder                     | ```find . -type d -name __pycache__ -exec rm -r {} \+```
| Replace text within a file (```/g``` replaces all occurences)   | ```sed -i "s/text_to_find/text_to_replace_with/g" myfile.txt``` (i.e. same syntax as ```:s``` in [vim](https://www.vim.org/))
| Search for text within multiple files (within multiple folders) | ```grep -r "search_string" /path/to/base/folder```

# Useful Regex Patterns
| Pattern                         | Explanation
|---------------------------------|-------------------
| ^\w[\w\.\-]+@(\w+\.)+[\w]{2,4}$ | Basic email address validation
