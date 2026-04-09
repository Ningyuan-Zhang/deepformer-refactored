# Methodology Layer Best Practices

## Purpose

This document summarizes methodology-layer best practices for regulatory-genomics sequence modeling projects. The methodology layer focuses on how prediction tasks are defined, how model routes are categorized, how labels are interpreted, and how engineering pipelines are organized for reproducible comparison.

## 1. Task formulation should be explicit

A sequence-modeling project should clearly state what prediction task it is solving. Different task formulations correspond to different modeling traditions and should not be mixed implicitly.

Typical task types include:

- binary peak prediction;
- binned coverage prediction;
- base-resolution profile prediction;
- RNA-seq coverage or multi-readout prediction.

These task types differ in label semantics, model outputs, loss design, and evaluation logic.

## 2. Binary peak route

The binary peak route is the most closely aligned with early sequence-based regulatory-genomics models such as:

- DeepSEA
- Basset
- FactorNet

Typical properties:

- input: one-hot encoded DNA sequence;
- output: multi-label binary vector;
- each target indicates the presence or absence of a regulatory event;
- common loss: binary cross-entropy or equivalent multilabel classification loss.

This route is often the most direct entry point for engineering validation and educational reproduction.

## 3. Binned coverage route

The binned coverage route is more aligned with models such as:

- Basenji
- Enformer
- EPCOT

Typical properties:

- output is not a simple binary peak label;
- labels are coverage-like or aggregated signal values across bins;
- the task captures richer quantitative structure than binary peak classification;
- model outputs and evaluation design are more complex.

This route is important when the goal is to preserve more signal information rather than only peak presence/absence.

## 4. Base-resolution profile route

The base-resolution profile route is aligned with models such as:

- BPNet
- Puffin

Typical properties:

- predictions are made at fine resolution across genomic positions;
- outputs correspond to profile-like signal distributions rather than coarse labels;
- interpretability is often tightly connected to motif-level and base-level attribution.

This route is powerful but generally more demanding in both data preparation and evaluation design.

## 5. RNA-seq / multi-readout route

A multi-readout route, including RNA-seq-style outputs, is associated with models such as:

- Borzoi

Typical properties:

- multiple output channels;
- more complex biological targets;
- greater engineering complexity in label preparation and result interpretation.

## 6. Label-route distinction should be documented

A methodology-layer best-practice project should explicitly state which label route is currently implemented and which routes are only discussed conceptually.

This prevents confusion such as:

- treating a binary-label project as if it were a profile-prediction project;
- claiming coverage-style modeling when only binary peak labels are available;
- mixing engineering demos with benchmark-grade comparisons.

## 7. Engineering demonstration is still meaningful

A project does not need to implement every route at once. A meaningful methodology-layer contribution may still be achieved if the project:

- clearly identifies the implemented route;
- builds a working data loader;
- connects the loader to the model;
- demonstrates forward pass and training behavior;
- explains what is not yet implemented.

This is especially important for refactored educational or prototype repositories.

## 8. Demo routes should be clearly distinguished from benchmark routes

A tiny train or demo evaluation pipeline should not be misrepresented as a full benchmark experiment. Good practice is to explicitly label such pipelines as:

- demo route;
- engineering verification;
- lightweight validation;
- non-benchmark result.

This keeps the repository honest and technically clear.

## 9. Reproducible methodology artifacts

The methodology layer should ideally provide:

- route explanation documents;
- dataset loaders;
- demo subset generation scripts;
- forward-pass test scripts;
- tiny training scripts;
- evaluation scripts;
- concise result summaries.

These artifacts together form a transparent methodology layer even when full paper-level reproduction is not yet complete.

## 10. Practical interpretation for this project

For the current DeepFormer refactored project, the methodology-layer best-practice goal is to:

- identify the correct task family;
- establish a clear executable route;
- connect reconstructed public data to model code;
- validate the route through forward testing, tiny training, and lightweight evaluation;
- distinguish completed engineering milestones from future benchmark work.