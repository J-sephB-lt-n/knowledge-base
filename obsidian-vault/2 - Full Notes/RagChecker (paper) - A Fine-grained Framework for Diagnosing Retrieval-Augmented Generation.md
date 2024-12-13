---
created:
  - 2024-11-26T15:40
modified: 2024-11-27 10:04
tags:
  - nlp
  - natural-language-processing
  - llm
  - large-language-model
  - eval
  - evaluation
  - metric
  - metrics
  - rag
  - retrieval
  - retrieval-augmented-generation
type:
  - note
status:
  - completed
---
RagChecker is a set of 10 intuitive “diagnostic” metrics designed to provide insight into the performance and behaviour of different parts of a RAG system.

![](../7%20-%20assets/RagChecker/ragchecker_metrics_simplified.png)

These metrics can be used to iteratively improve a system without having to manually inspect model outputs. (or to automatically optimize the RAG system using the metrics in an objection function).

The RagChecker framework involves comparing claims (knowledge triplets) for a single LLM response – the metrics compare between the LLM response, retrieved chunks and known correct answer (ground truth).

Claim extraction, and checking for claims in a given source text, are accomplished using the same system as [RefChecker](RefChecker%20(paper)%20-%20Reference-based%20Fine-grained%20Hallucination%20Checker%20and%20Benchmark%20for%20Large%20Language%20Models.md).

Through their empirical evaluation of the RagChecker framework, the authors also arrived at interesting insights (e.g. into design tradeoffs), and general suggestions for the design and optimization of RAG systems (refer to [the paper](https://arxiv.org/abs/2408.08067)).

The metrics are:
- Overall metrics:
	- [Overall Precision (metric)](#Overall%20Precision%20(metric))
	- [Overall Recall (metric)](#Overall%20Recall%20(metric))
- Retriever Metrics:
	- [Claim Recall (metric)](#Retriever%20Claim%20Recall%20(metric))
	- [Context Precision (metric)](#Retriever%20Context%20Precision%20(metric))
- Generator Metrics:
	- [Generator Faithfulness (metric)](#Generator%20Faithfulness%20(metric))
	- [Generator Hallucination (metric)](#Generator%20Hallucination%20(metric))
	- [Generator Self-Knowledge (metric)](#Generator%20Self-Knowledge%20(metric))
	- [Generator Context Utilisation (metric)](#Generator%20Context%20Utilisation%20(metric))
	- [Generator Relevant Noise Sensitivity (metric)](#Generator%20Relevant%20Noise%20Sensitivity%20(metric))
	- [Generator Irrelevant Noise Sensitivity (metric)](#Generator%20Irrelevant%20Noise%20Sensitivity%20(metric))
## Notation
* Given a query $q$ and documents $D$, the retriever $R$ retrieves top-$k$ relevant context $\{\text{chunk}_j\}=R(q,D,k)$ and the generator $G$ uses the retrieved data $\{\text{chunk}_j\}$ to generate a response $m=G\Big(\{\text{chunk}_j\},q\Big)$
* For a given user (input) query $q$, $gt$ is the "ground truth" response - a complete and correct answer to the question.
* $\{c_i\}$ is a set of claims
	* $\{c_i^{(m)}\}$ is the set of claims in the generator (model) response
	* $\{c_i^{(gt)}\}$ is the set of claims in the ground truth reference
* $\{\text{chunk}_j\}$ is the set of retrieved data
	* $\{\text{r-chunk}_j\}$ is the set of retrieved data each of which contains at least 1 correct claim (i.e. claim entailed in the ground truth reference) i.e. $\exists \space i, \space s.t. c_i^{(gt)} \in \text{chunk}_j$
	* $\{\text{irr-chunk}_j\}$ is the set of retrieved data none of which contain any claims entailed in the ground truth reference  i.e. $\not{\exists} \space i, \space s.t. c_i^{(gt)} \in \text{chunk}_j$
## Overall Precision (metric)
$$\text{Overall Precision} \quad=\quad \displaystyle\frac{\Bigl|\big\{c_i^{(m)}|c_i^{(m)}\in gt\big\}\Bigl|}{\Bigl|\big\{c_i^{(m)}\big\}\Bigl|}$$
![](../7%20-%20assets/RagChecker/individual_metric_diags/overall_precision.png)
## Overall Recall (metric)
$$\text{Overall Recall} \quad=\quad \displaystyle\frac{\Bigl|\big\{c_i^{(gt)}|c_i^{(gt)}\in m\big\}\Bigl|}{\Bigl|\big\{c_i^{(gt)}\big\}\Bigl|}$$
![](../7%20-%20assets/RagChecker/individual_metric_diags/overall_recall.png)
## Retriever Claim Recall (metric)
$$\text{Retriever Claim Recall} \quad=\quad \displaystyle\frac{\Bigl|\big\{c_i^{(gt)}|c_i^{(gt)}\in \{\text{chunk}_j\}\big\}\Bigl|}{\Bigl|\big\{c_i^{(gt)}\big\}\Bigl|}$$
![](../7%20-%20assets/RagChecker/individual_metric_diags/claim_recall.png)
## Retriever Context Precision (metric)
$$\text{Retriever Context Precision} \quad=\quad \displaystyle\frac{\Bigl|\{\text{r-chunk}_j\}\Bigl|}{k}$$
![](../7%20-%20assets/RagChecker/individual_metric_diags/context_precision.png)
## Generator Faithfulness (metric)
$$\text{Generator Faithfulness} \quad=\quad \displaystyle\frac{\Bigl|\big\{c_i^{(m)}|c_i^{(m)}\in\{\text{chunk}_j\}\big\}\Bigl|}{\Bigl|\big\{c_i^{(m)}\big\}\Bigl|}$$
![](../7%20-%20assets/RagChecker/individual_metric_diags/faithfulness.png)
## Generator Hallucination (metric)
$$\text{Generator Hallucination} \quad=\quad \displaystyle\frac{\Bigl|\big\{c_i^{(m)}|c_i^{(m)}\not\in gt, c_i^{(m)}\not\in \{\text{chunk}_j\}\big\}\Bigl|}{\Bigl|\big\{c_i^{(m)}\big\}\Bigl|}$$
![](../7%20-%20assets/RagChecker/individual_metric_diags/hallucination.png)
## Generator Self-Knowledge (metric)
$$\text{Generator Self-Knowledge} \quad=\quad \displaystyle\frac{\Bigl|\big\{c_i^{(m)}|c_i^{(m)}\in gt, c_i^{(m)} \not\in \{\text{chunk}_j\}\big\}\Bigl|}{\Bigl|\big\{c_i^{(m)}\big\}\Bigl|}$$
![](../7%20-%20assets/RagChecker/individual_metric_diags/self_knowledge.png)
## Generator Context Utilisation (metric)
$$\text{Generator Context Utilisation} \quad=\quad \displaystyle\frac{\Bigl|\big\{c_i^{(gt)}|c_i^{(gt)}\in \{\text{chunk}_j\}, c_i^{(gt)}\in m\big\}\Bigl|}{\Bigl|\big\{c_i^{(gt)}|c_i^{(gt)}\in\{\text{chunk}_j\}\big\}\Bigl|}$$
![](../7%20-%20assets/RagChecker/individual_metric_diags/context_utilisation.png)
## Generator Relevant Noise Sensitivity (metric)
$$\text{Generator Relevant Noise Sensitivity} \quad=\quad \displaystyle\frac{\Bigl|\big\{c_i^{(m)}|c_i^{(m)}\not\in gt, c_i^{(m)} \in \{\text{r-chunk}_j\}\big\}\Bigl|}{\Bigl|\big\{c_i^{(m)}\big\}\Bigl|}$$
![](../7%20-%20assets/RagChecker/individual_metric_diags/relevant_noise_sensitivity.png)
The overall framework summary diagram groups [Relevant Noise Sensitivity](#Generator%20Relevant%20Noise%20Sensitivity%20(metric)) and [Irrelevant Noise Sensitivity](#Generator%20Irrelevant%20Noise%20Sensitivity%20(metric)) together for simplicity (into just "Noise Sensitivity"), but the authors found through empirical evaluation that to differentiate between relevant and irrelevant noise sensitivity is useful.
## Generator Irrelevant Noise Sensitivity (metric)
$$\text{Generator Irrelevant Noise Sensitivity} \quad=\quad \displaystyle\frac{\Bigl|\big\{c_i^{(m)}|c_i^{(m)}\not\in gt, c_i^{(m)} \in \{\text{irr-chunk}_j\}\big\}\Bigl|}{\Bigl|\big\{c_i^{(m)}\big\}\Bigl|}$$
![](../7%20-%20assets/RagChecker/individual_metric_diags/irrelevant_noise_sensitivity.png)
The overall framework summary diagram groups [Relevant Noise Sensitivity](#Generator%20Relevant%20Noise%20Sensitivity%20(metric)) and [Irrelevant Noise Sensitivity](#Generator%20Irrelevant%20Noise%20Sensitivity%20(metric)) together for simplicity (into just "Noise Sensitivity"), but the authors found through empirical evaluation that to differentiate between relevant and irrelevant noise sensitivity is useful.

## References
* [(original paper) RagChecker: A Fine-grained Framework for Diagnosing Retrieval-Augmented Generation](https://arxiv.org/abs/2408.08067)
* [(original paper) RefChecker: Reference-based Fine-grained Hallucination Checker and Benchmark for Large Language Models](https://arxiv.org/abs/2405.14486)
## Related
* [RefChecker (paper summary) - Reference-based Fine-grained Hallucination Checker and Benchmark for Large Language Models](RefChecker%20(paper)%20-%20Reference-based%20Fine-grained%20Hallucination%20Checker%20and%20Benchmark%20for%20Large%20Language%20Models.md)