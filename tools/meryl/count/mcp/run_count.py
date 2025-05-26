from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_count(
    *,
    fasta_file: str,
    meryl_database: str,
    command: str = "count",
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    A genomic k-mer counter with additional sequence utility features.

    Args:
        fasta_file: Path to the input FASTA file.
        meryl_database: Path to the output Meryl database.
        command: Specifies how to count the kmers. Options: 'count' (default), 'count-forward', 'count-reverse'.
        extra (optional): Additional program arguments (e.g., kmer size `k` is mandatory).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {"command": command}
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:tools/meryl/count",
        inputs={"fasta_file": fasta_file},
        outputs={"meryl_database": meryl_database},
        params=params,
         
    )


@collect_tool()
def meryl_count(
    *,
    fasta_file: str,
    meryl_database: str,
    command: str = "count",
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    A genomic k-mer counter with additional sequence utility features.

    Args:
        fasta_file: Path to the input FASTA file.
        meryl_database: Path to the output Meryl database.
        command: Specifies how to count the kmers. Options: 'count' (default), 'count-forward', 'count-reverse'.
        extra (optional): Additional program arguments (e.g., kmer size `k` is mandatory).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_count(
        fasta_file=fasta_file,
        meryl_database=meryl_database,
        command=command,
        extra=extra,
         
    )
