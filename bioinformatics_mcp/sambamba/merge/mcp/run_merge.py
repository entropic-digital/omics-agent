from typing import List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_merge(
    *,
    sorted_bam_files: List[str],
    merged_bam_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Merge multiple BAM files into one using Sambamba.

    Args:
        sorted_bam_files: List of sorted BAM files to merge.
        merged_bam_file: Path to the merged BAM file output.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/sambamba/merge",
        inputs={"sorted_bam_files": sorted_bam_files},
        outputs={"merged_bam_file": merged_bam_file},
         
    )


@collect_tool()
def sambamba_merge(
    *,
    sorted_bam_files: List[str],
    merged_bam_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Merge multiple BAM files into one using Sambamba.

    Args:
        sorted_bam_files: List of sorted BAM files to merge.
        merged_bam_file: Path to the merged BAM file output.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_merge(
        sorted_bam_files=sorted_bam_files,
        merged_bam_file=merged_bam_file,
         
    )
