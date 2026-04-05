# DeepFormer Refactored

This repository is a refactored DeepFormer project organized in a unified engineering style.

## Project Goal

The goal of this project is to:

- read and understand the DeepFormer model
- reorganize the original repository into a cleaner project structure
- prepare training and evaluation pipelines
- document the model in QMD format
- support future reproduction on a local machine or server

## Repository Structure

- `config/`：training and evaluation configuration files
- `data/`：data instructions and expected runtime file locations
- `docs/`：QMD documentation
- `models/`：model definition
- `results/`：training and evaluation outputs
- `scripts/`：helper scripts
- `training/`：training and evaluation entry points
- `utils/`：utility functions
- `README.md`：project overview
- `USAGE.md`：usage instructions
- `requirements.txt`：dependency list
- `run_example_pipeline.sh`：example pipeline script

## Current Status

- [x] project structure initialized
- [x] training configuration prepared
- [x] evaluation configuration prepared
- [x] model skeleton migrated
- [x] training entry prepared
- [x] evaluation entry prepared
- [x] data instructions prepared
- [ ] environment setup
- [ ] runtime data preparation
- [ ] local/server execution test
- [ ] reproduction results
- [ ] final documentation polish

## Notes

This repository does not include the full external DeepFormer datasets.

The `data/` directory only documents the required runtime files.  
Actual data files should be prepared locally or on the server before running training or evaluation.