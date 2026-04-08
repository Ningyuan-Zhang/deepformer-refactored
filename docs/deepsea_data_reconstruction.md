# DeepSEA Public Data Reconstruction Notes

## Goal

This document records the public-data reconstruction workflow used to obtain DeepSEA-style dataset files for this refactored project.

## Background

The original DeepFormer repository refers to the DeepSEA public data bundle as the official source of training, validation, and testing data. However, the legacy direct download link is no longer reliably accessible. Therefore, this project adopts a public reconstruction workflow based on publicly available source files.

## Reconstruction Route

The reconstruction process was carried out using the public repository:

- `build-deepsea-training-dataset`

The workflow consisted of the following stages:

1. download public DeepSEA-related BED / narrowPeak source files;
2. verify and repair interrupted downloads when necessary;
3. decompress all `.gz` files;
4. download the hg19 chromosome FASTA archive;
5. merge chromosome FASTA files into a single `hg19.fa`;
6. run `build.py` to generate:
   - `train.mat`
   - `valid.mat`
   - `test.mat`

## Output Files

The reconstructed dataset files were copied into:

- `data/raw_deepsea/train.mat`
- `data/raw_deepsea/valid.mat`
- `data/raw_deepsea/test.mat`

These files are not tracked by GitHub because they are large runtime artifacts.

## Verification

After reconstruction, the generated `.mat` files were inspected by loading them with `scipy.io.loadmat` and printing the available keys, shapes, and data types.

A summary of this verification step is saved in:

- `results/deepsea_mat_summary.txt`

## Role in This Project

These reconstructed `.mat` files serve as the public-data reproduction result for the DeepSEA route. They are useful as evidence of successful public-data preparation and as an intermediate dataset layer for future runtime adaptation.

## Important Note

The current refactored DeepFormer configuration still expects runtime files such as:

- `male.hg19.fasta`
- `distinct_features.txt`
- `sorted_deepsea_data.bed.gz`
- `TF_intervals.txt`

Therefore, the reconstructed `.mat` files should currently be regarded as a completed public-data preparation milestone rather than a direct drop-in replacement for the existing YAML runtime configuration.