from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    fasta_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Creates a BWA index.

    Args:
        fasta_file: Path to the input FASTA file.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/bwa/index",
        inputs=dict(fasta_file=fasta_file),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def index(
    *,
    fasta_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Creates a BWA index.

    Args:
        fasta_file: Path to the input FASTA file.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(fasta_file=fasta_file, extra=extra,      )
