from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    fasta: str,
    index: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index a transcriptome using kallisto.

    Args:
        fasta: FASTA file to index.
        index: Output indexed file.
        extra (optional): Additional parameters for kallisto.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/kallisto/index",
        inputs=dict(fasta=fasta),
        outputs=dict(index=index),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def kallisto_index(
    *,
    fasta: str,
    index: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index a transcriptome using kallisto.

    Args:
        fasta: FASTA file to index.
        index: Output indexed file.
        extra (optional): Additional parameters for kallisto.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(fasta=fasta, index=index, extra=extra,      )
