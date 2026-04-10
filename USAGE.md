<div align="center">

# 🚀 Usage Guide

### How to run, inspect, and demonstrate the DeepFormer Refactored project

</div>

---

## 📌 Purpose of This Document

This file explains how to use the current **DeepFormer Refactored** project in practice.

It is designed for three use cases:

- understanding the repository workflow;
- running the current MAT-route demo pipeline;
- locating the right documents, scripts, and result files during project presentation or defense.

This guide focuses on the **current executable engineering route**, which is based on:

- reconstructed public DeepSEA-style MAT files;
- lightweight demo subsets;
- DeepFormer forward, tiny training, and demo evaluation.

---

## ✅ What This Project Can Do Right Now

At the current stage, this repository already supports:

- public-data reconstruction results stored as `.mat` files;
- HDF5-compatible MAT verification;
- demo subset `.npz` generation;
- PyTorch DataLoader validation;
- DeepFormer forward-pass testing;
- tiny demo training;
- checkpoint saving;
- lightweight demo evaluation.

This means the project is already **demo-executable**, even though it is **not yet a full benchmark-grade reproduction**.

---

## 🧭 Recommended Usage Path

If you want to understand or demonstrate the project in the most natural order, use this sequence:

1. read the project overview in `README.md`;
2. inspect the main report in `docs/deepformer.qmd`;
3. confirm the current MAT-route data status;
4. test the demo data loader;
5. inspect the DeepFormer model constructor;
6. run the forward-pass test;
7. run tiny demo training;
8. run demo evaluation;
9. inspect the result summaries in `results/`.

---

## 📁 Most Important Files

### Core documents
- `README.md`
- `docs/deepformer.qmd`
- `docs/final_project_status.md`
- `docs/defense_talking_points.md`

### Data-layer documents
- `docs/data_layer_best_practices.md`
- `docs/data_layer_current_status.md`

### Methodology-layer documents
- `docs/methodology_layer_best_practices.md`
- `docs/methodology_layer_current_status.md`

### Interpretability-layer documents
- `docs/interpretability_layer_best_practices.md`
- `docs/interpretability_layer_roadmap.md`

### MAT-route / demo documents
- `docs/deepsea_data_reconstruction.md`
- `docs/runtime_gap_analysis.md`
- `docs/deepsea_mat_route.md`
- `docs/deepsea_demo_pipeline.md`
- `docs/demo_evaluation.md`

### Scripts
- `scripts/inspect_deepsea_mat.py`
- `scripts/test_deepsea_demo_npz.py`
- `scripts/inspect_deepformer_signature.py`
- `scripts/test_deepformer_forward.py`
- `scripts/run_deepformer_demo_train.py`
- `scripts/run_deepformer_demo_eval.py`

---

## ⚙️ Environment Setup

The current demo route was developed and tested using the `deepformer_clean` environment on the server.

### Activate the environment

```bash
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate ~/ningyuan/envs/deepformer_clean
```

### Confirm Python path

```bash
which python
python --version
```

You should confirm that Python points to the intended environment before running scripts.

---

## 📂 Data Usage

The current executable route is based on reconstructed public MAT files stored under:

- `data/raw_deepsea/train.mat`
- `data/raw_deepsea/valid.mat`
- `data/raw_deepsea/test.mat`

The lightweight demo subsets are stored under:

- `data/raw_deepsea/demo_subset/train_demo_256.npz`
- `data/raw_deepsea/demo_subset/valid_demo_256.npz`
- `data/raw_deepsea/demo_subset/test_demo_256.npz`

### Important note

The original YAML runtime path still expects another file family based on FASTA / BED / TXT inputs. Therefore, the current MAT route is a **parallel executable route**, not yet a full replacement for the original runtime path.

---

## 🧪 Step-by-Step Demo Workflow

This is the recommended practical execution order.

### Step 1. Test the demo NPZ loader

```bash
python scripts/test_deepsea_demo_npz.py
```

Expected output:

- dataset length;
- single-sample input shape;
- single-sample label shape;
- batch input shape;
- batch label shape.

This step confirms that the demo subset can be read correctly by the PyTorch dataset and DataLoader.

---

### Step 2. Inspect the DeepFormer constructor

```bash
python scripts/inspect_deepformer_signature.py
```

Expected output:

- model class name;
- source file path;
- model constructor signature.

This is useful for confirming how the model should be instantiated in demo scripts.

---

### Step 3. Run a forward-pass validation

```bash
python scripts/test_deepformer_forward.py
```

Expected output:

- input batch shape;
- label batch shape;
- model output shape;
- output min/max or similar summary.

This step confirms that the reconstructed MAT-route data can actually be passed through the model.

---

### Step 4. Run tiny demo training

```bash
python scripts/run_deepformer_demo_train.py
```

Expected output:

- several training-loss lines;
- validation loss;
- validation output shape;
- checkpoint-saving path.

A demo checkpoint should be saved to:

- `results/deepformer_demo_model.pt`

This step confirms that the current route is trainable at demo scale.

---

### Step 5. Run demo evaluation

```bash
python scripts/run_deepformer_demo_eval.py
```

Expected output:

- average validation loss;
- average binary accuracy;
- output shape;
- prediction statistics.

This step confirms that the saved checkpoint can be reloaded and evaluated on the validation demo subset.

---

## 📊 Result Files

Lightweight result artifacts are stored under `results/`.

Typical files include:

- `results/deepsea_mat_summary.txt`
- `results/deepformer_demo_train_log.txt`
- `results/deepformer_demo_result_summary.txt`
- `results/deepformer_demo_eval_log.txt`
- `results/final_demo_status.txt`
- `results/methodology_layer_summary.txt`
- `results/interpretability_layer_plan.txt`

### What these files are for

These files are intended to:

- record structural verification results;
- preserve demo training/evaluation logs;
- provide small presentation-friendly evidence files;
- support defense and project explanation.

### What should *not* normally be committed

Large runtime artifacts should generally remain outside routine GitHub tracking, including:

- full MAT files;
- large demo data archives;
- genome FASTA archives;
- large intermediate files;
- large checkpoints.

---

## 🧠 How to Explain the Current Project

If you need to present the project, the clearest interpretation is:

- the repository has already completed **public-data reconstruction**;
- the reconstructed MAT route has been **verified structurally**;
- the demo data pipeline is **connected to the DeepFormer model**;
- a **tiny but complete train/eval loop** has been demonstrated;
- the project is already **presentation-ready and engineering-demonstrable**;
- it is **not yet a full paper-level benchmark reproduction**.

---

## 🏁 Recommended Minimal Demonstration

If you only have a short time and want to prove the project works, run the following four commands in order:

```bash
python scripts/test_deepsea_demo_npz.py
python scripts/test_deepformer_forward.py
python scripts/run_deepformer_demo_train.py
python scripts/run_deepformer_demo_eval.py
```

This gives you the shortest meaningful executable chain.

---

## 🔍 Troubleshooting

### 1. `ModuleNotFoundError`
Cause:
- the wrong environment is active;
- the project root is not on the Python path in a script.

Fix:
- activate `deepformer_clean`;
- re-run from the repository root;
- verify script imports.

### 2. `.mat` cannot be read by `scipy.io.loadmat`
Cause:
- reconstructed MAT files are HDF5-compatible rather than standard old-style MATLAB MAT files.

Fix:
- inspect them with the provided HDF5-aware script;
- use the MAT-route loader based on `h5py`.

### 3. GPU-related runtime error
Cause:
- unstable shared GPU state or CUDA/cuDNN compatibility issues.

Fix:
- use the CPU-based demo route for stability;
- reduce batch size if needed.

### 4. GitHub push does not include results
Cause:
- `results/` may be ignored by `.gitignore`.

Fix:
- use `git add -f` for selected small result files;
- do not add large runtime artifacts.

---

## ⚠️ Current Limitations

This repository still has important limitations:

- the MAT route is not yet fully unified with the original YAML runtime path;
- no peak-vs-coverage paired comparison has been completed yet;
- no benchmark-grade full training experiment has been completed;
- no completed attribution/motif/grammar analysis is available yet.

These limitations should be stated honestly in any formal presentation.

---

## 🔮 Suggested Next Steps

If the project is continued after the current stage, the most natural next directions are:

1. unify the MAT route with the main runtime path;
2. add a peak-vs-coverage methodology comparison;
3. extend the project into a more formal benchmark-scale training/evaluation setting;
4. integrate interpretability tools such as:
   - DeepLIFT
   - DeepExplainer
   - TF-MoDISco
   - Tangermeme

---

## 📌 Final Usage Summary

The simplest way to use this repository is:

1. activate the correct environment;
2. test the demo NPZ loader;
3. run the model forward test;
4. run tiny demo training;
5. run demo evaluation;
6. inspect results and supporting documents.

In its current form, the project is already suitable for:

- defense presentation;
- engineering demonstration;
- structured project handoff;
- future extension into a more complete reproduction workflow.

---