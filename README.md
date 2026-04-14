# DeepFormer Refactored

A refactored and runnable DeepFormer repository with a reconstructed public MAT-based data route for demo loading, forward testing, tiny training, lightweight evaluation, and notebook-based GPU demonstration.

---

## Overview

This repository is organized as a practical runnable version of DeepFormer.

At the current stage, it already supports:

- reconstructed public `train.mat / valid.mat / test.mat`
- MAT file inspection and structure verification
- demo subset loading from `.npz`
- DeepFormer model instantiation
- forward-pass validation
- tiny demo training
- lightweight demo evaluation
- a notebook-based GPU demo workflow

The goal of this repository is simple: let a reader quickly see

1. which environment to use,
2. which data files are needed,
3. which scripts should be run first,
4. what output files should be produced.

---

## Repository structure

```text
deepformer-refactored/
├── config/                  # configuration files
├── data/                    # MAT files, demo subsets, and data notes
├── docs/                    # extended project documentation
├── models/                  # model definitions
├── notebooks/               # notebook-based demo
├── results/                 # logs and lightweight result summaries
├── scripts/                 # runnable scripts
├── training/                # training/evaluation-related code
├── utils/                   # loaders and helper functions
├── README.md
├── USAGE.md
└── requirements.txt
```

---

## Recommended environment

For the current script-based demo route, use:

```bash
source /mnt/public5/genomebench/miniconda3/etc/profile.d/conda.sh
conda activate /mnt/public5/genomebench/miniconda3/envs/deepformer_clean
```

Before running any script, it is recommended to confirm the Python path:

```bash
python -c "import sys; print(sys.executable)"
```

---

## Required data files

The current runnable route assumes that the following files already exist on the server.

### Full MAT files
- `data/raw_deepsea/train.mat`
- `data/raw_deepsea/valid.mat`
- `data/raw_deepsea/test.mat`

### Demo subset files
- `data/raw_deepsea/demo_subset/train_demo_256.npz`
- `data/raw_deepsea/demo_subset/valid_demo_256.npz`
- `data/raw_deepsea/demo_subset/test_demo_256.npz`

The MAT files are the reconstructed large-scale data artifacts.  
The demo subset files are small extracted files used for quick testing and demonstration.

---

## Quick start

If you only want to verify that the current repository is runnable, execute the following commands in order:

```bash
cd /mnt/public5/genomebench/ningyuan/projects/deepformer-refactored

source /mnt/public5/genomebench/miniconda3/etc/profile.d/conda.sh
conda activate /mnt/public5/genomebench/miniconda3/envs/deepformer_clean

python scripts/test_deepsea_demo_npz.py
python scripts/test_deepformer_forward.py
python scripts/run_deepformer_demo_train.py
python scripts/run_deepformer_demo_eval.py
```

This is the shortest practical execution route in the current repository.

---

## Script-based running procedure

### Step 1. Enter the project root

```bash
cd /mnt/public5/genomebench/ningyuan/projects/deepformer-refactored
pwd
```

Expected output:

```text
/mnt/public5/genomebench/ningyuan/projects/deepformer-refactored
```

---

### Step 2. Activate the environment

```bash
source /mnt/public5/genomebench/miniconda3/etc/profile.d/conda.sh
conda activate /mnt/public5/genomebench/miniconda3/envs/deepformer_clean
```

Optional check:

```bash
python -c "import sys; print(sys.executable)"
```

---

### Step 3. Test whether the demo subset can be loaded

```bash
python scripts/test_deepsea_demo_npz.py
```

This script checks:

- whether the `.npz` demo files can be opened,
- whether the input shape is correct,
- whether the label shape is correct,
- whether the DataLoader can generate batches correctly.

If this step fails, later model steps should not be run yet.

---

### Step 4. Inspect the DeepFormer constructor

```bash
python scripts/inspect_deepformer_signature.py
```

This script is used to confirm how the current DeepFormer model is instantiated.

For the current demo route, the expected constructor arguments are:

- `sequence_length = 1000`
- `n_targets = 919`

---

### Step 5. Run a forward-pass validation

```bash
python scripts/test_deepformer_forward.py
```

This script checks whether:

- a batch from the demo subset can be passed into the model,
- the model output shape is correct,
- the forward pass can finish successfully.

If this step passes, the data-to-model connection is working.

---

### Step 6. Run tiny demo training

```bash
python scripts/run_deepformer_demo_train.py
```

This is a small demonstration training script, not a full benchmark training run.

It is used to verify:

- loss computation,
- backward propagation,
- optimizer update,
- checkpoint saving.

Typical output files include:

- `results/deepformer_demo_train_log.txt`
- `results/deepformer_demo_result_summary.txt`
- `results/deepformer_demo_model.pt`

---

### Step 7. Run lightweight demo evaluation

```bash
python scripts/run_deepformer_demo_eval.py
```

This script loads the demo checkpoint and performs a lightweight evaluation on the validation demo subset.

Typical output files include:

- `results/deepformer_demo_eval_log.txt`
- `results/final_demo_status.txt`

---

## Notebook-based GPU demo

In addition to the script-based route, the repository also contains a notebook-based GPU demo:

- `notebooks/deepformer_gpu_demo_notebook.ipynb`

This notebook is intended for step-by-step demonstration of the current workflow in notebook format.

The notebook includes:

1. entering the project root,
2. importing dependencies,
3. checking GPU availability,
4. loading the demo subset,
5. constructing the DataLoader,
6. constructing DeepFormer,
7. running a forward test,
8. running tiny training,
9. running validation,
10. saving checkpoint and logs.

### How to use the notebook

Open the notebook in VS Code or Jupyter and select the appropriate kernel.

Important notes:

- always run the notebook from the first cell,
- if the kernel is restarted, run all earlier cells again,
- if the environment changes, restart the kernel before re-running.

---

## Current MAT route

The current runnable route in this repository is a MAT-based route.

This means:

1. public data were reconstructed into MAT files,
2. the MAT file structure was inspected,
3. small demo subsets were extracted,
4. the demo subsets were connected to a PyTorch-compatible loader,
5. the loader output was connected to DeepFormer,
6. forward / train / evaluation scripts were built on top of this route.

The current main route is therefore not yet the original YAML-based FASTA/BED/TXT runtime path, but a practical MAT-based execution route.

---

## Data shapes used in the current route

From the reconstructed MAT files:

### Training set
- `trainxdata`: `(4400000, 1000, 4)`
- `traindata`: `(4400000, 919)`

### Validation set
- `validxdata`: `(8000, 1000, 4)`
- `validdata`: `(8000, 919)`

### Test set
- `testxdata`: `(455024, 1000, 4)`
- `testdata`: `(455024, 919)`

This means:

- each input sample is a one-hot encoded DNA sequence of length 1000,
- each label is a 919-dimensional target vector.

A more detailed summary is stored in:

- `results/deepsea_mat_summary.txt`

---

## Recommended order for first-time users

For a first-time user of this repository, the recommended order is:

1. read this `README.md`,
2. verify the environment,
3. run `test_deepsea_demo_npz.py`,
4. run `test_deepformer_forward.py`,
5. run `run_deepformer_demo_train.py`,
6. run `run_deepformer_demo_eval.py`,
7. inspect the files in `results/`.

This order is simpler and more practical than reading all documents first.

---

## Troubleshooting

### 1. Wrong Python interpreter

Check:

```bash
python -c "import sys; print(sys.executable)"
```

Make sure the environment path is the intended one.

---

### 2. Wrong working directory

Check:

```bash
pwd
```

Make sure you are inside:

```text
/mnt/public5/genomebench/ningyuan/projects/deepformer-refactored
```

---

### 3. Missing demo subset files

Check:

```bash
ls data/raw_deepsea/demo_subset
```

If the demo subset files are missing, the demo route will not run.

---

### 4. Data loading fails

Run:

```bash
python scripts/test_deepsea_demo_npz.py
```

before running any model-related script.

---

### 5. Model forward fails

Run:

```bash
python scripts/test_deepformer_forward.py
```

before trying training or evaluation.

---

### 6. Notebook variables are missing after restart

If the notebook reports errors such as `PROJECT_ROOT is not defined`, it usually means the kernel was restarted and later cells were executed before earlier setup cells.

In this case:

- restart the kernel,
- run the notebook again from the first cell.

---

## Output files

The most important result files currently include:

- `results/deepsea_mat_summary.txt`
- `results/deepformer_demo_train_log.txt`
- `results/deepformer_demo_result_summary.txt`
- `results/deepformer_demo_eval_log.txt`
- `results/final_demo_status.txt`

These files are intended to provide lightweight evidence that the current route has been executed successfully.

---

## Current scope

The repository already provides a runnable engineering route, but several things are still not finished:

- the MAT route is not yet fully unified with the original YAML runtime path,
- the current training/evaluation flow is demo-scale rather than benchmark-scale,
- peak-vs-coverage comparison has not yet been added,
- interpretability scripts and final outputs have not yet been completed.

Therefore, this repository should currently be understood as a runnable engineering version, not a full paper-level reproduction.

---

## Additional documentation

If more detailed notes are needed, refer to:

### Data-related documents
- `docs/data_layer_best_practices.md`
- `docs/data_layer_current_status.md`

### Method-related documents
- `docs/methodology_layer_best_practices.md`
- `docs/methodology_layer_current_status.md`

### Interpretability-related documents
- `docs/interpretability_layer_best_practices.md`
- `docs/interpretability_layer_roadmap.md`

### Project notes
- `docs/deepformer.qmd`
- `docs/final_project_status.md`
- `docs/defense_talking_points.md`

---

## Minimal command summary

If you only want the current shortest runnable path, use:

```bash
python scripts/test_deepsea_demo_npz.py
python scripts/test_deepformer_forward.py
python scripts/run_deepformer_demo_train.py
python scripts/run_deepformer_demo_eval.py
```