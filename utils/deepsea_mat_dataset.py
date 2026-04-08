from pathlib import Path
from typing import Optional, Tuple
import numpy as np
import h5py
import torch
from torch.utils.data import Dataset


SPLIT_KEY_MAP = {
    "train": ("trainxdata", "traindata"),
    "valid": ("validxdata", "validdata"),
    "test": ("testxdata", "testdata"),
}


class DeepSEAMatDataset(Dataset):
    """
    Lazy PyTorch Dataset for HDF5-compatible DeepSEA MAT files.

    Expected file structure:
      - train.mat  -> trainxdata / traindata
      - valid.mat  -> validxdata / validdata
      - test.mat   -> testxdata / testdata

    x shape in file: (N, 1000, 4)
    y shape in file: (N, 919)

    Returned x shape: (4, 1000) for Conv1d-style PyTorch models
    Returned y shape: (919,)
    """

    def __init__(self, mat_path: str, split: Optional[str] = None):
        self.mat_path = Path(mat_path)
        self.split = split or self._infer_split_from_filename(self.mat_path.name)

        if self.split not in SPLIT_KEY_MAP:
            raise ValueError("Unknown split: {}".format(self.split))

        self.x_key, self.y_key = SPLIT_KEY_MAP[self.split]

        self._file = h5py.File(str(self.mat_path), "r")
        self.x_data = self._file[self.x_key]
        self.y_data = self._file[self.y_key]

        if self.x_data.shape[0] != self.y_data.shape[0]:
            raise ValueError(
                "Input/label length mismatch: {} vs {}".format(
                    self.x_data.shape[0], self.y_data.shape[0]
                )
            )

    @staticmethod
    def _infer_split_from_filename(filename: str) -> str:
        filename = filename.lower()
        if "train" in filename:
            return "train"
        if "valid" in filename:
            return "valid"
        if "test" in filename:
            return "test"
        raise ValueError("Cannot infer split from filename: {}".format(filename))

    def __len__(self) -> int:
        return int(self.x_data.shape[0])

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        x = np.asarray(self.x_data[idx], dtype=np.float32)   # (1000, 4)
        y = np.asarray(self.y_data[idx], dtype=np.float32)   # (919,)

        # transpose to channel-first for PyTorch Conv1d: (4, 1000)
        x = x.T

        x_tensor = torch.from_numpy(x)
        y_tensor = torch.from_numpy(y)
        return x_tensor, y_tensor

    def close(self) -> None:
        if hasattr(self, "_file") and self._file is not None:
            try:
                self._file.close()
            except Exception:
                pass
            self._file = None

    def __del__(self):
        self.close()