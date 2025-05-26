from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_plotcorrelation(
    *,
    input_matrix: str,
    output_plot: str,
    output_matrix: Optional[str] = None,
    extra: Optional[str] = None,
    correlation: str = "spearman",
    plot: str = "heatmap",
     
) -> subprocess.CompletedProcess:
    """
    Deeptools Plot Correlation.

    Analysis and visualization of sample correlations based on the output
    of multiBamSummary or multiBigwigSummary.

    Args:
        input_matrix: Path to compressed matrix file.
        output_plot: Path to scatterplot/heatmap. The available formats are `.png`, `.eps`, `.pdf`, and `.svg`.
        output_matrix (optional): Optional path to pairwise correlation values (TSV).
        extra (optional): Optional parameters except IO and `--plotFileFormat`.
        correlation: Either `spearman` or `pearson`.
        plot: Either `heatmap` or `scatterplot`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/deeptools/plotcorrelation",
        inputs={"matrix": input_matrix},
        outputs={"plot": output_plot, "matrix": output_matrix}
        if output_matrix
        else {"plot": output_plot},
        params={
            "extra": extra,
            "correlation": correlation,
            "plot": plot,
        },
         
    )


@collect_tool()
def plotcorrelation(
    *,
    input_matrix: str,
    output_plot: str,
    output_matrix: Optional[str] = None,
    extra: Optional[str] = None,
    correlation: str = "spearman",
    plot: str = "heatmap",
     
) -> subprocess.CompletedProcess:
    """
    Deeptools Plot Correlation.

    Analysis and visualization of sample correlations based on the output
    of multiBamSummary or multiBigwigSummary.

    Args:
        input_matrix: Path to compressed matrix file.
        output_plot: Path to scatterplot/heatmap. The available formats are `.png`, `.eps`, `.pdf`, and `.svg`.
        output_matrix (optional): Optional path to pairwise correlation values (TSV).
        extra (optional): Optional parameters except IO and `--plotFileFormat`.
        correlation: Either `spearman` or `pearson`.
        plot: Either `heatmap` or `scatterplot`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_plotcorrelation(
        input_matrix=input_matrix,
        output_plot=output_plot,
        output_matrix=output_matrix,
        extra=extra,
        correlation=correlation,
        plot=plot,
         
    )
