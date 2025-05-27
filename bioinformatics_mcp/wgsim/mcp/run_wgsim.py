from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_wgsim(
    *,
    read_length: int,
    mutation_rate: float,
    indel_fraction: float,
    coverage: float,
    genome_fasta: str,
    output_prefix: str,
    seed: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Short read simulator.

    Args:
        read_length: Length of simulated reads.
        mutation_rate: Mutation rate during simulation.
        indel_fraction: Fraction of indels in mutations.
        coverage: Desired coverage of the simulated reads.
        genome_fasta: Path to the input reference genome in FASTA format.
        output_prefix: Prefix for the output files containing simulated reads.
        seed (optional): Random seed for reproducibility.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/wgsim",
        inputs=dict(genome_fasta=genome_fasta),
        outputs=dict(output_prefix=output_prefix),
        params={
            "read_length": read_length,
            "mutation_rate": mutation_rate,
            "indel_fraction": indel_fraction,
            "coverage": coverage,
            "seed": seed,
        },
         
    )


@collect_tool()
def wgsim(
    *,
    read_length: int,
    mutation_rate: float,
    indel_fraction: float,
    coverage: float,
    genome_fasta: str,
    output_prefix: str,
    seed: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Short read simulator.

    Args:
        read_length: Length of simulated reads.
        mutation_rate: Mutation rate during simulation.
        indel_fraction: Fraction of indels in mutations.
        coverage: Desired coverage of the simulated reads.
        genome_fasta: Path to the input reference genome in FASTA format.
        output_prefix: Prefix for the output files containing simulated reads.
        seed (optional): Random seed for reproducibility.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_wgsim(
        read_length=read_length,
        mutation_rate=mutation_rate,
        indel_fraction=indel_fraction,
        coverage=coverage,
        genome_fasta=genome_fasta,
        output_prefix=output_prefix,
        seed=seed,
         
    )
