from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    reference_fasta: str,
    output_prefix: str,
    log_file: Optional[str] = None,
    threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Indexes a reference using pbmm2, a minimap2 SMRT wrapper for PacBio data.

    Args:
        reference_fasta: Path to the reference FASTA file to be indexed.
        output_prefix: Prefix for the output index files.
        log_file (optional): Path to a file where logs will be written.
        threads (optional): Number of threads to use for indexing. Default is 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/pbmm2/index",
        inputs=dict(reference_fasta=reference_fasta),
        outputs=dict(output_prefix=output_prefix),
        params={"log_file": log_file, "threads": threads}
        if log_file or threads != 1
        else {},
         
    )


@collect_tool()
def index(
    *,
    reference_fasta: str,
    output_prefix: str,
    log_file: Optional[str] = None,
    threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Indexes a reference using pbmm2, a minimap2 SMRT wrapper for PacBio data.

    Args:
        reference_fasta: Path to the reference FASTA file to be indexed.
        output_prefix: Prefix for the output index files.
        log_file (optional): Path to a file where logs will be written.
        threads (optional): Number of threads to use for indexing. Default is 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        reference_fasta=reference_fasta,
        output_prefix=output_prefix,
        log_file=log_file,
        threads=threads,
         
    )
