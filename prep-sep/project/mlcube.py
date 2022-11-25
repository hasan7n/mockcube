"""MLCube handler file"""

import typer
import subprocess


app = typer.Typer()


def exec_python(cmd: str) -> None:
    splitted_cmd = cmd.split()

    subprocess.run(splitted_cmd, cwd=".", check=True)


class PrepareTask(object):
    """
    Task for preparing the data

    Arguments:
    - data_path: data location.
    - labels_path: labels location
    - params_file: yaml file with additional parameters
    - output_path: location to store prepared data
    - output_labels_path: location to store prepared data

    """

    @staticmethod
    def run(
        data_path: str,
        labels_path: str,
        params_file: str,
        output_path: str,
        output_labels_path: str,
    ) -> None:
        cmd = f"python3 prepare_data.py --data_path={data_path} --labels_path={labels_path} --params_file={params_file} --output_path={output_path} --output_labels_path={output_labels_path}"
        exec_python(cmd)


class SanityCheckTask(object):
    """
    Task for checking that the resulting data follows the standard

    Arguments:
    - data_path: data location.
    - params_file: location of parameters.yaml file
    labels_path
    """

    @staticmethod
    def run(data_path: str, params_file: str, labels_path: str) -> None:
        cmd = f"python3 check.py --data_path={data_path} --params_file={params_file} --labels_path={labels_path}"
        exec_python(cmd)


class StatisticsTask(object):
    """
    Task for generating and storing statistics about the prepared data

    Arguments:
    - data_path: data location.
    - params_file: location of parameters.yaml file
    - out_path: location to store the statistics yaml file
    labels_path
    """

    @staticmethod
    def run(data_path: str, params_file: str, out_path: str, labels_path: str) -> None:
        cmd = f"python3 statistics.py --data_path={data_path} --params_file={params_file} --out_path={out_path} --labels_path={labels_path}"
        exec_python(cmd)


@app.command("prepare")
def prepare(
    data_path: str = typer.Option(..., "--data_path"),
    labels_path: str = typer.Option(..., "--labels_path"),
    parameters_file: str = typer.Option(..., "--parameters_file"),
    output_path: str = typer.Option(..., "--output_path"),
    output_labels_path: str = typer.Option(..., "--output_labels_path"),
):
    PrepareTask.run(
        data_path, labels_path, parameters_file, output_path, output_labels_path
    )


@app.command("sanity_check")
def sanity_check(
    data_path: str = typer.Option(..., "--data_path"),
    labels_path: str = typer.Option(..., "--labels_path"),
    parameters_file: str = typer.Option(..., "--parameters_file"),
):
    SanityCheckTask.run(data_path, parameters_file, labels_path)


@app.command("statistics")
def sanity_check(
    data_path: str = typer.Option(..., "--data_path"),
    labels_path: str = typer.Option(..., "--labels_path"),
    parameters_file: str = typer.Option(..., "--parameters_file"),
    out_path: str = typer.Option(..., "--output_path"),
):
    StatisticsTask.run(data_path, parameters_file, out_path, labels_path)


if __name__ == "__main__":
    app()
