from typing import List, Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_plotfingerprint(
    *,
    bam_files: List[str],
    bam_index_files: List[str],
    plot_file: str,
    counts_file: Optional[str] = None,
    metrics_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the deepTools plotFingerprint tool.

    Args:
        bam_files: List of input BAM files.
        bam_index_files: List of corresponding BAM index files (.bai).
        plot_file: Output file for the fingerprint plot in image format (.png, .eps, .pdf, or .svg).
        counts_file (optional): Output file for tab-separated table of read counts per bin (.tab).
        metrics_file (optional): Output file for tab-separated table of quality control metrics (.txt).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "bam_files": bam_files,
        "bam_index_files": bam_index_files,
    }

    outputs = {
        "plot_file": plot_file,
    }

    if counts_file:
        outputs["counts_file"] = counts_file

    if metrics_file:
        outputs["metrics_file"] = metrics_file

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/deeptools/plotfingerprint",
        inputs=inputs,
        outputs=outputs,
         
    )


@collect_tool()
def plotfingerprint(
    *,
    bam_files: List[str],
    bam_index_files: List[str],
    plot_file: str,
    counts_file: Optional[str] = None,
    metrics_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the deepTools plotFingerprint tool.

    Args:
        bam_files: List of input BAM files.
        bam_index_files: List of corresponding BAM index files (.bai).
        plot_file: Output file for the fingerprint plot in image format (.png, .eps, .pdf, or .svg).
        counts_file (optional): Output file for tab-separated table of read counts per bin (.tab).
        metrics_file (optional): Output file for tab-separated table of quality control metrics (.txt).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_plotfingerprint(
        bam_files=bam_files,
        bam_index_files=bam_index_files,
        plot_file=plot_file,
        counts_file=counts_file,
        metrics_file=metrics_file,
         
    )
