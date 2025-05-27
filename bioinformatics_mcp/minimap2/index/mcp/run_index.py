from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    reference_genome: str,
    indexed_reference_genome: str,
     
) -> subprocess.CompletedProcess:
    """
    Creates a minimap2 index for the reference genome.

    Args:
        reference_genome: Input reference genome in FASTA format.
        indexed_reference_genome: Output path for the indexed reference genome.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/minimap2/index",
        inputs=dict(reference_genome=reference_genome),
        outputs=dict(indexed_reference_genome=indexed_reference_genome),
         
    )


@collect_tool()
def minimap2_index(
    *,
    reference_genome: str,
    indexed_reference_genome: str,
     
) -> subprocess.CompletedProcess:
    """
    Creates a minimap2 index for the reference genome.

    Args:
        reference_genome: Input reference genome in FASTA format.
        indexed_reference_genome: Output path for the indexed reference genome.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        reference_genome=reference_genome,
        indexed_reference_genome=indexed_reference_genome,
         
    )
