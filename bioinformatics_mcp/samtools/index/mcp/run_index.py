from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    bam_file: str,
    bam_file_index: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index BAM file with Samtools.

    Args:
        bam_file: Path to the input BAM file.
        bam_file_index: Path to the output BAM file index (.bai).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/samtools/index",
        inputs=dict(bam_file=bam_file),
        outputs=dict(bam_file_index=bam_file_index),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def samtools_index(
    *,
    bam_file: str,
    bam_file_index: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index BAM file with Samtools.

    Args:
        bam_file: Path to the input BAM file.
        bam_file_index: Path to the output BAM file index (.bai).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        bam_file=bam_file,
        bam_file_index=bam_file_index,
        extra=extra,
         
    )
