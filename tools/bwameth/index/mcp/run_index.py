from typing import List
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    reference_fasta: str,
    output_index_files: List[str],
     
) -> subprocess.CompletedProcess:
    """
    Index a reference sequence using bwa-meth for future BS-Seq mapping.

    Args:
        reference_fasta: Path to the reference fasta file.
        output_index_files: List of paths to the resulting index files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/bwameth/index",
        inputs={"reference_fasta": reference_fasta},
        outputs={"output_index_files": output_index_files},
        params={},
         
    )


@collect_tool()
def index(
    *,
    reference_fasta: str,
    output_index_files: List[str],
     
) -> subprocess.CompletedProcess:
    """
    Index a reference sequence using bwa-meth for future BS-Seq mapping.

    Args:
        reference_fasta: Path to the reference fasta file.
        output_index_files: List of paths to the resulting index files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        reference_fasta=reference_fasta,
        output_index_files=output_index_files,
         
    )
