from pathlib import Path

from selene_sdk.utils import load_path, parse_configs_and_run


def main():
    project_root = Path(__file__).resolve().parents[1]
    config_path = project_root / "config" / "evaluate_deepformer.yaml"

    configs = load_path(str(config_path))
    parse_configs_and_run(configs)


if __name__ == "__main__":
    main()