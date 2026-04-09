from pathlib import Path
import sys

import torch
from torch import nn
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


def compute_binary_accuracy(preds: torch.Tensor, targets: torch.Tensor, threshold: float = 0.5) -> float:
    pred_bin = (preds >= threshold).float()
    correct = (pred_bin == targets).float()
    return float(correct.mean().item())


def main() -> None:
    device = torch.device("cpu")
    print("DEVICE:", device)

    valid_ds = DeepSEADemoNPZDataset(
        str(PROJECT_ROOT / "data" / "raw_deepsea" / "demo_subset" / "valid_demo_256.npz")
    )
    valid_loader = DataLoader(valid_ds, batch_size=8, shuffle=False, num_workers=0)

    model = DeepFormer(sequence_length=1000, n_targets=919).to(device)
    ckpt_path = PROJECT_ROOT / "results" / "deepformer_demo_model.pt"
    print("CHECKPOINT PATH:", ckpt_path)

    state_dict = torch.load(str(ckpt_path), map_location=device)
    model.load_state_dict(state_dict)
    model.eval()

    criterion = nn.BCELoss()

    total_loss = 0.0
    total_acc = 0.0
    total_batches = 0

    first_batch_output_shape = None
    first_batch_target_shape = None
    first_batch_pred_mean = None
    first_batch_pred_std = None
    first_batch_target_mean = None

    with torch.no_grad():
        for xb, yb in valid_loader:
            xb = xb.to(device)
            yb = yb.to(device)

            output = normalize_output(model(xb))
            loss = criterion(output, yb)
            acc = compute_binary_accuracy(output, yb)

            total_loss += float(loss.item())
            total_acc += float(acc)
            total_batches += 1

            if first_batch_output_shape is None:
                first_batch_output_shape = tuple(output.shape)
                first_batch_target_shape = tuple(yb.shape)
                first_batch_pred_mean = float(output.mean().item())
                first_batch_pred_std = float(output.std().item())
                first_batch_target_mean = float(yb.mean().item())

    avg_loss = total_loss / total_batches
    avg_acc = total_acc / total_batches

    print("VALID BATCHES:", total_batches)
    print("AVERAGE VALID LOSS:", avg_loss)
    print("AVERAGE BINARY ACCURACY:", avg_acc)
    print("FIRST BATCH OUTPUT SHAPE:", first_batch_output_shape)
    print("FIRST BATCH TARGET SHAPE:", first_batch_target_shape)
    print("FIRST BATCH PRED MEAN:", first_batch_pred_mean)
    print("FIRST BATCH PRED STD:", first_batch_pred_std)
    print("FIRST BATCH TARGET MEAN:", first_batch_target_mean)


if __name__ == "__main__":
    main()