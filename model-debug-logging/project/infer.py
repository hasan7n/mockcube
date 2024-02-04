import os


def run_inference(data_path, output_path):

    # load prepared data
    cases = (
        open(os.path.join(data_path, "nums.csv")).read().strip().split("\n")
    )
    preds = [ic for ic in range(len(cases))]

    with open(os.path.join(output_path, "preds.txt"), "w") as f:
        f.write("\n".join(list(map(str, preds))) + "\n")

