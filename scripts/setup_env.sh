#!/usr/bin/env bash

set -e

echo "[1/4] Create conda environment"
conda create -n deepformer python=3.9 -y

echo "[2/4] Activate environment"
source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate deepformer

echo "[3/4] Install dependencies"
pip install -r requirements.txt

echo "[4/4] Done"
echo "Environment 'deepformer' is ready."