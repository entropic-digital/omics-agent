from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_merqury(
    *,
    fasta: str,
    meryldb: str,
    meryldb_parents: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Evaluate genome assemblies with k-mers and more using Merqury.

    Args:
        fasta: One or two assembly fasta file(s).
        meryldb: Meryl database.
        meryldb_parents (optional): Meryl database of parents for trio analysis.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "fasta": fasta,
        "meryldb": meryldb,
        **({"meryldb_parents": meryldb_parents} if meryldb_parents else {}),
    }
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/merqury",
        inputs=inputs,
        params={},
         
    )


@collect_tool()
def merqury(
    *,
    fasta: str,
    meryldb: str,
    meryldb_parents: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Evaluate genome assemblies with k-mers and more using Merqury.

    Args:
        fasta: One or two assembly fasta file(s).
        meryldb: Meryl database.
        meryldb_parents (optional): Meryl database of parents for trio analysis.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_merqury(
        fasta=fasta, meryldb=meryldb, meryldb_parents=meryldb_parents,      
    )
