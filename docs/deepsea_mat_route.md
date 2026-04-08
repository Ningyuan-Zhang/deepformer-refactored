# DeepSEA MAT Route

## Purpose

This document records the `.mat`-based data route that was established after reconstructing the public DeepSEA dataset.

## Why this route is needed

The current refactored DeepFormer YAML configuration still expects runtime files such as:

- `male.hg19.fasta`
- `distinct_features.txt`
- `sorted_deepsea_data.bed.gz`
- `TF_intervals.txt`

However, the public-data reconstruction workflow produced a different but valid dataset layer:

- `train.mat`
- `valid.mat`
- `test.mat`

Therefore, a separate `.mat`-based route is necessary if we want to make direct use of the reconstructed public dataset.

## Verified MAT file structure

The reconstructed `.mat` files were inspected and found to be HDF5-compatible rather than standard `scipy.io.loadmat` MATLAB files.

### train.mat
- `trainxdata`: shape `(4400000, 1000, 4)`, dtype `uint8`
- `traindata`: shape `(4400000, 919)`, dtype `uint8`

### valid.mat
- `validxdata`: shape `(8000, 1000, 4)`, dtype `uint8`
- `validdata`: shape `(8000, 919)`, dtype `uint8`

### test.mat
- `testxdata`: shape `(455024, 1000, 4)`, dtype `uint8`
- `testdata`: shape `(455024, 919)`, dtype `uint8`

## Interpretation

The reconstructed dataset is already sufficient to support a new direct-loading workflow based on HDF5 `.mat` files. This route avoids dependence on the expired legacy download link and provides a concrete public-data milestone for the refactored project.

## Immediate next step

The immediate next step is to build a lightweight `.mat` loader that:

1. opens the HDF5-compatible `.mat` files with `h5py`;
2. loads sequence inputs and labels lazily;
3. converts each sample to the tensor format expected by a PyTorch sequence model.

## Role in project presentation

This route is important for project presentation because it demonstrates:

- public-data reconstruction from accessible resources;
- successful dataset verification;
- a realistic engineering bridge from raw public data to model-ready input.