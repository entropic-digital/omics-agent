from typing import List
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_plass(
    *,
    fastq_files: List[str],
    output_fasta: str,
     
) -> subprocess.CompletedProcess:
    """
    Plass (Protein-Level ASSembler) assembles short read sequencing data on a protein level.

    Args:
        fastq_files: List of input FASTQ files for assembly.
        output_fasta: Path to the output FASTA file containing protein assemblies.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/plass",
        inputs={"fastq_files": fastq_files},
        outputs={"output_fasta": output_fasta},
         
    )


@collect_tool()
def plass(
    *,
    fastq_files: List[str],
    output_fasta: str,
     
) -> subprocess.CompletedProcess:
    """
    Plass (Protein-Level ASSembler) assembles short read sequencing data on a protein level.

    Args:
        fastq_files: List of input FASTQ files for assembly.
        output_fasta: Path to the output FASTA file containing protein assemblies.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_plass(fastq_files=fastq_files, output_fasta=output_fasta,      )
