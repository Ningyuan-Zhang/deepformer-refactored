# DeepSEA Demo Pipeline

## Purpose

This document records the lightweight demo pipeline built on top of the reconstructed public DeepSEA `.mat` files.

## Why a demo pipeline is needed

The reconstructed `.mat` files are large and suitable for demonstrating that the public data route works. However, for quick validation and presentation, it is useful to create much smaller demo subsets that can be loaded quickly and used for lightweight forward tests and tiny training runs.

## Demo pipeline structure

The demo pipeline follows the steps below:

1. reconstruct public DeepSEA `.mat` files;
2. inspect the `.mat` file structure;
3. export small `.npz` demo subsets;
4. build a lightweight PyTorch dataset for the `.npz` files;
5. verify DataLoader behavior;
6. inspect the DeepFormer model constructor;
7. run a forward pass using a small demo batch;
8. run a tiny training loop on the demo subset.

## Demo subset role

The demo subsets are not intended to replace the full dataset. Their purpose is to support:

- rapid testing;
- debugging;
- shape verification;
- forward-pass validation;
- lightweight presentation and defense demonstrations.

## Engineering value

This demo route provides a practical bridge between reconstructed public data and model execution. It is especially useful when the full original runtime configuration has not yet been completely adapted to the reconstructed `.mat` route.