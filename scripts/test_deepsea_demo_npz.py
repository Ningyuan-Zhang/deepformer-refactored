from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from torch.utils.data import DataLoader
from utils.deepsea_demo_npz_dataset import DeepSEADemoNPZDataset


def inspect_one_file(path: Path, name: str) -> None:
    print("=" * 80)
    print("NAME:", name)
    print("PATH:", path)

    dataset = DeepSEADemoNPZDataset(str(path))
    print("DATASET LENGTH:", len(dataset))

    x0, y0 = dataset[0]
    print("SINGLE X SHAPE:", tuple(x0.shape))
    print("SINGLE Y SHAPE:", tuple(y0.shape))
    print("SINGLE X DTYPE:", x0.dtype)
    print("SINGLE Y DTYPE:", y0.dtype)

    loader = DataLoader(dataset, batch_size=4, shuffle=False, num_workers=0)
    xb, yb = next(iter(loader))
    print("BATCH X SHAPE:", tuple(xb.shape))
    print("BATCH Y SHAPE:", tuple(yb.shape))


def main() -> None:
    demo_dir = PROJECT_ROOT / "data" / "raw_deepsea" / "demo_subset"

    inspect_one_file(demo_dir / "train_demo_256.npz", "train_demo_256")
    inspect_one_file(demo_dir / "valid_demo_256.npz", "valid_demo_256")
    inspect_one_file(demo_dir / "test_demo_256.npz", "test_demo_256")


if __name__ == "__main__":
    main()