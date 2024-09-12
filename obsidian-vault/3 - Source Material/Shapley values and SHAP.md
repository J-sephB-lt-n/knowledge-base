---
created:
  - 2024-09-11T15:00
modified: 2024-09-12 20:15
tags:
  - game-theory
  - shapley
  - shap
  - model-explainability
  - model-interpretability
  - feature-importance
  - machine-learning
  - statistics
type:
  - note
status:
  - completed
---
**_Shapley values_** are a method for fair distribution of payout amongst players in a cooperative game, wheres **_SHAP (SHapley Additive exPlanations)_** refers to a family of algorithmic applications of **_Shapley values_** to explaining the predictions of Machine Learning models.
## Shapley Values
_Shapley Values_ are a concept from Game Theory, named in honour of creator Lloyd Shapley.

In a cooperative game, _Shapley values_ dictate how the payoff/outcome in a cooperative game should be distributed amongst the players when the different players have not contributed equally to the outcome.
The _Shapley value_ guarantees that each player is paid at least as much (at minimum) as they would have been if they had acted alone in the game (not collaborated).

At the highest level, the _Shapley value_ (which describes the relative amount to pay to a particular player) is the average marginal contribution of a player, averaged over every possible combination of players. 

[A famous example of the Shapley value in practice is the airport problem. In the problem, an airport needs to be built in order to accommodate a range of aircraft that require different lengths of runway. The question is how to distribute the costs of the airport to all actors in an equitable manner. The solution is simply to spread the marginal cost of each required length of runway among all the actors needing a runway at least that long. In the end, actors requiring a shorter runway pay less, and those needing a longer runway pay more; however, none of the actors pay as much as they would have if they had chosen not to cooperate.](https://www.investopedia.com/terms/s/shapley-value.asp)

_Shapley values_ are the [unique solution satisfying 4 specific fairness properties](https://en.wikipedia.org/wiki/Shapley_value#Properties).

## SHAP (SHapley Additive exPlanations)
**_SHAP_** applies the concept of _Shapley values_ to the problem of predictive model explainability.

The concept is this:
- The '_game_' is the prediction task for a single instance/example in the dataset
- The '_cooperating players_' in the game are the features (predictive variables) in the model
- The '_gain/payout_' to be apportioned amongst the '_players_' is the model prediction for the instance minus the average prediction over all instances i.e. the difference between the average prediction and this specific instance prediction

The _Shapley value_ (in this context) is calculated as "_the average contribution of a feature value to the prediction, averaged across different feature value combinations (i.e. in the presence of different sets of other feature values)_"

The _Shapley value_ for a specific feature _j_ for a single instance prediction _i_ is calculated as follows:
1. Calculate the marginal effect of feature value _j_ (change in predicted value if feature value _j_ is included vs. excluded) for every possible feature coalition (feature set) - or possibly a sample if all feature coalitions is too computationally intensive.
   '_Not including_' a feature value in a feature coalition (feature set) means giving that feature another random value from another randomly sampled data point.
2. The _Shapley value_ for feature _j_ for instance prediction _i_ is then the average (mean) of the marginal effects calculated in (1) above.

Calculating _Shapley values_ for all instances (or a random sample) for all features facilitates different kinds of global model interpretation.  
## References
* https://christophm.github.io/interpretable-ml-book/shapley.html
* https://en.wikipedia.org/wiki/Shapley_value
* https://www.investopedia.com/terms/s/shapley-value.asp
## Related

* Links to other notes which are directly related go here