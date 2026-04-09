from pathlib import Path
import sys
import inspect

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from models.deepformer import DeepFormer


def main() -> None:
    print("PROJECT ROOT:", PROJECT_ROOT)
    print("MODEL CLASS:", DeepFormer.__name__)
    print("MODEL MODULE FILE:", inspect.getsourcefile(DeepFormer))
    print("MODEL SIGNATURE:", inspect.signature(DeepFormer))


if __name__ == "__main__":
    main()