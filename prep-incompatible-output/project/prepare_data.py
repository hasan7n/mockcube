import os
import yaml
import argparse


class DataPreparation:
    def __init__(self, data_path, labels_path, params_file, output_path):
        with open(params_file, "r") as f:
            self.params = yaml.full_load(f)

        self.data_path = data_path
        self.labels_path = labels_path
        self.output_path = output_path

    def run(self):
        os.makedirs(self.output_path, exist_ok=True)

        file = "nums.txt"
        content = open(os.path.join(self.data_path, file)).read().strip().split("\n")
        content = [list(map(int, line.strip().split())) for line in content]
        content = [[str(num + self.params["add"]) for num in line] for line in content]
        content = "\n".join([" ".join(line) for line in content]) + "\n"

        new_file = file.replace(".txt", ".ext")
        print("processing data")
        with open(os.path.join(self.output_path, new_file), "w") as f:
            f.write(content)

        file = "ans.txt"
        print("processing labels")
        new_file = file.replace(".txt", ".ext")
        with open(os.path.join(self.output_path, new_file), "w") as f:
            f.write(open(os.path.join(self.labels_path, file)).read())

        print("data successfully prepared.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--data_path",
        "--data-path",
        type=str,
        required=True,
        help="Location of videos",
    )

    parser.add_argument(
        "--labels_path",
        "--labels-path",
        type=str,
        required=True,
        help="Location of labels",
    )

    parser.add_argument(
        "--params_file",
        "--params-file",
        type=str,
        required=True,
        help="Configuration file for the data-preparation step",
    )

    parser.add_argument(
        "--output_path",
        "--output-path",
        type=str,
        required=True,
        help="Location to store the prepared data",
    )

    args = parser.parse_args()
    preprocessor = DataPreparation(
        args.data_path, args.labels_path, args.params_file, args.output_path
    )
    preprocessor.run()

