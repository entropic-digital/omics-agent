from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_split(
    *,
    bam_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Split BAM file into sub-files, default by reference.

    Args:
        bam_file: Path to the input BAM file. This must be the only file in input.
        extra (optional): Additional optional parameters.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/bamtools/split",
        inputs={"bam_file": bam_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def split_bam(
    *,
    bam_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Split BAM file into sub-files, default by reference.

    Args:
        bam_file: Path to the input BAM file. This must be the only file in input.
        extra (optional): Additional optional parameters.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_split(bam_file=bam_file, extra=extra,      )
