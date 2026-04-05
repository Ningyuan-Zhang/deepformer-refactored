#!/usr/bin/env bash

set -e

echo "Step 1: setup environment"
bash scripts/setup_env.sh

echo "Step 2: run training"
bash scripts/run_train.sh

echo "Step 3: run evaluation"
bash scripts/run_predict.sh

echo "Pipeline finished."