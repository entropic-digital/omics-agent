from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_calcuts(
    *,
    stats_file: str,
    coverage_cutoffs: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Purge haplotigs and overlaps in an assembly based on read depth.

    Args:
        stats_file: Path to the stats file.
        coverage_cutoffs: Path to the output coverage cut-offs file.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/purge_dups/calcuts",
        inputs=dict(stats_file=stats_file),
        outputs=dict(coverage_cutoffs=coverage_cutoffs),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def calcuts(
    *,
    stats_file: str,
    coverage_cutoffs: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Purge haplotigs and overlaps in an assembly based on read depth.

    Args:
        stats_file: Path to the stats file.
        coverage_cutoffs: Path to the output coverage cut-offs file.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_calcuts(
        stats_file=stats_file,
        coverage_cutoffs=coverage_cutoffs,
        extra=extra,
         
    )
