from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_blastp(
    *,
    fname_fasta: str,
    fname_db: str,
    fname: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    DIAMOND blastp: A high-performance sequence aligner for protein and translated DNA searches.

    Args:
        fname_fasta: Path to query file (Fasta formatted).
        fname_db: Path to DIAMOND database.
        fname: Path to query results.
        extra (optional): Additional parameters, other than `--threads`, `--db`, `--query`, and `--out`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/diamond/blastp",
        inputs=dict(fname_fasta=fname_fasta, fname_db=fname_db),
        outputs=dict(fname=fname),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def blastp(
    *,
    fname_fasta: str,
    fname_db: str,
    fname: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    DIAMOND blastp: A high-performance sequence aligner for protein and translated DNA searches.

    Args:
        fname_fasta: Path to query file (Fasta formatted).
        fname_db: Path to DIAMOND database.
        fname: Path to query results.
        extra (optional): Additional parameters, other than `--threads`, `--db`, `--query`, and `--out`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_blastp(
        fname_fasta=fname_fasta,
        fname_db=fname_db,
        fname=fname,
        extra=extra,
         
    )
