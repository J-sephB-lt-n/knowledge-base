---
created:
  - 2024-09-11T15:00
modified: 2024-09-16 21:13
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
  - in-progress
---
**_Shapley values_** are a method for fair distribution of payout amongst players in a cooperative game, wheres **_SHAP (SHapley Additive exPlanations)_** refers to a family of algorithmic applications of **_Shapley values_** to explaining the predictions of a Machine Learning model.
## Shapley Values
_Shapley values_ are a concept from Game Theory, named in honour of their creator Lloyd Shapley.

In a cooperative game, _shapley values_ dictate how the payoff/outcome in a cooperative game should be distributed amongst the players when the different players have not contributed equally toward achieving that payoff/outcome.
The _shapley value_ for a player _i_ (amount to pay/assign to player _i_) considers the marginal value add by player _i_ across every possible permutation (ordering) of players. 
e.g. for 3 players (where $v(S)$ denotes the value of the coalition/set of players $S$):

| Player arrival order | Marginal value added by player 1              |
| -------------------- | --------------------------------------------- |
| 123                  | $v\big(\{1\}\big)$                            |
| 132                  | $v\big( \{1\} \big)$                          |
| 213                  | $v\Big( \{2,1\} \Big) - v\Big(\{1\}\Big)$     |
| 231                  | $v\Big( \{2,3,1\} \Big) - v\Big(\{2,3\}\Big)$ |
| 312                  | $v\Big( \{3,1\} \Big) - v\Big(\{3\}\Big)$     |
| 321                  | $v\Big( \{3,2,1\} \Big) - v\Big(\{3,2\}\Big)$ |
The _shapley value_ for player 1 in this example is then the average (mean) of these 6 marginal values.
This can be written mathematically as:
$$\begin{array}{lcl}
\underset{\text{shapley value of player }i}{\underbrace{\phi_i(v)}} &=& \displaystyle\frac{1}{n!} \displaystyle{\sum_{S\subseteq N \setminus \{i\}}} |S|! \space\space\big(n-|S|-1\big)! \Big(v\big(S\cup\{i\}\big) - v\big(S\big)\Big) \\ 
S &=& \text{A specific coalition (set) of players} \\
v(S) &=& \text{The worth (value) of coalition } S \\
&\space& v: 2^N \rightarrow \mathbb{R}, \quad v(\emptyset)=0\\
n &=& \text{The total number of players} \\
n! &=& \text{Total number of permutations of all players} \\
N &=& \text{The set of all players (i.e. } S \subseteq N \text{)}\\
\end{array}$$
_Shapley values_ are the only payment rule (mapping) which satisfies the following 4 fairness properties:

|     | Property    | Description                                                                                                                         |
| --- | ----------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Efficiency  | The sum of payouts equals the payout achieved by the coalition containing all players i.e. $\sum_{i\in N} \phi_i(v) = v(N)$         |
| 2   | Symmetry    | Players contributing the same marginal value on all possible coalitions get the same payout                                         |
| 3   | Null player | A player contributing no value always receives a payout of 0                                                                        |
| 4   | Linearity   | For 2 different games with value functions $v$ and $w$,<br>$\phi_i(v+w) = \phi_i(v)+\phi_i(w)$ <br>and<br>$\phi_i(av) = a\phi_i(v)$ |

Other properties of _shapley values_:

| Property               | Description                                                                                                                                                                                                                                                      |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Individual Rationality | $\phi_i(v)\geq v\big(\{i\}\big)$ if $v(S\sqcup T)\geq v(S)+v(T)$<br>i.e. if merging coalitions always achieves more (or the same) than the sum of the individual coalition values, then the payout under the shapley value is at worst the same as playing alone |

[A famous example of the Shapley value in practice is the airport problem. In the problem, an airport needs to be built in order to accommodate a range of aircraft that require different lengths of runway. The question is how to distribute the costs of the airport to all actors in an equitable manner. The solution is simply to spread the marginal cost of each required length of runway among all the actors needing a runway at least that long. In the end, actors requiring a shorter runway pay less, and those needing a longer runway pay more; however, none of the actors pay as much as they would have if they had chosen not to cooperate.](https://www.investopedia.com/terms/s/shapley-value.asp)
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