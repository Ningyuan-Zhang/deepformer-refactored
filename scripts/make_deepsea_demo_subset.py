from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
import numpy as np
import h5py


def export_subset(input_path: Path, x_key: str, y_key: str, output_path: Path, n: int = 256) -> None:
    with h5py.File(str(input_path), "r") as f:
        x = np.asarray(f[x_key][:n], dtype=np.uint8)
        y = np.asarray(f[y_key][:n], dtype=np.uint8)

    np.savez_compressed(output_path, x=x, y=y)
    print("Saved:", output_path)
    print("  x shape:", x.shape, "dtype:", x.dtype)
    print("  y shape:", y.shape, "dtype:", y.dtype)


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]
    out_dir = project_root / "data" / "raw_deepsea" / "demo_subset"
    out_dir.mkdir(parents=True, exist_ok=True)

    export_subset(
        project_root / "data" / "raw_deepsea" / "train.mat",
        "trainxdata",
        "traindata",
        out_dir / "train_demo_256.npz",
        n=256,
    )
    export_subset(
        project_root / "data" / "raw_deepsea" / "valid.mat",
        "validxdata",
        "validdata",
        out_dir / "valid_demo_256.npz",
        n=256,
    )
    export_subset(
        project_root / "data" / "raw_deepsea" / "test.mat",
        "testxdata",
        "testdata",
        out_dir / "test_demo_256.npz",
        n=256,
    )


if __name__ == "__main__":
    main()