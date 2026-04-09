# Demo Evaluation

## Purpose

This document records the lightweight evaluation stage built on top of the DeepSEA MAT-route demo pipeline.

## Evaluation setting

The evaluation is not intended to be a full benchmark experiment. Instead, it is a lightweight engineering validation stage designed to confirm that:

1. the reconstructed public-data route can be loaded correctly;
2. the DeepFormer demo model can be restored from a saved checkpoint;
3. the model can produce valid outputs on the demo validation subset;
4. basic loss and prediction statistics can be computed successfully.

## Inputs

The evaluation stage uses:

- validation demo subset:
  - `data/raw_deepsea/demo_subset/valid_demo_256.npz`
- demo checkpoint:
  - `results/deepformer_demo_model.pt`

## Evaluation outputs

The demo evaluation script reports:

- average validation loss;
- average binary accuracy;
- output tensor shape;
- target tensor shape;
- first-batch prediction mean;
- first-batch prediction standard deviation;
- first-batch target mean.

## Interpretation

This stage should be interpreted as a lightweight engineering evaluation rather than a paper-level biological benchmark. Its main value is to confirm that the reconstructed MAT-route has already been connected to a working model checkpoint and that the complete demo pipeline now includes both training and evaluation.

## Project significance

With this evaluation stage added, the project now supports the following complete demo workflow:

public data reconstruction -> MAT verification -> demo subset generation -> DataLoader test -> model forward -> tiny demo training -> checkpoint saving -> demo evaluation