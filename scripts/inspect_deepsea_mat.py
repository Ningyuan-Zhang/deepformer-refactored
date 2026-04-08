from pathlib import Path
import sys

from scipy.io import loadmat
import h5py


def inspect_with_scipy(path: Path) -> list[str]:
    lines = []
    mat = loadmat(path)
    keys = [k for k in mat.keys() if not k.startswith("__")]
    lines.append("FORMAT: scipy.io.loadmat-compatible")
    lines.append(f"KEYS: {keys}")
    for key in keys:
        value = mat[key]
        try:
            lines.append(f"  {key}: shape={value.shape}, dtype={value.dtype}")
        except Exception:
            lines.append(f"  {key}: type={type(value)}")
    return lines


def inspect_hdf5_group(obj, prefix=""):
    lines = []
    for key in obj.keys():
        item = obj[key]
        if isinstance(item, h5py.Dataset):
            lines.append(f"{prefix}{key}: dataset shape={item.shape}, dtype={item.dtype}")
        elif isinstance(item, h5py.Group):
            lines.append(f"{prefix}{key}: group")
            lines.extend(inspect_hdf5_group(item, prefix=prefix + "  "))
        else:
            lines.append(f"{prefix}{key}: type={type(item)}")
    return lines


def inspect_with_h5py(path: Path) -> list[str]:
    lines = []
    with h5py.File(path, "r") as f:
        lines.append("FORMAT: HDF5-compatible")
        keys = list(f.keys())
        lines.append(f"KEYS: {keys}")
        lines.extend(inspect_hdf5_group(f))
    return lines


def inspect_mat_file(path: Path) -> None:
    print("=" * 80)
    print(f"FILE: {path}")

    # First try scipy.loadmat
    try:
        lines = inspect_with_scipy(path)
        for line in lines:
            print(line)
        return
    except Exception as e:
        print(f"SCIPY_LOADMAT_FAILED: {type(e).__name__}: {e}")

    # Then try h5py
    try:
        lines = inspect_with_h5py(path)
        for line in lines:
            print(line)
        return
    except Exception as e:
        print(f"H5PY_INSPECTION_FAILED: {type(e).__name__}: {e}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python scripts/inspect_deepsea_mat.py <mat_file_1> [<mat_file_2> ...]")
        sys.exit(1)

    for arg in sys.argv[1:]:
        inspect_mat_file(Path(arg))


if __name__ == "__main__":
    main()