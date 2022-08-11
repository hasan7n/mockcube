import os
import yaml
import argparse
import numpy as np


class Statistics:
    def __init__(self, data_path, params_file, out_path):
        with open(params_file, "r") as f:
            self.params = yaml.full_load(f)

        self.data_path = data_path
        self.out_path = out_path

    def run(self):
        num_cases = len(
            open(os.path.join(self.data_path, "ans.ext")).read().strip().split("\n")
        )
        cases = (
            open(os.path.join(self.data_path, "nums.ext")).read().strip().split("\n")
        )
        cases = [line.strip().split() for line in cases]
        num_per_case = [len(case) for case in cases]
        cases = [[int(num) for num in line] for line in cases]
        minimum = min([min(line) for line in cases])
        inverse_minimum = np.nan if minimum == 0 else 1 / minimum
        yaml.safe_dump(
            {
                "num_cases": num_cases,
                "num_per_case": num_per_case,
                "inverse_minimum": inverse_minimum,
            },
            open(self.out_path, "w"),
        )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--data_path",
        "--data-path",
        type=str,
        required=True,
        help="location of prepared data",
    )

    parser.add_argument(
        "--params_file",
        "--params-file",
        type=str,
        required=True,
        help="Configuration file for the data-preparation step",
    )

    parser.add_argument(
        "--out_path",
        "--out-path",
        type=str,
        required=True,
        help="output file to store the statistics",
    )

    args = parser.parse_args()
    statistics_calculator = Statistics(args.data_path, args.params_file, args.out_path)
    statistics_calculator.run()

