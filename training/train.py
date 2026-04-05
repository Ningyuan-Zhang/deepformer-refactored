from pathlib import Path

from selene_sdk.utils.config import load_path, parse_configs_and_run


def main():
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "config" / "train_deepformer.yaml"

    configs = load_path(str(config_path))
    parse_configs_and_run(configs, lr=0.0005)


if __name__ == "__main__":
    main()