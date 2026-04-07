# Data

This repository does not store the full DeepFormer runtime dataset.

## Official Public Data Route

According to the original DeepFormer repository, the official public data route is the DeepSEA training, validation, and testing bundle:

`http://deepsea.princeton.edu/media/code/deepsea_train_bundle.v0.9.tar.gz`

After downloading and extracting this bundle, the original README instructs users to place the three `.mat` files into the `data/` directory.

## Runtime Files Expected by This Refactored Repository

The current configuration files in this refactored project expect the following runtime files:

- `male.hg19.fasta`
- `distinct_features.txt`
- `sorted_deepsea_data.bed.gz`
- `TF_intervals.txt`

These files are not included in the GitHub repository itself and must be prepared externally before runtime execution.

## Practical Note

The public DeepSEA bundle should be treated as the official public starting point for data acquisition. Additional processing or file preparation may still be required in order to match the runtime file names and formats expected by the current configuration files.