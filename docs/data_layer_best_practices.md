# Data Layer Best Practices

## Purpose

This document summarizes the data-layer best practices relevant to regulatory-genomics sequence modeling projects, especially for projects that rely on public-source reconstruction rather than directly accessible legacy data bundles.

## 1. Data source transparency

A data-driven modeling project should clearly describe:

- where the raw data come from;
- whether the data are directly downloaded or reconstructed from public resources;
- which intermediate transformation steps are applied;
- what the final model-facing file formats are.

If a legacy direct-download route is no longer reliably accessible, the replacement public-data reconstruction path should be documented in sufficient detail for later reproduction.

## 2. Raw-data quality and comparability

When multiple signal tracks or genomic annotations are used, the project should explicitly describe how comparability is controlled. Typical considerations include:

- mappability;
- GC bias;
- repeat-rich regions;
- low-complexity regions;
- blacklist regions, when available;
- consistency of peak/coverage generation rules.

Even when a project does not fully implement all of these controls, the expected quality-control dimensions should still be stated explicitly.

## 3. Signal generation consistency

For regulatory-genomics modeling, the following should be defined consistently:

- peak caller or signal-generation pipeline;
- parameter settings;
- binning or window size;
- transformation of signal values;
- final file format conventions.

A project should avoid mixing incompatible label-generation rules without documenting the difference.

## 4. Negative/background sampling

When a task includes positive and negative genomic regions, the project should document how background examples are chosen. Possible strategies include:

- random genomic background;
- GC-matched background;
- mappability-matched background;
- distance-matched background.

The choice affects model difficulty and interpretation, so it should not be left implicit.

## 5. Data split and leakage control

A regulatory-genomics project should explicitly address data leakage. Good practice includes:

- splitting by chromosome or by large genomic segments rather than by random nearby windows;
- avoiding leakage through duplicated or highly similar genomic regions;
- documenting whether splits are chromosome-based, experiment-based, cell-type-based, or species-based;
- explaining whether labels or annotations may indirectly leak information across train/valid/test sets.

Even in a demo-stage project, leakage risk should be acknowledged and not ignored.

## 6. File-format verification

Before building model loaders, all runtime-facing files should be verified. For example:

- confirm file existence and size;
- confirm whether `.mat` files are standard MATLAB files or HDF5-compatible files;
- inspect key names, shapes, and data types;
- verify consistency between input tensors and label tensors.

This step is especially important when reconstructed public data are used.

## 7. Lightweight demo subsets

Large datasets are not always convenient for debugging or presentation. Therefore, it is often useful to create small demo subsets that:

- preserve the same data structure as the full dataset;
- are small enough for fast testing;
- support quick DataLoader, forward-pass, and tiny-training validation.

These subsets are not replacements for full datasets, but they are valuable engineering tools.

## 8. Reproducibility artifacts

The data layer should leave behind reproducible artifacts such as:

- reconstruction scripts;
- format-inspection scripts;
- result summaries;
- small logs describing completed verification steps.

These files are often more suitable for GitHub than large raw datasets themselves.

## 9. Recommended outputs for a presentation-ready project

A presentation-ready project should ideally provide:

- a documented public-data route;
- a description of the final data format;
- verification of input/label tensor shapes;
- a clear statement of what has and has not been fully quality-controlled;
- a small demo subset for rapid validation.

## 10. Practical interpretation for this project

For the current DeepFormer refactored project, the data-layer best-practice goal is not only to obtain dataset files, but to ensure that:

- the public-data route is explainable;
- the generated files are structurally verified;
- the data are usable by downstream model code;
- the limitations of the current data route are clearly stated.