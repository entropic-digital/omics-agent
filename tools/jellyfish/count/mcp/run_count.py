from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_count(
    *,
    sequence_fasta_file: str,
    kmer_count_jf_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Count k-mers in a FASTA file using Jellyfish.

    Args:
        sequence_fasta_file: Path to the input FASTA file containing sequences.
        kmer_count_jf_file: Path to the output Jellyfish (jf) file for k-mer counts.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/jellyfish/count",
        inputs=dict(sequence_fasta_file=sequence_fasta_file),
        outputs=dict(kmer_count_jf_file=kmer_count_jf_file),
         
    )


@collect_tool()
def jellyfish_count(
    *,
    sequence_fasta_file: str,
    kmer_count_jf_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Count k-mers in a FASTA file using Jellyfish.

    Args:
        sequence_fasta_file: Path to the input FASTA file containing sequences.
        kmer_count_jf_file: Path to the output Jellyfish (jf) file for k-mer counts.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_count(
        sequence_fasta_file=sequence_fasta_file,
        kmer_count_jf_file=kmer_count_jf_file,
         
    )
