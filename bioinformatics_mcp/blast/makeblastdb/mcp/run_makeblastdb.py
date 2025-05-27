from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_makeblastdb(
    *,
    fasta: str,
    output: str,
    params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Makeblastdb produces local BLAST databases from nucleotide or protein FASTA files.

    Args:
        fasta: Path to the input FASTA file.
        output: Path to the output database files with various extensions (e.g., .nin, .nsq, .nhr for nucleotides or .pin, .psq, .phr for proteins).
        params (optional): Additional optional parameters besides `-in`, `-dtype`, and `-out`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/blast/makeblastdb",
        inputs=dict(fasta=fasta),
        outputs=dict(output=output),
        params={"params": params} if params else {},
         
    )


@collect_tool()
def makeblastdb(
    *,
    fasta: str,
    output: str,
    params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Makeblastdb produces local BLAST databases from nucleotide or protein FASTA files.

    Args:
        fasta: Path to the input FASTA file.
        output: Path to the output database files with various extensions (e.g., .nin, .nsq, .nhr for nucleotides or .pin, .psq, .phr for proteins).
        params (optional): Additional optional parameters besides `-in`, `-dtype`, and `-out`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_makeblastdb(
        fasta=fasta,
        output=output,
        params=params,
         
    )
