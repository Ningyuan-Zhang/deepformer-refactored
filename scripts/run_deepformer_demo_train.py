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


def evaluate_one_batch(model, loader, criterion, device):
    model.eval()
    xb, yb = next(iter(loader))
    xb = xb.to(device)
    yb = yb.to(device)

    with torch.no_grad():
        output = normalize_output(model(xb))
        loss = criterion(output, yb)

    return float(loss.item()), tuple(output.shape)


def main() -> None:
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print("DEVICE:", device)

    train_ds = DeepSEADemoNPZDataset(
        str(PROJECT_ROOT / "data" / "raw_deepsea" / "demo_subset" / "train_demo_256.npz")
    )
    valid_ds = DeepSEADemoNPZDataset(
        str(PROJECT_ROOT / "data" / "raw_deepsea" / "demo_subset" / "valid_demo_256.npz")
    )

    train_loader = DataLoader(train_ds, batch_size=8, shuffle=True, num_workers=0)
    valid_loader = DataLoader(valid_ds, batch_size=8, shuffle=False, num_workers=0)

    model = DeepFormer(sequence_length=1000, n_targets=919).to(device)
    criterion = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    model.train()
    max_steps = 10

    for step, (xb, yb) in enumerate(train_loader, start=1):
        xb = xb.to(device)
        yb = yb.to(device)

        optimizer.zero_grad()
        output = normalize_output(model(xb))
        loss = criterion(output, yb)
        loss.backward()
        optimizer.step()

        print("STEP {} | TRAIN LOSS {:.6f}".format(step, float(loss.item())))

        if step >= max_steps:
            break

    valid_loss, valid_shape = evaluate_one_batch(model, valid_loader, criterion, device)
    print("VALID LOSS:", valid_loss)
    print("VALID OUTPUT SHAPE:", valid_shape)

    results_dir = PROJECT_ROOT / "results"
    results_dir.mkdir(parents=True, exist_ok=True)
    ckpt_path = results_dir / "deepformer_demo_model.pt"
    torch.save(model.state_dict(), ckpt_path)
    print("CHECKPOINT SAVED TO:", ckpt_path)


if __name__ == "__main__":
    main()