# DeepFormer Refactored

This repository is a refactored DeepFormer project organized in a unified engineering style.

## Project Goal

The goal of this project is to:

- study and explain the DeepFormer model
- reorganize the original repository into a clearer engineering structure
- prepare configuration files, model code, training entry points, and evaluation entry points
- document the project in Quarto (`.qmd`) format
- support future runtime validation and reproduction on a server environment

## Repository Structure

- `config/`: training and evaluation configuration files
- `data/`: data instructions and runtime data placeholders
- `docs/`: Quarto documentation
- `models/`: model definition
- `results/`: runtime outputs
- `scripts/`: helper scripts
- `training/`: training and evaluation entry points
- `utils/`: utility functions
- `README.md`: project overview
- `USAGE.md`: usage guide
- `requirements.txt`: dependency list
- `run_example_pipeline.sh`: example pipeline script

## Model Overview

DeepFormer is a hybrid neural network for DNA sequence function prediction. According to the original repository, it combines convolutional neural networks with a linear attention mechanism and achieves strong performance on the DeepSEA benchmark.

## Dependencies

The original DeepFormer repository specifies the following recommended environment:

- Python 3.9
- selene-sdk 0.4.4
- einops 0.5.0
- pytorch 1.7.1
- torchvision 0.8.2
- torchaudio 0.7.2

This refactored repository records the same dependency direction, while the actual runtime environment may require practical adjustments depending on the server setup.

## Data Source

The original DeepFormer repository points to the public DeepSEA training bundle as the official data source. However, the legacy direct download link is no longer reliably accessible. Therefore, in this refactored project, the DeepSEA dataset should be treated as an externally reconstructed dataset based on publicly available resources.

A practical public alternative is to rebuild the DeepSEA-style `train.mat`, `valid.mat`, and `test.mat` files using the public reconstruction workflow described in the `build-deepsea-training-dataset` project.

## Required Runtime Files in This Refactored Project

The current configuration files in this refactored repository expect the following runtime data files:

- `data/male.hg19.fasta`
- `data/distinct_features.txt`
- `data/sorted_deepsea_data.bed.gz`
- `data/TF_intervals.txt`

Therefore, the public DeepSEA bundle should be understood as the public starting point for data acquisition, while additional runtime file preparation may still be required before full execution.

## Recommended Reproduction Scope

For the current refactored project, the recommended scope is:

1. use the public DeepSEA bundle as the official data source;
2. keep the repository structure, documentation, and engineering layout complete and reproducible;
3. treat runtime execution as a follow-up step that depends on preparing the expected runtime files under `data/`.

## Main Execution Entry Points

### Training
- configuration: `config/train_deepformer.yaml`
- entry point: `training/train.py`

### Evaluation
- configuration: `config/evaluate_deepformer.yaml`
- entry point: `training/evaluate.py`

## Notes

This repository is intended to serve both as a refactored reproduction scaffold and as a structured learning resource for understanding DeepFormer, configuration-driven sequence modeling, and repository organization.