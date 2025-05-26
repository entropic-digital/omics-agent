from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_ngscstat(
    *,
    mapped_reads: str,
    coverage: str,
    stats: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run 'purge_dups ngscstat' to purge haplotigs and overlaps in an assembly based on read depth.

    Args:
        mapped_reads: Path to the mapped reads in PAF format.
        coverage: Path to the output coverage file.
        stats: Path to the output stats file.
        extra (optional): Additional arguments to be passed to the program.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/purge_dups/ngscstat",
        inputs=dict(mapped_reads=mapped_reads),
        outputs=dict(coverage=coverage, stats=stats),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def ngscstat(
    *,
    mapped_reads: str,
    coverage: str,
    stats: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run 'purge_dups ngscstat' to purge haplotigs and overlaps in an assembly based on read depth.

    Args:
        mapped_reads: Path to the mapped reads in PAF format.
        coverage: Path to the output coverage file.
        stats: Path to the output stats file.
        extra (optional): Additional arguments to be passed to the program.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_ngscstat(
        mapped_reads=mapped_reads,
        coverage=coverage,
        stats=stats,
        extra=extra,
         
    )
