from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_plotcoverage(
    *,
    bams: str,
    bed: str,
    blacklist: str,
    raw_counts: str,
    metrics: str,
    plot: str,
     
) -> subprocess.CompletedProcess:
    """
    Run the deepTools plotCoverage tool to assess sequencing depth.

    Args:
        bams: Path to alignment (BAM) file.
        bed: Path to region file (BED).
        blacklist: Path to blacklisted regions (BED).
        raw_counts: Path to output raw coverage plot.
        metrics: Path to output raw coverage metrics.
        plot: Path to output image.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/deeptools/plotcoverage",
        inputs=dict(bams=bams, bed=bed, blacklist=blacklist),
        outputs=dict(raw_counts=raw_counts, metrics=metrics, plot=plot),
         
    )


@collect_tool()
def plotcoverage(
    *,
    bams: str,
    bed: str,
    blacklist: str,
    raw_counts: str,
    metrics: str,
    plot: str,
     
) -> subprocess.CompletedProcess:
    """
    Run the deepTools plotCoverage tool to assess sequencing depth.

    Args:
        bams: Path to alignment (BAM) file.
        bed: Path to region file (BED).
        blacklist: Path to blacklisted regions (BED).
        raw_counts: Path to output raw coverage plot.
        metrics: Path to output raw coverage metrics.
        plot: Path to output image.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_plotcoverage(
        bams=bams,
        bed=bed,
        blacklist=blacklist,
        raw_counts=raw_counts,
        metrics=metrics,
        plot=plot,
         
    )
