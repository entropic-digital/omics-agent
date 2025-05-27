from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_correction(
    *,
    ref: str,
    query: str,
    fasta: str,
    agp: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Homology-based misassembly correction.

    Args:
        ref: Reference fasta file (uncompressed or bgzipped).
        query: Query fasta file (uncompressed or bgzipped).
        fasta: Path to save the corrected query assembly in FASTA format.
        agp: Path to save the AGP file defining the exact coordinates of query sequence breaks.
        extra (optional): Additional parameters for the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/ragtag/correction",
        inputs=dict(ref=ref, query=query),
        outputs=dict(fasta=fasta, agp=agp),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def correction(
    *,
    ref: str,
    query: str,
    fasta: str,
    agp: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Homology-based misassembly correction.

    Args:
        ref: Reference fasta file (uncompressed or bgzipped).
        query: Query fasta file (uncompressed or bgzipped).
        fasta: Path to save the corrected query assembly in FASTA format.
        agp: Path to save the AGP file defining the exact coordinates of query sequence breaks.
        extra (optional): Additional parameters for the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_correction(
        ref=ref, query=query, fasta=fasta, agp=agp, extra=extra,      
    )
