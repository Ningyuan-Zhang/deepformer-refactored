#!/usr/bin/env bash

set -e

source "$(conda info --base)/etc/profile.d/conda.sh"
conda activate deepformer

python training/evaluate.py