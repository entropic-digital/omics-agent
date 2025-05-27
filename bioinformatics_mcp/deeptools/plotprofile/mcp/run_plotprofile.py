from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_plotprofile(
    *,
    matrix_file: str,
    plot_img: str,
    regions: Optional[str] = None,
    data: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    ``deepTools plotProfile`` plots scores over sets of genomic regions.

    Args:
        matrix_file: Gzipped matrix file from ``deepTools computeMatrix`` (.gz).
        plot_img: Plot file in image format (.png, .eps, .pdf or .svg) [required].
        regions (optional): File with sorted regions after skipping zeros or min/max threshold values (.bed).
        data (optional): Tab-separated table for average profile (.tab).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/deeptools/plotprofile",
        inputs=dict(matrix_file=matrix_file),
        outputs={
            key: value
            for key, value in {
                "plot_img": plot_img,
                "regions": regions,
                "data": data,
            }.items()
            if value
        },
        params={},
         
    )


@collect_tool()
def plotprofile(
    *,
    matrix_file: str,
    plot_img: str,
    regions: Optional[str] = None,
    data: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    ``deepTools plotProfile`` plots scores over sets of genomic regions.

    Args:
        matrix_file: Gzipped matrix file from ``deepTools computeMatrix`` (.gz).
        plot_img: Plot file in image format (.png, .eps, .pdf or .svg) [required].
        regions (optional): File with sorted regions after skipping zeros or min/max threshold values (.bed).
        data (optional): Tab-separated table for average profile (.tab).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_plotprofile(
        matrix_file=matrix_file,
        plot_img=plot_img,
        regions=regions,
        data=data,
         
    )
