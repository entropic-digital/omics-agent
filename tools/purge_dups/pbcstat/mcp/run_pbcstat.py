from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_pbcstat(
    *,
    mapped_reads: str,
    coverage: str,
    stats: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Purge haplotigs and overlaps in an assembly based on read depth.

    Args:
        mapped_reads: Input file with mapped reads in PAF format.
        coverage: Output file to store coverage information.
        stats: Output file to store statistical information.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/purge_dups/pbcstat",
        inputs={"mapped_reads": mapped_reads},
        outputs={"coverage": coverage, "stats": stats},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def pbcstat(
    *,
    mapped_reads: str,
    coverage: str,
    stats: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Purge haplotigs and overlaps in an assembly based on read depth.

    Args:
        mapped_reads: Input file with mapped reads in PAF format.
        coverage: Output file to store coverage information.
        stats: Output file to store statistical information.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_pbcstat(
        mapped_reads=mapped_reads,
        coverage=coverage,
        stats=stats,
        extra=extra,
         
    )
