# Data Layer Current Status

## Purpose

This document records the current data-layer status of the DeepFormer refactored project.

## 1. What has already been completed

### 1.1 Public-data route reconstruction

The original legacy public DeepSEA direct-download route was no longer reliably accessible. Therefore, a public reconstruction workflow was adopted.

Using publicly accessible source files and the hg19 reference genome, the project successfully reconstructed the following dataset files:

- `train.mat`
- `valid.mat`
- `test.mat`

These files were copied into:

- `data/raw_deepsea/train.mat`
- `data/raw_deepsea/valid.mat`
- `data/raw_deepsea/test.mat`

### 1.2 MAT-format verification

The reconstructed `.mat` files were inspected and confirmed to be HDF5-compatible rather than standard `scipy.io.loadmat` MATLAB files.

Verified structure:

#### train.mat
- `trainxdata`: `(4400000, 1000, 4)`, `uint8`
- `traindata`: `(4400000, 919)`, `uint8`

#### valid.mat
- `validxdata`: `(8000, 1000, 4)`, `uint8`
- `validdata`: `(8000, 919)`, `uint8`

#### test.mat
- `testxdata`: `(455024, 1000, 4)`, `uint8`
- `testdata`: `(455024, 919)`, `uint8`

### 1.3 Demo subset generation

To support lightweight debugging and demonstration, a small demo subset route was built. Small `.npz` subsets were exported from the reconstructed `.mat` files.

These demo subsets preserve the same essential input/label structure while remaining small enough for quick loading, forward testing, and tiny demo training.

### 1.4 Data-loader-facing verification

The reconstructed MAT route was connected to a PyTorch-compatible dataset loader, and the resulting input tensors were verified to match the expected shape used by the model demo pipeline.

This means that the data layer has already advanced beyond raw-file storage and has entered executable engineering usage.

---

## 2. What this project has achieved at the data layer

At the current stage, this project has already achieved the following data-layer milestones:

- a public-data replacement route for an expired legacy data source;
- successful generation of train/valid/test dataset artifacts;
- structural verification of reconstructed MAT files;
- creation of lightweight demo subsets;
- successful handoff from reconstructed data files to model-facing loaders.

This is already a substantial data-layer accomplishment for a refactored engineering project.

---

## 3. What is still not fully completed

Although the current data layer is already functional and demonstrable, several data-layer best-practice items are not yet fully expanded into a complete benchmark-grade protocol.

### 3.1 Full QC protocol is not yet implemented

The current project does not yet provide a complete explicit QC framework covering items such as:

- mappability control;
- GC-bias control;
- repeat/low-complexity region handling;
- blacklist usage;
- replicate-level QC metrics.

These items are recognized as important, but they are not yet fully implemented as part of the current engineering pipeline.

### 3.2 Leakage-control discussion is not yet fully benchmark-grade

The project has reconstructed the data and verified the resulting files, but it has not yet expanded into a full benchmark-grade analysis of:

- chromosome-level leakage risk;
- duplicated-region leakage;
- experiment-level leakage;
- alternative split designs.

At the current stage, this should be regarded as a known future-strengthening direction.

### 3.3 The current YAML runtime path still expects another file family

The existing refactored YAML configuration still expects FASTA / BED / TXT runtime files. Therefore, the reconstructed MAT route currently exists as a parallel executable route rather than a fully unified data layer for the entire original runtime configuration.

---

## 4. Why the current data-layer status is still meaningful

Even though some benchmark-grade data-layer controls are not yet fully expanded, the current status is already meaningful because it demonstrates:

- public-data recovery from accessible resources;
- successful reconstruction of model-usable dataset artifacts;
- verification of internal file structure;
- transition from inaccessible legacy data dependency to reproducible engineering inputs.

For a presentation-ready project, this is already a strong and concrete result.

---

## 5. Current data-layer position

At the current stage, the data layer should be described as:

- clearly reconstructed;
- structurally verified;
- demo-executable;
- partially quality-documented;
- not yet expanded into a full benchmark-grade data-governance workflow.

---

## 6. Recommended one-sentence summary

The data layer of the current project has already progressed from legacy inaccessible input dependency to a publicly reconstructed, structurally verified, and demo-executable dataset route, although benchmark-grade QC and leakage-control analysis remain future work.