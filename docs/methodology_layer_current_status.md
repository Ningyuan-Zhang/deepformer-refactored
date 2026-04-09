# Methodology Layer Current Status

## Purpose

This document records the current methodology-layer status of the DeepFormer refactored project.

## 1. Current task route

At the current stage, the project is most closely aligned with the **binary peak-style route**.

Reasons:

- the reconstructed dataset is organized as sequence input plus multi-label targets;
- the model-facing input uses one-hot-like sequence encoding with shape `(1000, 4)`;
- the target dimension is `919`;
- the demo training route uses a binary cross-entropy loss.

Therefore, the current executable engineering route is best understood as a binary-label sequence-modeling route rather than a coverage-based or base-resolution profile route.

## 2. What has been completed

### 2.1 MAT-route establishment

A separate `.mat`-based route was established after reconstructing the public dataset. This was necessary because the current YAML runtime path still expects a different FASTA / BED / TXT file family.

### 2.2 Loader implementation

A dedicated HDF5-compatible MAT loader was implemented. The loader can:

- open reconstructed MAT files;
- lazily access sequence inputs and labels;
- convert the input from `(1000, 4)` to `(4, 1000)` for PyTorch-style model execution.

### 2.3 Demo subset route

A lightweight `.npz` demo-subset route was established to support rapid testing and presentation.

This step made it possible to perform:

- dataset loader tests;
- forward-pass validation;
- tiny demo training;
- lightweight demo evaluation.

### 2.4 DeepFormer forward validation

The project successfully connected the demo data route to the refactored DeepFormer model and verified that a valid forward pass could be executed.

### 2.5 Tiny training route

A tiny demonstration training pipeline was completed. This confirmed that:

- the model could receive inputs from the demo route;
- optimization could proceed;
- training loss could be computed and updated;
- a demo checkpoint could be saved.

### 2.6 Lightweight evaluation route

A lightweight evaluation stage was added on top of the demo checkpoint. This confirmed that:

- the checkpoint could be reloaded successfully;
- the validation demo subset could be processed;
- validation loss and simple prediction statistics could be computed.

---

## 3. What this project has achieved at the methodology layer

The current project has already achieved a meaningful methodology-layer milestone because it now supports a complete demo executable chain:

public reconstructed data -> MAT verification -> demo subset -> dataset loader -> model forward -> tiny training -> checkpoint saving -> demo evaluation

This is already substantially stronger than a repository that only contains code structure without a verified executable route.

---

## 4. What has not yet been fully completed

### 4.1 Peak vs coverage comparison is not yet implemented

The current project does not yet provide a paired comparison between:

- a binary peak route, and
- a coverage-style route

for the same data source.

Therefore, the project currently demonstrates one task formulation rather than a full task-family comparison.

### 4.2 Other methodology routes are not yet executed

The project does not yet implement:

- binned coverage route;
- base-resolution profile route;
- RNA-seq / multi-readout route

as executable pipelines within the current repository.

### 4.3 Full benchmark-grade training is not yet done

The current training route is intentionally lightweight and demo-oriented. It is sufficient for engineering validation, but not yet equivalent to a full benchmark experiment or paper-level reproduction.

---

## 5. Why the current methodology-layer status is still meaningful

Even though the project currently focuses on one executable route, the methodology layer is already meaningful because it demonstrates:

- correct route identification;
- successful engineering connection between reconstructed data and model code;
- working forward, training, and evaluation scripts;
- a clear boundary between completed work and future expansion.

For a presentation-ready engineering project, this is already a strong methodology-layer result.

---

## 6. Current methodology-layer position

At the current stage, the methodology layer should be described as:

- executable;
- route-specific;
- engineering-validated;
- demo-complete;
- not yet expanded into a multi-route benchmark framework.

---

## 7. Recommended one-sentence summary

The methodology layer of the current project has already established a complete executable binary-peak-style demo pipeline for DeepFormer, while broader coverage/profile task comparisons remain future work.