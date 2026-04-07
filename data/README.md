# Data

This repository does not store the full DeepFormer runtime dataset.

## Public Data Route

The original DeepFormer repository refers to the DeepSEA public data bundle. Since the legacy direct download link is no longer reliably available, this project uses the DeepSEA public-data reconstruction route as the practical public alternative.

The expected final dataset files are:

- `train.mat`
- `valid.mat`
- `test.mat`

These files can be reconstructed from publicly available metadata, BED files, and the hg19 reference genome using the DeepSEA reconstruction workflow.

## Runtime Files Expected by This Refactored Repository

The current configuration files in this refactored project expect the following runtime files:

- `male.hg19.fasta`
- `distinct_features.txt`
- `sorted_deepsea_data.bed.gz`
- `TF_intervals.txt`

These files are not included in the GitHub repository itself and must be prepared externally before runtime execution.

## Practical Note

The public DeepSEA bundle should be treated as the official public starting point for data acquisition. Additional processing or file preparation may still be required in order to match the runtime file names and formats expected by the current configuration files.