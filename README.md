# Useful Algorithms List

When solving a new problem, I like to consult this list in order to identify algorithmic/software tools might be relevant to the problem

* [Algorithms List](#algorithms-list)

* [Learning Resources](#learning-resources)

* [Software Tools](#software-tools)

* [Literature](#literature)

# Algorithms/Fields List 
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
| Shrinkage Estimators (e.g. James Stein)|                          |                           | 
| Supervised Learning                    |                          |                           |
| Survival Analysis                      |                          |                           |
| Topic Modelling (NLP)                  |                          |                           | 

# Learning Resources 

Is Free | Name                    | Description                                            | Link(s)
--------|-------------------------|--------------------------------------------------------|-------------------
Yes     | Awesome Time Series     | A large curated list of time series resources          | https://github.com/lmmentel/awesome-time-series
Yes     | Big Book of R           | A staggeringly large repository of Data Science, Machine-Learning and statistics books | https://www.bigbookofr.com
Yes     | Forecasting: Principles and Practice | A thorough summary of a wide range of time series forecasting topics (with R code) | https://robjhyndman.com/teaching/ or https://otexts.org/fpp3/
Yes     | Google user authentication and password best practice |13 best practices for user account, authentication, and password management | https://cloud.google.com/blog/products/identity-security/account-authentication-and-password-management-best-practices
Yes     | jwt.io                  | Amazing interactive resource for learning about Json Web Tokens (JWTs) | https://jwt.io
Yes     | Made With ML            | Beautifully curated content (with code examples) on the full Data + Machine Learning Pipeline | https://madewithml.com/ | 
Yes     | OWASP                   | A global open organization dedicated to cyber security | https://owasp.org
Yes     | OWASP Cheat Sheet Series| Articles covering massive range of web security topics | https://github.com/OWASP/CheatSheetSeries
Yes     | Tech Interview Handbook |                                                        | https://github.com/yangshun/tech-interview-handbook

# Open Source Software Tools

Name               | Description                                                | Link(s)
-------------------|------------------------------------------------------------|----------
Black              |                                                            |
Commitizen         | For standardizing git commit messages                      | https://github.com/commitizen-tools/commitizen (see also https://www.conventionalcommits.org/en/v1.0.0/)
EGADS              | Open-source Java package to automatically detect anomalies in large scale time-series data | https://github.com/yahoo/egads
Great Expectations |                                                            | https://github.com/great-expectations/great_expectations
HuggingFace        |                                                            | https://huggingface.co
ML Flow            |                                                            |
PyLint             |                                                            |
PyMC               |                                                            |
Scalene            | Python program profiling (for speed/memory optimization)   | https://github.com/plasma-umass/scalene
Scrapy             | Tools for web scraping                                     | https://github.com/scrapy/scrapy 
Tesseract          | Extremely good Optical Character Recognition (OCR) engine  | https://github.com/tesseract-ocr/tesseract  
TS Fresh           | Automatic extraction of relevant features from time series | https://github.com/blue-yonder/tsfresh

# Literature
Name                                  | Description                                                | Link(s)
--------------------------------------|------------------------------------------------------------|----------------
Must-read papers on Recommender System| An extensive curated list of papers on recommender systems | https://github.com/hongleizhang/RSPapers

# Team Git Repo Best Practice

I describe here the **centralized workflow** git strategy (also called [GitHub flow](https://docs.github.com/en/get-started/quickstart/github-flow)), although there are other effective ones. In this strategy, team members work on feature branches which are merged into main when they are completed. 

* Keep the master (main) branch clean. 
        
    - Complete a new feature on a new branch and merge the completed feature into main when is is finished
    
    - Can use [precommit](https://pre-commit.com) and **git hooks** to automatically reject merges of insufficient quality  

* Keep commits atomic - solve one specific task per commit. 

* Avoid long-running branches (these can diverge a lot from main and make merging difficult). Rather make incremental small changes and merge frequently into main.    

* Before merging a new feature branch into main, **git pull origin main** while on the feature branch and resolve conflicts with main on the feature branch

* Make commit messages descriptive, and formalize their structure. A consistent structure makes it much easier to programmatically search your commit history. A tool like [commitizen](https://github.com/commitizen-tools/commitizen) can make this much easier. An example of a message standard is [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)

* Do not allow merges into main without going through a stage of code review



