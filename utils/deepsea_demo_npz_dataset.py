from pathlib import Path
from typing import Tuple
import numpy as np
import torch
from torch.utils.data import Dataset


class DeepSEADemoNPZDataset(Dataset):
    """
    Lightweight PyTorch dataset for demo subset .npz files.

    Expected structure:
      x: (N, 1000, 4)
      y: (N, 919)

    Returned x:
      (4, 1000) for Conv1d-style models
    Returned y:
      (919,)
    """

    def __init__(self, npz_path: str):
        self.npz_path = Path(npz_path)
        data = np.load(str(self.npz_path))
        self.x = data["x"].astype(np.float32)
        self.y = data["y"].astype(np.float32)

        if self.x.shape[0] != self.y.shape[0]:
            raise ValueError(
                "Input/label length mismatch: {} vs {}".format(
                    self.x.shape[0], self.y.shape[0]
                )
            )

    def __len__(self) -> int:
        return int(self.x.shape[0])

    def __getitem__(self, idx: int) -> Tuple[torch.Tensor, torch.Tensor]:
        x = self.x[idx]      # (1000, 4)
        y = self.y[idx]      # (919,)

        x = x.T              # -> (4, 1000)

        x_tensor = torch.from_numpy(x)
        y_tensor = torch.from_numpy(y)
        return x_tensor, y_tensor