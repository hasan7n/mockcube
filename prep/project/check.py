import os
import yaml
import argparse


class SanityChecks:
    def __init__(self, data_path, params_file):
        with open(params_file, "r") as f:
            self.params = yaml.full_load(f)

        self.data_path = data_path

    def run(self):
        ans = os.path.join(self.data_path, "ans.csv")
        nums = os.path.join(self.data_path, "nums.csv")
        assert os.path.exists(ans), "file doesn't exist"
        assert os.path.exists(nums), "file doesn't exist"
        assert len(open(ans).read().strip().split("\n")) == len(
            open(nums).read().strip().split("\n")
        )
        print("Prepared data sucessfully passed all tests")


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

    args = parser.parse_args()
    sanity_checker = SanityChecks(args.data_path, args.params_file,)
    sanity_checker.run()

