# Runtime Gap Analysis

## Purpose

This document explains the current gap between the completed public DeepSEA data reconstruction workflow and the current runtime configuration of the refactored DeepFormer project.

## What has already been completed

The following public-data preparation work has already been completed:

- public DeepSEA-related source files were downloaded;
- compressed source files were decompressed;
- the hg19 reference genome was prepared;
- the DeepSEA reconstruction workflow was executed;
- the following files were generated:
  - `train.mat`
  - `valid.mat`
  - `test.mat`

These files were copied into:

- `data/raw_deepsea/train.mat`
- `data/raw_deepsea/valid.mat`
- `data/raw_deepsea/test.mat`

## What the current runtime configuration expects

The current refactored YAML configuration expects runtime files such as:

- `data/male.hg19.fasta`
- `data/distinct_features.txt`
- `data/sorted_deepsea_data.bed.gz`
- `data/TF_intervals.txt`

Therefore, the reconstructed `.mat` files are not yet direct drop-in replacements for the current configuration.

## Meaning of the current milestone

The reconstructed `.mat` files should be regarded as a completed public-data preparation milestone. They provide:

- a publicly reproducible data route;
- concrete dataset artifacts for demonstration;
- evidence that the data pipeline can be rebuilt without relying on expired private download links.

## Next technical options

There are two realistic next-step directions:

### Option 1: Keep the current runtime configuration and reconstruct the expected runtime files

This route keeps the current YAML structure unchanged and focuses on preparing the expected FASTA / BED / TXT runtime files.

### Option 2: Add a separate `.mat`-based execution route

This route treats the reconstructed `train.mat`, `valid.mat`, and `test.mat` as the primary data artifacts and introduces a dedicated `.mat`-based loading workflow for future execution.

## Recommended interpretation for presentation

For project presentation and repository demonstration, the current public-data reconstruction should be presented as a major completed milestone. The repository is already strong in terms of structure, documentation, public-data reproducibility, and workflow transparency, even though the current YAML runtime path has not yet been fully adapted to the reconstructed `.mat` files.