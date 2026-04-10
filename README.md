<div align="center">

# 🧬 DeepFormer Refactored

### Public-data reconstruction, MAT-route engineering, and demo-executable DeepFormer workflow

</div>

---

## 📌 Project Overview

This project refactors the original DeepFormer workflow into a clearer engineering repository and builds a **publicly reconstructable data route** that does not rely on an expired legacy download path.

The repository currently provides:

- a refactored DeepFormer project structure;
- a reconstructed public DeepSEA-style dataset route;
- HDF5-compatible MAT verification;
- a MAT-based PyTorch loading pipeline;
- demo subset generation;
- DeepFormer forward validation;
- tiny demo training;
- lightweight demo evaluation.

At the current stage, this project should be regarded as a:

- **presentation-ready engineering project**
- **demo-executable DeepFormer prototype**
- **public-data-reconstructed workflow**
- **not yet a full paper-level reproduction**

---

## ✅ Current Status

The project has already completed the following milestones:

- [x] Public DeepSEA-style data reconstruction
- [x] HDF5-compatible MAT verification
- [x] Demo subset generation
- [x] PyTorch DataLoader validation
- [x] DeepFormer forward-pass validation
- [x] Tiny demo training
- [x] Demo checkpoint saving
- [x] Lightweight demo evaluation

### Current project level

| Level | Status |
|---|---|
| Presentation-ready | ✅ Completed |
| Engineering-demo complete | ✅ Completed |
| Full benchmark-grade reproduction | ❌ Not yet completed |
| Full interpretability experiment | ❌ Not yet completed |

---

## 🧭 Best-Practice Framework

This project is organized under a three-layer best-practice view.

### 1. Data Layer
Focuses on:

- public-data reconstruction;
- MAT-file verification;
- demo-subset preparation;
- data-structure validation;
- current data-layer limitations.

Related files:

- `docs/data_layer_best_practices.md`
- `docs/data_layer_current_status.md`

### 2. Methodology Layer
Focuses on:

- MAT-route loader construction;
- demo subset route;
- DeepFormer forward validation;
- tiny demo training;
- lightweight demo evaluation;
- executable engineering chain.

Related files:

- `docs/methodology_layer_best_practices.md`
- `docs/methodology_layer_current_status.md`

### 3. Interpretability Layer
Focuses on:

- attribution-to-motif workflow planning;
- interpretability tool-chain design;
- future roadmap for DeepLIFT / DeepExplainer / TF-MoDISco / grammar analysis.

Related files:

- `docs/interpretability_layer_best_practices.md`
- `docs/interpretability_layer_roadmap.md`

---

## 🏗 Repository Structure

```text
deepformer-refactored/
├── config/                         # configuration files
├── data/
│   ├── README.md
│   └── raw_deepsea/                # reconstructed MAT files (runtime artifacts)
├── docs/                           # project documents and QMD report
├── models/                         # model definitions
├── results/                        # lightweight logs and summaries
├── scripts/                        # utility / testing / demo scripts
├── training/                       # training and evaluation entry files
├── utils/                          # dataset loaders and helper modules
├── README.md
├── USAGE.md
└── requirements.txt
```

---

## 📂 Public Data Reconstruction

The original legacy public DeepSEA-style route was no longer reliably accessible, so this project adopts a **public reconstruction workflow**.

Using public source files and the hg19 reference genome, the following dataset files were reconstructed:

- `train.mat`
- `valid.mat`
- `test.mat`

These files are stored under:

- `data/raw_deepsea/train.mat`
- `data/raw_deepsea/valid.mat`
- `data/raw_deepsea/test.mat`

### Verified MAT structure

The reconstructed MAT files were inspected and confirmed to be **HDF5-compatible** rather than standard `scipy.io.loadmat` MATLAB files.

| File | Input key | Input shape | Label key | Label shape |
|---|---|---:|---|---:|
| `train.mat` | `trainxdata` | `(4400000, 1000, 4)` | `traindata` | `(4400000, 919)` |
| `valid.mat` | `validxdata` | `(8000, 1000, 4)` | `validdata` | `(8000, 919)` |
| `test.mat` | `testxdata` | `(455024, 1000, 4)` | `testdata` | `(455024, 919)` |

Additional summary:

- `results/deepsea_mat_summary.txt`

---

## 🧪 MAT-Route Demo Pipeline

A dedicated MAT-based engineering route was built to connect reconstructed public data to the refactored DeepFormer code.

### Demo pipeline

```text
public data reconstruction
    -> MAT verification
    -> demo subset generation
    -> PyTorch DataLoader test
    -> DeepFormer forward test
    -> tiny demo training
    -> checkpoint saving
    -> lightweight demo evaluation
```

### Demo subset files

Small `.npz` subsets were generated for rapid testing and presentation:

- `data/raw_deepsea/demo_subset/train_demo_256.npz`
- `data/raw_deepsea/demo_subset/valid_demo_256.npz`
- `data/raw_deepsea/demo_subset/test_demo_256.npz`

These subsets preserve the same basic structure as the full MAT files while enabling fast debugging and demonstration.

---

## 🚀 Quick Start

### 1. Activate environment

```bash
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate ~/ningyuan/envs/deepformer_clean
```

### 2. Test the demo NPZ loader

```bash
python scripts/test_deepsea_demo_npz.py
```

### 3. Inspect the DeepFormer constructor

```bash
python scripts/inspect_deepformer_signature.py
```

### 4. Run a forward-pass validation

```bash
python scripts/test_deepformer_forward.py
```

### 5. Run tiny demo training

```bash
python scripts/run_deepformer_demo_train.py
```

### 6. Run demo evaluation

```bash
python scripts/run_deepformer_demo_eval.py
```

---

## 📊 Result Summaries

Lightweight result artifacts are stored in `results/`, including:

- `results/deepsea_mat_summary.txt`
- `results/deepformer_demo_train_log.txt`
- `results/deepformer_demo_result_summary.txt`
- `results/deepformer_demo_eval_log.txt`
- `results/final_demo_status.txt`
- `results/methodology_layer_summary.txt`
- `results/interpretability_layer_plan.txt`

These files are intentionally small and presentation-friendly.

Large runtime artifacts such as MAT files, demo NPZ subsets, genome archives, and large checkpoints are not intended to be committed to GitHub as ordinary repository content.

---

## 🧠 What Has Been Achieved

This project has already demonstrated that DeepFormer can be turned into a **public-data-reconstructed and demo-executable engineering workflow**.

The most important completed value is:

> the project no longer depends on an expired legacy public-data link and now provides a verifiable route from public data reconstruction to model-connected demo execution.

Concretely, the project already supports:

- reconstructed public dataset artifacts;
- HDF5-compatible MAT inspection;
- MAT-based dataset loading;
- demo data extraction;
- forward-pass verification;
- tiny training;
- lightweight evaluation.

---

## ⚠️ Current Limitations

This repository is not yet a full paper-level reproduction.

### Current limitations include:

- the current YAML runtime path still expects another FASTA / BED / TXT file family;
- the reconstructed MAT route currently exists as a parallel executable route rather than a complete replacement for the original runtime path;
- no peak-vs-coverage paired comparison has been implemented yet;
- no benchmark-grade full training experiment has been completed yet;
- no final attribution/motif/grammar interpretability experiment has been completed yet.

---

## 📘 Main Documents

### General project documents
- `USAGE.md`
- `docs/final_project_status.md`
- `docs/defense_talking_points.md`

### Data layer
- `docs/data_layer_best_practices.md`
- `docs/data_layer_current_status.md`

### Methodology layer
- `docs/methodology_layer_best_practices.md`
- `docs/methodology_layer_current_status.md`

### Interpretability layer
- `docs/interpretability_layer_best_practices.md`
- `docs/interpretability_layer_roadmap.md`

### DeepFormer / MAT-route / demo pipeline
- `docs/deepformer.qmd`
- `docs/deepsea_data_reconstruction.md`
- `docs/runtime_gap_analysis.md`
- `docs/deepsea_mat_route.md`
- `docs/deepsea_demo_pipeline.md`
- `docs/demo_evaluation.md`

---

## 🔮 Future Work

The most natural next steps are:

1. fully unify the MAT route with the main runtime configuration;
2. add a peak-vs-coverage methodology comparison;
3. extend the project to a more formal benchmark-grade training and evaluation setting;
4. integrate interpretability tools such as:
   - DeepLIFT
   - DeepExplainer
   - TF-MoDISco
   - Tangermeme

---

## 🏁 Final Position

A concise summary of the current project status is:

> DeepFormer Refactored has already evolved into a **presentation-ready, public-data-reconstructed, demo-executable engineering project**, although full benchmark-grade reproduction and interpretability experiments remain future work.

---