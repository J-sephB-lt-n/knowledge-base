# Knowledge Base

Whenever I discover something interesting or useful, but is too small to be it's own project, then I put it into here.

I've put the sections links in a disordered heap to make serendipity more likely:

[Association, Bias & Causation](#association-bias--causation), [Algorithms list](#algorithms-list), [Database Normalisation (incomplete)](#database-normalisation), [Kelly Criterion](#the-kelly-criterion), [Learning Resources](#learning-resources), [Cool open-source software tools](#cool-open-source-software-tools), [useful bash terminal commands](#useful-bash-terminal-commands), [useful regex patterns](#useful-regex-patterns), [open-source data annotation tools](#open-source-data-annotation-tools)

# Algorithms List 
| Name                                   | Description              | Example Use Cases         | Useful Resources
|----------------------------------------|--------------------------|---------------------------|------------------
| Anomaly Detection                      |                          | payment fraud detection   | https://scikit-learn.org/stable/modules/outlier_detection.html 
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
| Retrival-Augmented Generation (RAG)    |                          |                           |
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

# Cool Open Source Software Tools

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

# Useful Bash Terminal Commands

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


## Association, Bias & Causation

```math
$$\begin{array}{lcl}
\underbrace{E\Big[Y\Bigl|T=1\Big] - E\Big[Y\Bigl|T=0\Big]}_{
    \substack{ \text{Difference between} \\ \text{treatment group means} } 
    }
    &=& 
    \underbrace{E\Big[Y(1)-Y(0)\Bigl|T=1\Big]}_{
    \substack{\text{Average Treatment effect} \\ \text{on the Treated (ATT)} }} + 
    \underbrace{\Bigg(E\Big[Y(0)\Bigl|T=1\Big]-E\Big[Y(0)\Bigl|T=0\Big]\Bigg)}_{
        \text{Selection Bias}
        } \\
\space &\space& \space \\
Y_i &=& \text{outcome of interest (on individual } i)\\
T_i &=& \begin{cases}1 \quad \text{if individual } i \text{ received treatment} \\
0 \quad \text{if individual } i \text{ did not receive treatment}\end{cases} \\
Y_i(1) &=& \text{outcome which would have been observed for individual } i \text{ if they had received the treatment} \\
Y_i(0) &=& \text{outcome which would have been observed for individual } i \text{ if they had NOT received the treatment} \\
\end{array}$$
```

Here is a simulation in python showing this to be true:
```python
import random
import statistics

N_INDIVIDUALS: int = 100_000
random.seed(69)

untreated_prob_of_dying: list[float] = [
    random.uniform(0, 1) for _ in range(N_INDIVIDUALS)
]
treated_prob_of_dying: list[float] = [
    # treatment halves probability of death #
    0.5 * p
    for p in untreated_prob_of_dying
]
assigned_treatment_group: list[str] = [
    # biased by probability of dying #
    random.choices(["treated", "untreated"], weights=(p, 1 - p))[0]
    for p in untreated_prob_of_dying
]
prob_of_dying: list[float] = [
    (
        untreated_prob_of_dying[idx]
        if treat_grp == "untreated"
        else treated_prob_of_dying[idx]
    )
    for idx, treat_grp in enumerate(assigned_treatment_group)
]
mean_prob_of_dying_treated_group: float = statistics.mean(
    [
        prob_of_dying[idx]
        for idx, treat_grp in enumerate(assigned_treatment_group)
        if treat_grp == "treated"
    ]
)
mean_prob_of_dying_untreated_group: float = statistics.mean(
    [
        prob_of_dying[idx]
        for idx, treat_grp in enumerate(assigned_treatment_group)
        if treat_grp == "untreated"
    ]
)
att: float = statistics.mean(
    [
        (treated_prob_of_dying[idx] - untreated_prob_of_dying[idx])
        for idx, treat_grp in enumerate(assigned_treatment_group)
        if treat_grp == "treated"
    ]
)
selection_bias: float = statistics.mean(
    [
        untreated_prob_of_dying[idx]
        for idx, treat_grp in enumerate(assigned_treatment_group)
        if treat_grp == "treated"
    ]
) - statistics.mean(
    [
        untreated_prob_of_dying[idx]
        for idx, treat_grp in enumerate(assigned_treatment_group)
        if treat_grp == "untreated"
    ]
)

print(
    f"""
                      E[Y|T=1] - E[Y|T=0] = {(mean_prob_of_dying_treated_group - mean_prob_of_dying_untreated_group):.5f}
                     ATT + selection_bias = {(att + selection_bias):.5f} 

                    ATT: E[Y(1)-Y(0)|T=1] = {att:.5f}
Selection Bias: E[Y(0)|T=1] - E[Y(0)|T=0] = {selection_bias:.5f}
"""
)
```
```
                      E[Y|T=1] - E[Y|T=0] = 0.00176
                     ATT + selection_bias = 0.00176 

                    ATT: E[Y(1)-Y(0)|T=1] = -0.33341
Selection Bias: E[Y(0)|T=1] - E[Y(0)|T=0] = 0.33516
```

## Database Normalisation

```<this section is still under construction>```

### 1st Normal Form

To be in first normal form, each table cell must contain a single value (e.g. not anything like an array, json or nested table within the cell).

Example: Not in first normal form:

| Name     | Skills
|----------|-----------
| Joe      | python,unicyling,piano 
| Napoleon | nunchuck,bow hunting,computer hacking

Example: In first normal form:

| Name | Skill
|------|--------------
| Joe  | python
| Joe  | unicyling
| Joe  | piano 
| Napoleon | nunchuck
| Napoleon | bow hunting
| Napoleon | computer hacking

### Database Normalisation: 2nd Normal Form



### Database Normalisation: 3rd Normal Form


## The Kelly Criterion 

The [Kelly Criterion](https://en.wikipedia.org/wiki/Kelly_criterion) (or [Kelly Strategy](https://en.wikipedia.org/wiki/Kelly_criterion)) is a result from probability theory. In a specific repeated game (which resembles some gambling games and investment scenarios), it is the strategy achieving maximum gain/reward in the long run. 

The formulation is as follows:

In a single game:

* The player invests (risks) $100r\%$ of their total assets/portfolio/wealth $A$. 

* With probability $w$, they earn a return of $100g\%$ on their investment/risk. i.e. $A_{t+1}=A_t(1+rg)$ 

* With probability $1-w$, they lose $100b\%$ of their investment/risk. i.e. $A_{t+1}=A_t(1-rb)$

After playing $n$ consecutive games, the expected value of their total assets/portfolio/wealth is:

$$P_n \quad=\quad A_0(1+rg)^{wn}(1-rb)^{(1-w)n}$$

The value of $r$ maximizing $P_n$ can be found by solving the equation 

$$\frac{d}{d r}\frac{log(P_n)}{n} \quad=\quad 0$$

The solution is:

$$arg\space max_r\space P_n \quad=\quad \displaystyle\frac{w}{b} - \frac{1-w}{g}$$