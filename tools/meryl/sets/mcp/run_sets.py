from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_sets(
    *,
    input_databases: List[str],
    output_database: str,
    command: Optional[str] = "union",
     
) -> subprocess.CompletedProcess:
    """
    A genomic k-mer counter (and sequence utility) with nice features.

    Args:
        input_databases: List of input meryl databases.
        output_database: Output meryl database.
        command (optional): Specifies how to handle the kmer sets. Options are:
            `union` (default), `union-min`, `union-max`, `union-sum`, `intersect`,
            `intersect-min`, `intersect-max`, `intersect-sum`, `subtract`,
            `difference`, or `symmetric-difference`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/meryl/sets",
        inputs=dict(input_databases=input_databases),
        outputs=dict(output_database=output_database),
        params={"command": command},
         
    )


@collect_tool()
def sets(
    *,
    input_databases: List[str],
    output_database: str,
    command: Optional[str] = "union",
     
) -> subprocess.CompletedProcess:
    """
    A genomic k-mer counter (and sequence utility) with nice features.

    Args:
        input_databases: List of input meryl databases.
        output_database: Output meryl database.
        command (optional): Specifies how to handle the kmer sets. Options are:
            `union` (default), `union-min`, `union-max`, `union-sum`, `intersect`,
            `intersect-min`, `intersect-max`, `intersect-sum`, `subtract`,
            `difference`, or `symmetric-difference`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_sets(
        input_databases=input_databases,
        output_database=output_database,
        command=command,
         
    )
