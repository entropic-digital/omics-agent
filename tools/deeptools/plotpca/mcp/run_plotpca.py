from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_plotpca(
    *,
    input_file: str,
    output_plot: str,
    output_matrix: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate a principal component analysis (PCA) plot from multiBamSummary or multiBigwigSummary output.

    Args:
        input_file: Path to the compressed matrix file.
        output_plot: Path to the PCA plot. Supported extensions are `.png`, `.eps`, `.pdf`, and `.svg`.
        output_matrix (optional): Optional path to the data underlying the plot.
        extra (optional): Additional command-line parameters to pass besides IO and `--plotFileFormat`.
  
    Returns:
        subprocess.CompletedProcess: Contains information about the completed Snakemake process.
    """
    inputs = {"input_file": input_file}
    outputs = {
        "output_plot": output_plot,
    }
    if output_matrix:
        outputs["output_matrix"] = output_matrix

    params = {}
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:tools/deeptools/plotpca",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def plotpca(
    *,
    input_file: str,
    output_plot: str,
    output_matrix: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate a principal component analysis (PCA) plot from multiBamSummary or multiBigwigSummary output.

    Args:
        input_file: Path to the compressed matrix file.
        output_plot: Path to the PCA plot. Supported extensions are `.png`, `.eps`, `.pdf`, and `.svg`.
        output_matrix (optional): Optional path to the data underlying the plot.
        extra (optional): Additional command-line parameters to pass besides IO and `--plotFileFormat`.
  
    Returns:
        subprocess.CompletedProcess: Contains information about the completed Snakemake process.
    """
    return run_plotpca(
        input_file=input_file,
        output_plot=output_plot,
        output_matrix=output_matrix,
        extra=extra,
         
    )
