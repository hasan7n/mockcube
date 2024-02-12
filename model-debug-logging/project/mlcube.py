"""MLCube handler file"""
import os
import logging
logging.getLogger().setLevel(os.getenv('MEDPERF_LOGLEVEL', 'WARNING'))

import typer
import yaml
from infer import run_inference

app = typer.Typer()


@app.command("infer")
def infer(
    data_path: str = typer.Option(..., "--data_path"),
    parameters_file: str = typer.Option(..., "--parameters_file"),
    output_path: str = typer.Option(..., "--output_path"),
):
    with open(parameters_file) as f:
        parameters = yaml.safe_load(f)

    # main part - to check the logging env
    found_loglevel = os.getenv("MEDPERF_LOGLEVEL", "None")
    expected_loglevel = parameters["expected_loglevel"]
    print(f'container logging level: expected {expected_loglevel}, found {found_loglevel}')
    assert found_loglevel == expected_loglevel

    # stub part to align benchmark & test run to finish successfully
    run_inference(data_path, output_path)


@app.command("hotfix")
def hotfix():
    # NOOP command for typer to behave correctly. DO NOT REMOVE OR MODIFY
    pass


if __name__ == "__main__":
    app()
