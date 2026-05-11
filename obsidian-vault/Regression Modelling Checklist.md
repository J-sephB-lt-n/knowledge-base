---
created:
  - 2026-04-29T12:41
modified: 2026-05-06 14:10
tags:
  - regression
  - machine-learning
  - model
  - model-validation
  - model-explainability
  - model-interpretability
type:
  - note
status:
  - in-progress
---
## Assumptions of Linear Regression

1. Linearity of effects of predictors
2. Additivity of effects of multiple predictors
3. Absolute distributional assumptions (parametric regression models assume a distribution for $Y|X$)
4. Relative distributional assumptions

## Handling of Missing Data

What are our assumptions? Are they reasonable?
What are the implications of our approach?
Have we considered removal/imputation?
What is the effect of handling missing data in a different way? Can we fit the model different ways to see?

## Data/Domain understanding

What steps have been taken to explore/understand the data? (was there an Exploratory Data Analysis step?)
What steps have been taken to explore/understand the problem domain?

- Have we explored the predictive/ relationships between the variables prior to starting modelling?

## Data cleanliness

Have we done explicit data quality evaluation?
Have we done explicit data cleaning?
## Flexibility

Does our model allow us to detect complex non-linear and non-additive relationships?
Does our model allow us to detect temporal relationships? (should it?)
## Overfitting

- How are we detecting and preventing overfitting?
- Have we taken steps to identify data leakage? 
	- Checking overly predictive variables before starting formal modelling
	- Looking at the movement of variables over time
- Have we been indulging in "p-hacking"? (trying everything imaginable to find what fits best to the same data we are evaluating ourselves on)
## Measuring Accuracy

- Have we measured accuracy from different angles?
- Have we checked accuracy within different strata?
- Have we compared our model against simple baselines?
- Have we quantified variability? (and also within different strata)
## Model Choice

- How have we settled on a choice of model? What were the decision criteria?
- What alternative models were considered? Why?
- Which models were not considered? Why?

- Does our model choice/paradigm fit the downstream use of the output?
	- Are we doing inference (statistical modelling) or predictive modelling (Machine Learning)?
	- Should we be presenting point estimates or confidence/credibiility intervals?
	- Does the downstream use care more about mean estimates or quantile estimates?
## Causality

Are we falling into the trap of assuming that predictability/association is causality?
## Interpretability

- Have we identified which variables are most "important" (by different measures of important)?
- Can we quantify the effect of different variables on the prediction (can be global or local)
	- Partial dependence plots
- Have we interpreted model behaviour both globally and locally (on aggregate, but also inspecting some different random representative points in the data).
- Have we quantified the uncertainties in our claims drawn from our model?
## Reproducibility

Is our work reproducible?
## Documentation

- Is our code (and approach) well documented? Including explicitly documenting our decisions, reasoning and assumptions.
- Does the documentation match the code?
## References
* [Regression Modelling Strategies (book)](Regression%20Modelling%20Strategies%20(book).md)
## Related
* Links to other notes which are directly related go here