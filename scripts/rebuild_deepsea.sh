#!/usr/bin/env bash
set -euo pipefail

# DeepSEA public-data reconstruction workflow
# This script records the major steps used to reconstruct
# train.mat / valid.mat / test.mat from public resources.

PROJECT_ROOT="${HOME}/ningyuan/projects"
REBUILD_ROOT="${PROJECT_ROOT}/deepsea_rebuild"
BUILD_REPO="${REBUILD_ROOT}/build-deepsea-training-dataset"
HG19_DIR="${REBUILD_ROOT}/hg19"
HG19_FA="${HG19_DIR}/hg19.fa"

mkdir -p "${REBUILD_ROOT}"
mkdir -p "${HG19_DIR}"

echo "[1/6] Entering reconstruction repository..."
cd "${BUILD_REPO}"

echo "[2/6] Downloading public DeepSEA source files..."
cd data
xargs -L 1 curl -C - -O -L < deepsea_data.urls

echo "[3/6] Decompressing source files..."
find . -maxdepth 1 -name "*.gz" -print0 | xargs -0 gunzip || true

echo "[4/6] Preparing hg19 reference genome..."
cd "${HG19_DIR}"
wget -c https://hgdownload.soe.ucsc.edu/goldenPath/hg19/bigZips/chromFa.tar.gz
tar -xzf chromFa.tar.gz
cat chr*.fa > hg19.fa

echo "[5/6] Building DeepSEA .mat files..."
cd "${BUILD_REPO}"
mkdir -p out

python build.py \
  --metadata_file data/deepsea_metadata.tsv \
  --pos data/allTFs.pos.bed \
  --beds_folder data/ \
  --hg19 "${HG19_FA}" \
  --train_size 2200000 \
  --valid_size 4000 \
  --train_filename out/train.mat \
  --valid_filename out/valid.mat \
  --test_filename out/test.mat \
  --train_data_filename out/train_data.npy \
  --train_labels_filename out/train_labels.npy \
  --valid_data_filename out/valid_data.npy \
  --valid_labels_filename out/valid_labels.npy \
  --test_data_filename out/test_data.npy \
  --test_labels_filename out/test_labels.npy \
  2>&1 | tee build_deepsea.log

echo "[6/6] Copying results into the refactored project..."
mkdir -p "${PROJECT_ROOT}/deepformer-refactored/data/raw_deepsea"

cp out/train.mat "${PROJECT_ROOT}/deepformer-refactored/data/raw_deepsea/"
cp out/valid.mat "${PROJECT_ROOT}/deepformer-refactored/data/raw_deepsea/"
cp out/test.mat "${PROJECT_ROOT}/deepformer-refactored/data/raw_deepsea/"

echo "Done."