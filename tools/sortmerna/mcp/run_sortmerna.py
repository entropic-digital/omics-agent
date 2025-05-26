from typing import Optional, List
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_sortmerna(
    *,
    reference_files: List[str],
    query_file: str,
    aligned_reads: str,
    unaligned_reads: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    SortMeRNA is a local sequence alignment tool for filtering,
    mapping, and OTU clustering.

    Args:
        reference_files: One or more reference FASTA files.
        query_file: Query FASTA file (single or paired-end).
        aligned_reads: Path to save aligned reads.
        unaligned_reads: Path to save unaligned reads.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the
        completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/sortmerna",
        inputs=dict(reference_files=reference_files, query_file=query_file),
        outputs=dict(aligned_reads=aligned_reads, unaligned_reads=unaligned_reads),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def sortmerna(
    *,
    reference_files: List[str],
    query_file: str,
    aligned_reads: str,
    unaligned_reads: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    SortMeRNA is a local sequence alignment tool for filtering,
    mapping, and OTU clustering.

    Args:
        reference_files: One or more reference FASTA files.
        query_file: Query FASTA file (single or paired-end).
        aligned_reads: Path to save aligned reads.
        unaligned_reads: Path to save unaligned reads.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the
        completed Snakemake process.
    """
    return run_sortmerna(
        reference_files=reference_files,
        query_file=query_file,
        aligned_reads=aligned_reads,
        unaligned_reads=unaligned_reads,
        extra=extra,
         
    )
