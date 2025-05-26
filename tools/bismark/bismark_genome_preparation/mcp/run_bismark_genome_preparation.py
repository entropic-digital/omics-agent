from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bismark_genome_preparation(
    *,
    genome: str,
    bismark_genome_dir: str,
     
) -> subprocess.CompletedProcess:
    """
    Generate reference genome indexes for Bismark.

    Args:
        genome: Path to genome file (*.fa, *.fasta, *.fa.gz, *.fasta.gz).
        bismark_genome_dir: Output directory where generated Bismark indexes are moved and input fasta file is soft-linked.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/bismark/bismark_genome_preparation",
        inputs=dict(genome=genome),
        outputs=dict(bismark_genome_dir=bismark_genome_dir),
         
    )


@collect_tool()
def bismark_genome_preparation(
    *,
    genome: str,
    bismark_genome_dir: str,
     
) -> subprocess.CompletedProcess:
    """
    Generate reference genome indexes for Bismark.

    Args:
        genome: Path to genome file (*.fa, *.fasta, *.fa.gz, *.fasta.gz).
        bismark_genome_dir: Output directory where generated Bismark indexes are moved and input fasta file is soft-linked.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bismark_genome_preparation(
        genome=genome, bismark_genome_dir=bismark_genome_dir,      
    )
