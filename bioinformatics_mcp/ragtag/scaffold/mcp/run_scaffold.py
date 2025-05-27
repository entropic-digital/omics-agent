from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_scaffold(
    *,
    ref: str,
    query: str,
    fasta: str,
    agp: str,
    stats: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Homology-based assembly scaffolding using RagTag.

    Args:
        ref: Reference fasta file (uncompressed or bgzipped).
        query: Query fasta file (uncompressed or bgzipped).
        fasta: Output file for scaffolds in FASTA format.
        agp: Output file for ordering and orientations of query sequences in AGP format.
        stats: Output file for scaffolding process summary statistics.
        extra (optional): Additional parameters for the scaffolding process.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/ragtag/scaffold",
        inputs=dict(ref=ref, query=query),
        outputs=dict(fasta=fasta, agp=agp, stats=stats),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def scaffold(
    *,
    ref: str,
    query: str,
    fasta: str,
    agp: str,
    stats: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Homology-based assembly scaffolding using RagTag.

    Args:
        ref: Reference fasta file (uncompressed or bgzipped).
        query: Query fasta file (uncompressed or bgzipped).
        fasta: Output file for scaffolds in FASTA format.
        agp: Output file for ordering and orientations of query sequences in AGP format.
        stats: Output file for scaffolding process summary statistics.
        extra (optional): Additional parameters for the scaffolding process.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_scaffold(
        ref=ref,
        query=query,
        fasta=fasta,
        agp=agp,
        stats=stats,
        extra=extra,
         
    )
