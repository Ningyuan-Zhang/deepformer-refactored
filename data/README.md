# Data

This repository does not include the full DeepFormer training and evaluation datasets.

## Required files at runtime

The following files are expected under `data/` when running training or evaluation:

- `male.hg19.fasta`
- `distinct_features.txt`
- `sorted_deepsea_data.bed.gz`
- `TF_intervals.txt`

## Notes

- These files are required by the configuration files.
- They are not included in this GitHub repository because they are external data files and may be large.
- They should be prepared locally or on the server before running the project.

## Current status

- [ ] Prepare local data files
- [ ] Prepare server data files
- [ ] Verify file paths in YAML configuration