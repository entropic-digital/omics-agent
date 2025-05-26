from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_markdup(
    *,
    bam_file: str,
    deduplicated_bam_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Marks or removes duplicate reads in a BAM file using sambamba markdup.

    Args:
        bam_file: Path to the input BAM file.
        deduplicated_bam_file: Path to the output deduplicated BAM file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/sambamba/markdup",
        inputs=dict(bam_file=bam_file),
        outputs=dict(deduplicated_bam_file=deduplicated_bam_file),
         
    )


@collect_tool()
def markdup(
    *,
    bam_file: str,
    deduplicated_bam_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Marks or removes duplicate reads in a BAM file using sambamba markdup.

    Args:
        bam_file: Path to the input BAM file.
        deduplicated_bam_file: Path to the output deduplicated BAM file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_markdup(
        bam_file=bam_file, deduplicated_bam_file=deduplicated_bam_file,      
    )
