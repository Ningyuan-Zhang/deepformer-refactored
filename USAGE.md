# Usage

## 1. Overview

This project reorganizes DeepFormer into a structured repository with separate folders for configuration, model definition, training, evaluation, utilities, documentation, and results.

## 2. Basic Workflow

The expected workflow is:

1. prepare the environment
2. prepare runtime data files under `data/`
3. check training and evaluation YAML files
4. run training
5. run evaluation
6. collect outputs under `results/`
7. update documentation in `docs/deepformer.qmd`

## 3. Main Files

### Training
- `config/train_deepformer.yaml`
- `training/train.py`

### Evaluation
- `config/evaluate_deepformer.yaml`
- `training/evaluate.py`

### Model
- `models/deepformer.py`

### Documentation
- `docs/deepformer.qmd`

## 4. Data

This repository does not ship the full training/evaluation datasets.

Required files should be placed under `data/` at runtime, as documented in `data/README.md`.

## 5. Current Limitation

At the current stage, the repository structure and core files are prepared, but actual runtime depends on:

- correct Python environment
- installed dependencies
- prepared DeepFormer data files
- available compute environment