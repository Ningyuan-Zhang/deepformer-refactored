from pathlib import Path
import sys
import inspect

import torch
from torch.utils.data import DataLoader

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from models.deepformer import DeepFormer
from utils.deepsea_demo_npz_dataset import DeepSEADemoNPZDataset


def normalize_output(output):
    if isinstance(output, torch.Tensor):
        return output
    if isinstance(output, (list, tuple)) and len(output) > 0:
        if isinstance(output[0], torch.Tensor):
            return output[0]
    raise TypeError("Unsupported model output type: {}".format(type(output)))


def main() -> None:
    print("PROJECT ROOT:", PROJECT_ROOT)
    print("MODEL SIGNATURE:", inspect.signature(DeepFormer))

    dataset = DeepSEADemoNPZDataset(
        str(PROJECT_ROOT / "data" / "raw_deepsea" / "demo_subset" / "train_demo_256.npz")
    )
    loader = DataLoader(dataset, batch_size=4, shuffle=False, num_workers=0)
    xb, yb = next(iter(loader))

    print("INPUT BATCH SHAPE:", tuple(xb.shape))
    print("LABEL BATCH SHAPE:", tuple(yb.shape))

    model = DeepFormer(sequence_length=1000, n_targets=919)
    model.eval()

    with torch.no_grad():
        output = model(xb)
        output = normalize_output(output)

    print("OUTPUT SHAPE:", tuple(output.shape))
    print("OUTPUT DTYPE:", output.dtype)
    print("OUTPUT MIN:", float(output.min()))
    print("OUTPUT MAX:", float(output.max()))


if __name__ == "__main__":
    main()