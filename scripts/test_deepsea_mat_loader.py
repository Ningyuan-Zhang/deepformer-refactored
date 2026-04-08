from pathlib import Path
import sys

# Add project root to sys.path
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from torch.utils.data import DataLoader
from utils.deepsea_mat_dataset import DeepSEAMatDataset


def inspect_one_split(mat_path: str, split_name: str) -> None:
    print("=" * 80)
    print("SPLIT:", split_name)
    print("MAT PATH:", mat_path)

    dataset = DeepSEAMatDataset(mat_path, split=split_name)
    print("DATASET LENGTH:", len(dataset))
    print("RAW X SHAPE:", dataset.x_data.shape)
    print("RAW Y SHAPE:", dataset.y_data.shape)

    x0, y0 = dataset[0]
    print("SINGLE X SHAPE:", tuple(x0.shape))
    print("SINGLE Y SHAPE:", tuple(y0.shape))
    print("SINGLE X DTYPE:", x0.dtype)
    print("SINGLE Y DTYPE:", y0.dtype)

    loader = DataLoader(dataset, batch_size=4, shuffle=False, num_workers=0)
    xb, yb = next(iter(loader))
    print("BATCH X SHAPE:", tuple(xb.shape))
    print("BATCH Y SHAPE:", tuple(yb.shape))

    dataset.close()


def main() -> None:
    inspect_one_split(str(PROJECT_ROOT / "data" / "raw_deepsea" / "train.mat"), "train")
    inspect_one_split(str(PROJECT_ROOT / "data" / "raw_deepsea" / "valid.mat"), "valid")
    inspect_one_split(str(PROJECT_ROOT / "data" / "raw_deepsea" / "test.mat"), "test")


if __name__ == "__main__":
    main()