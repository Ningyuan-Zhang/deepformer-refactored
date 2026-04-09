# Interpretability Layer Roadmap

## Purpose

This document records the current interpretability-layer position of the DeepFormer refactored project and outlines the next-step roadmap.

## 1. Current status

At the current stage, the project has not yet completed a full interpretability experiment. In particular, it has not yet produced:

- base-level contribution maps as final saved results;
- motif-clustering outputs;
- grammar-level interaction analysis;
- biological validation figures.

Therefore, the interpretability layer should currently be described as **planned and scaffolded**, not fully executed.

## 2. Why interpretability is still relevant now

Even though interpretability outputs have not yet been fully produced, the project has already completed the prerequisite engineering steps needed for future interpretability work:

- a model can be instantiated successfully;
- the forward pass is executable;
- a tiny demo training route exists;
- a demo checkpoint can be saved and reloaded;
- the input route is clearly defined and shape-verified.

This means the project now has a valid starting point for future attribution analysis.

## 3. Planned interpretability progression

The recommended future interpretability workflow for this project is:

### Step 1: base-level contribution analysis
Apply an attribution method such as:

- DeepLIFT
- DeepExplainer

to estimate which input bases contribute most strongly to selected outputs.

### Step 2: motif-level summarization
Transform attribution patterns into motif-like summaries using a tool such as:

- TF-MoDISco

### Step 3: grammar-level analysis
Analyze motif combinations, co-occurrence patterns, spacing, and interaction logic.

### Step 4: validation-oriented interpretation
Compare discovered patterns against known biological expectations when appropriate, or treat them as hypothesis-generating results.

## 4. Planned tool-chain candidates

The current project roadmap considers the following interpretability tools as natural future candidates:

- DeepLIFT
- DeepExplainer
- TF-MoDISco
- Tangermeme or related downstream utilities

These tools are not yet fully integrated, but they define the intended interpretability direction.

## 5. Why this roadmap is already useful

Even without completed interpretability experiments, this roadmap is useful because it:

- clarifies the next technical direction;
- prevents the repository from appearing to stop at raw prediction;
- aligns the project with interpretability-oriented regulatory-genomics workflows;
- makes the repository more comparable to stronger explanatory engineering repositories.

## 6. Current interpretability-layer position

At the current stage, the interpretability layer should be described as:

- conceptually defined;
- technically scaffolded by a runnable model pipeline;
- not yet experimentally completed.

## 7. Recommended one-sentence summary

The current project has not yet completed attribution-to-motif interpretability experiments, but it now has a runnable model and a clearly defined roadmap for future interpretability-layer integration.