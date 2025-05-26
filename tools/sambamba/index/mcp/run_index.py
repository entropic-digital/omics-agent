from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    bam_file: str,
    bam_index: str,
     
) -> subprocess.CompletedProcess:
    """
    Indexing a BAM file using Sambamba.

    Args:
        bam_file: Path to the input BAM file.
        bam_index: Path to the output BAM index file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/sambamba/index",
        inputs={"bam_file": bam_file},
        outputs={"bam_index": bam_index},
         
    )


@collect_tool()
def sambamba_index(
    *,
    bam_file: str,
    bam_index: str,
     
) -> subprocess.CompletedProcess:
    """
    Indexing a BAM file using Sambamba.

    Args:
        bam_file: Path to the input BAM file.
        bam_index: Path to the output BAM index file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(bam_file=bam_file, bam_index=bam_index,      )
