from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_split_fa(
    *,
    stats_file: str,
    coverage_cut_offs: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Purge haplotigs and overlaps in an assembly based on read depth.

    Args:
        stats_file: Path to the input stats file.
        coverage_cut_offs: Path to the output coverage cut-offs file.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/purge_dups/split_fa",
        inputs=dict(stats_file=stats_file),
        outputs=dict(coverage_cut_offs=coverage_cut_offs),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def split_fa(
    *,
    stats_file: str,
    coverage_cut_offs: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Purge haplotigs and overlaps in an assembly based on read depth.

    Args:
        stats_file: Path to the input stats file.
        coverage_cut_offs: Path to the output coverage cut-offs file.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_split_fa(
        stats_file=stats_file,
        coverage_cut_offs=coverage_cut_offs,
        extra=extra,
         
    )
