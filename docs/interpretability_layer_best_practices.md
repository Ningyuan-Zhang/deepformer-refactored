# Interpretability Layer Best Practices

## Purpose

This document summarizes interpretability-layer best practices for regulatory-genomics sequence modeling projects.

## 1. Why interpretability matters

In regulatory-genomics sequence models, predictive performance alone is often not sufficient. A strong project should also ask:

- which sequence positions drive the prediction;
- which motif-like patterns are being used;
- whether combinations of motifs form recognizable grammar;
- whether the learned patterns agree with known biology or at least form testable hypotheses.

Therefore, interpretability should be treated as a major layer rather than a minor optional extra.

## 2. A common interpretability progression

A practical interpretability progression often follows this order:

1. base-level contribution;
2. motif extraction;
3. motif grammar or pattern interaction;
4. hypothesis-driven validation.

This progression helps turn model internals into biologically interpretable structure.

## 3. Base-level attribution

The first interpretability step is often to assign importance scores to input bases. Common attribution tools include:

- DeepLIFT
- DeepExplainer
- gradient-based variants

These methods aim to estimate which bases most strongly influence the model output.

## 4. Motif discovery from importance signals

Base-level attribution scores are often not directly the final interpretability target. Instead, they can be used to extract recurrent sequence patterns or motif-like signatures.

A widely used downstream tool is:

- TF-MoDISco

This type of step groups local contribution patterns into reusable motif-level summaries.

## 5. Grammar-level interpretation

After motif-like patterns are identified, a stronger project may investigate higher-level relationships such as:

- motif co-occurrence;
- spacing preferences;
- orientation constraints;
- combinatorial logic.

This stage is often referred to as motif grammar or regulatory grammar analysis.

## 6. Validation-oriented interpretation

Interpretability should not stop at generating pretty patterns. Good practice includes:

- checking whether recovered patterns are stable;
- comparing patterns against known motif databases when appropriate;
- using perturbation or in silico mutagenesis to test whether discovered patterns matter functionally.

## 7. Tool-chain transparency

A good interpretability-layer project should clearly document:

- which attribution method is used;
- what model output is being explained;
- what input representation is being explained;
- how importance maps are transformed into motif-level outputs;
- where resulting figures and summaries are stored.

## 8. Interpretability should be honest about project stage

A project should not claim full biological interpretability if it has only completed preliminary engineering preparation. It is acceptable to state that:

- interpretability tools are planned;
- interface points are identified;
- result directories are prepared;
- full interpretability experiments remain future work.

This is better than overstating incomplete results.

## 9. Recommended artifacts for an interpretability-ready repository

A repository that wants to be interpretability-ready should ideally provide:

- an interpretability overview document;
- planned tool-chain description;
- placeholder scripts or interfaces for attribution;
- clear output directories for interpretability results;
- a roadmap describing future interpretability experiments.

## 10. Practical interpretation for this project

For the current DeepFormer refactored project, the interpretability-layer best-practice goal is to define a clear future path from:

demo-executable model -> attribution method -> motif-level summary -> grammar-level analysis -> biological interpretation

Even if full interpretability experiments are not yet completed, the project should still make the future interface and intended workflow explicit.