from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_stats(
    *,
    meryl_databases: str,
    output_type: str = "statistics",  # Options: "statistics", "histogram", "print"
     
) -> subprocess.CompletedProcess:
    """
    A genomic k-mer counter (and sequence utility) with nice features.

    Args:
        meryl_databases: Path to the meryl database(s).
        output_type (optional): Specifies which stats to display.
            - "statistics" (default): Shows total, unique, distinct k-mers.
            - "histogram": Displays k-mer frequency.
            - "print": Displays k-mers.
  
    Returns:
        CompletedProcess instance containing information about the
        completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/meryl/stats",
        inputs=dict(meryl_databases=meryl_databases),
        params={"command": output_type},
         
    )


@collect_tool()
def stats(
    *,
    meryl_databases: str,
    output_type: str = "statistics",  # Options: "statistics", "histogram", "print"
     
) -> subprocess.CompletedProcess:
    """
    A genomic k-mer counter (and sequence utility) with nice features.

    Args:
        meryl_databases: Path to the meryl database(s).
        output_type (optional): Specifies which stats to display.
            - "statistics" (default): Shows total, unique, distinct k-mers.
            - "histogram": Displays k-mer frequency.
            - "print": Displays k-mers.
  
    Returns:
        CompletedProcess instance containing information about the
        completed Snakemake process.
    """
    return run_stats(
        meryl_databases=meryl_databases,
        output_type=output_type,
         
    )
