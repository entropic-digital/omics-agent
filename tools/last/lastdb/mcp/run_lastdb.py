from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_lastdb(
    *,
    fasta_reference: str,
    indexed_db: str,
     
) -> subprocess.CompletedProcess:
    """
    LAST finds similar regions between sequences and aligns them. It is designed for comparing large datasets to each other
    (e.g., vertebrate genomes and/or large numbers of DNA reads).

    Args:
        fasta_reference: Path to the input FASTA file containing the reference sequences.
        indexed_db: Path to the output indexed database for mapping with LAST.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/last/lastdb",
        inputs=dict(fasta_reference=fasta_reference),
        outputs=dict(indexed_db=indexed_db),
         
    )


@collect_tool()
def lastdb(
    *,
    fasta_reference: str,
    indexed_db: str,
     
) -> subprocess.CompletedProcess:
    """
    LAST finds similar regions between sequences and aligns them. It is designed for comparing large datasets to each other
    (e.g., vertebrate genomes and/or large numbers of DNA reads).

    Args:
        fasta_reference: Path to the input FASTA file containing the reference sequences.
        indexed_db: Path to the output indexed database for mapping with LAST.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_lastdb(fasta_reference=fasta_reference, indexed_db=indexed_db,      )
