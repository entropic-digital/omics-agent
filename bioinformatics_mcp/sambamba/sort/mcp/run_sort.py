from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_sort(
    *,
    bam_file: str,
    sorted_bam_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Sort bam file with sambamba.

    Args:
        bam_file: Path to the input bam file.
        sorted_bam_file: Path to the output sorted bam file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/sambamba/sort",
        inputs=dict(bam_file=bam_file),
        outputs=dict(sorted_bam_file=sorted_bam_file),
         
    )


@collect_tool()
def sambamba_sort(
    *,
    bam_file: str,
    sorted_bam_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Sort bam file with sambamba.

    Args:
        bam_file: Path to the input bam file.
        sorted_bam_file: Path to the output sorted bam file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_sort(bam_file=bam_file, sorted_bam_file=sorted_bam_file,      )
