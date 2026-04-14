# DeepFormer Refactored

A practical and runnable DeepFormer repository with a reconstructed MAT-based data route for data loading, forward testing, tiny training, lightweight evaluation, and notebook-based demonstration.

---

## Overview

This repository reorganizes the original DeepFormer project into a cleaner engineering structure and provides a **MAT-based runnable route** for quick validation and demonstration.

At the current stage, the repository supports:

- reconstructed `train.mat / valid.mat / test.mat`
- MAT structure inspection
- demo subset loading from `.npz`
- DeepFormer model instantiation
- forward-pass validation
- tiny demo training
- lightweight demo evaluation
- a notebook-based demo workflow

This repository is intended to help new users quickly answer four questions:

1. What files are required?
2. Which environment should be used?
3. Which scripts should be run first?
4. What outputs should be generated after each step?

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

## Prerequisites

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd deepformer-refactored
```

### 2. Prepare a Python environment

A conda environment is recommended.

```bash
conda create -n deepformer_clean python=3.9 -y
conda activate deepformer_clean
pip install -r requirements.txt
```

If your local setup uses another environment name, that is also fine. The important point is that the environment must be able to import the required packages and run the scripts in `scripts/`.

### 3. Optional notebook support

If you want to run the notebook demo, install notebook-related packages:

```bash
pip install ipykernel notebook jupyterlab
python -m ipykernel install --user --name deepformer_clean --display-name "Python (deepformer_clean)"
```

---

## Required data files

The current runnable route assumes that the following files are available under `data/raw_deepsea/`.

### Full MAT files
- `data/raw_deepsea/train.mat`
- `data/raw_deepsea/valid.mat`
- `data/raw_deepsea/test.mat`

### Demo subset files
- `data/raw_deepsea/demo_subset/train_demo_256.npz`
- `data/raw_deepsea/demo_subset/valid_demo_256.npz`
- `data/raw_deepsea/demo_subset/test_demo_256.npz`

The full MAT files are the reconstructed large-scale data artifacts.  
The demo subset files are smaller extracted files used for quick testing and demonstration.

If these files are not included in your clone, place them in the paths above before running the scripts.

---

## Quick start

If you only want to verify that the current repository is runnable, execute the following commands in order:

```bash
python scripts/test_deepsea_demo_npz.py
python scripts/test_deepformer_forward.py
python scripts/run_deepformer_demo_train.py
python scripts/run_deepformer_demo_eval.py
```

This is the shortest practical execution route in the current repository.

---

## Script-based running procedure

### Step 1. Confirm the project root

Run:

```bash
pwd
```

You should be inside the repository root directory:

```text
deepformer-refactored/
```

---

### Step 2. Activate the environment

```bash
conda activate deepformer_clean
```

Optional check:

```bash
python -c "import sys; print(sys.executable)"
```

This helps confirm that the expected interpreter is being used.

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

This script is used to confirm how the current DeepFormer model should be instantiated.

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

This is a small demonstration training script, not a full benchmark-scale training run.

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

## Notebook-based demo

In addition to the script-based route, the repository also contains a notebook-based demo:

- `notebooks/deepformer_gpu_demo_notebook.ipynb`

This notebook is intended for step-by-step demonstration of the current workflow in notebook format.

The notebook includes:

1. project root setup,
2. dependency import,
3. device checking,
4. demo subset loading,
5. DataLoader construction,
6. DeepFormer construction,
7. forward-pass testing,
8. tiny training,
9. validation,
10. checkpoint and log saving.

### How to use the notebook

Open the notebook in VS Code or Jupyter and select the appropriate kernel.

Recommended kernel:

- `Python (deepformer_clean)`

Important notes:

- always run the notebook from the first cell;
- if the kernel is restarted, run all earlier cells again;
- if the environment changes, restart the kernel before re-running.

---

## Current MAT route

The current runnable route in this repository is a **MAT-based route**.

This means:

1. public data were reconstructed into MAT files,
2. the MAT file structure was inspected,
3. small demo subsets were extracted,
4. the demo subsets were connected to a PyTorch-compatible loader,
5. the loader output was connected to DeepFormer,
6. forward / train / evaluation scripts were built on top of this route.

The current main route is therefore **not yet the original YAML-based FASTA/BED/TXT runtime path**, but a practical MAT-based execution route.

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

- each input sample is a one-hot encoded DNA sequence of length 1000;
- each label is a 919-dimensional target vector.

A more detailed summary is stored in:

- `results/deepsea_mat_summary.txt`

---

## Recommended order for first-time users

For a first-time user of this repository, the recommended order is:

1. read this `README.md`;
2. verify the environment;
3. run `scripts/test_deepsea_demo_npz.py`;
4. run `scripts/test_deepformer_forward.py`;
5. run `scripts/run_deepformer_demo_train.py`;
6. run `scripts/run_deepformer_demo_eval.py`;
7. inspect the files in `results/`.

This order is simpler and more practical than reading all documents first.

---

## Troubleshooting

### 1. Wrong Python interpreter

Check:

```bash
python -c "import sys; print(sys.executable)"
```

Make sure the environment is the intended one.

---

### 2. Wrong working directory

Check:

```bash
pwd
```

Make sure you are inside the repository root before running scripts.

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

- restart the kernel;
- run the notebook again from the first cell.

---

## Output files

The most important result files currently include:

- `results/deepsea_mat_summary.txt`
- `results/deepformer_demo_train_log.txt`
- `results/deepformer_demo_result_summary.txt`
- `results/deepformer_demo_eval_log.txt`
- `results/final_demo_status.txt`

These files provide lightweight evidence that the current route has been executed successfully.

---

## Current scope

The repository already provides a runnable engineering route, but several things are still not finished:

- the MAT route is not yet fully unified with the original YAML runtime path;
- the current training/evaluation flow is demo-scale rather than benchmark-scale;
- peak-vs-coverage comparison has not yet been added;
- interpretability scripts and final outputs have not yet been completed.

Therefore, this repository should currently be understood as a **runnable engineering version**, not a full paper-level reproduction.

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