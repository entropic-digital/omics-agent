from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_align(
    *,
    nucleotide_reads: str,
    indexed_protein_fasta: str,
    mapped_reads: str,
     
) -> subprocess.CompletedProcess:
    """
    Align nucleotide reads to an indexed protein fasta file using PALADIN.

    Args:
        nucleotide_reads: Path to the input nucleotide reads in FASTQ format.
        indexed_protein_fasta: Path to the indexed protein FASTA file (output of paladin index or prepare).
        mapped_reads: Path to the output mapped reads in SAM/BAM format.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/paladin/align",
        inputs=dict(
            nucleotide_reads=nucleotide_reads,
            indexed_protein_fasta=indexed_protein_fasta,
        ),
        outputs=dict(
            mapped_reads=mapped_reads,
        ),
         
    )


@collect_tool()
def align(
    *,
    nucleotide_reads: str,
    indexed_protein_fasta: str,
    mapped_reads: str,
     
) -> subprocess.CompletedProcess:
    """
    Align nucleotide reads to an indexed protein fasta file using PALADIN.

    Args:
        nucleotide_reads: Path to the input nucleotide reads in FASTQ format.
        indexed_protein_fasta: Path to the indexed protein FASTA file (output of paladin index or prepare).
        mapped_reads: Path to the output mapped reads in SAM/BAM format.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_align(
        nucleotide_reads=nucleotide_reads,
        indexed_protein_fasta=indexed_protein_fasta,
        mapped_reads=mapped_reads,
         
    )
