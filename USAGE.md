# Usage

## 1. Overview

This project reorganizes DeepFormer into a structured repository with separate folders for configuration, model definition, training, evaluation, scripts, utilities, data instructions, and Quarto documentation.

## 2. Intended Workflow

The intended workflow of this repository is:

1. review the repository structure and documentation;
2. prepare a Python environment;
3. prepare the required runtime files under `data/`;
4. verify that configuration files and imports work correctly;
5. run evaluation or prediction-related validation;
6. optionally proceed to full training-oriented reproduction.

## 3. Main Files

### Model
- `models/deepformer.py`

### Training
- `config/train_deepformer.yaml`
- `training/train.py`

### Evaluation
- `config/evaluate_deepformer.yaml`
- `training/evaluate.py`

### Documentation
- `docs/deepformer.qmd`

## 4. Data

The official public data route documented by the original DeepFormer repository is the DeepSEA data bundle:

`http://deepsea.princeton.edu/media/code/deepsea_train_bundle.v0.9.tar.gz`

However, the current refactored runtime configuration expects specific runtime files such as `male.hg19.fasta`, `distinct_features.txt`, `sorted_deepsea_data.bed.gz`, and `TF_intervals.txt`. These files should be prepared externally and placed under `data/` before execution.

## 5. Execution Note

This repository is designed to be structurally complete and documentation-ready. Actual execution depends on a correctly prepared environment and the availability of the required runtime data files.

## 6. Server-Side Recommendation

For practical runtime reproduction, it is recommended to:

- keep editing and documentation work on the local machine;
- use the server mainly for environment setup, data storage, and execution;
- verify imports before running training or evaluation.