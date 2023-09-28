#!/usr/bin/env python3
import json
import argparse
from pathlib import Path
from dut import Dut

def load_config(settings: Path) -> dict:
    with open(settings) as settings_file:
        settings = settings_file.read()
        settings_dict = json.loads(settings)
        return settings_dict

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        "--config",
        type=str,
        required=True,
        default="configs/example.json",
        help="loop configuration json file, examples can be found in the configs folder",
    )
    args = parser.parse_args()
    config = load_config(args.config)
    dut = Dut(config)
