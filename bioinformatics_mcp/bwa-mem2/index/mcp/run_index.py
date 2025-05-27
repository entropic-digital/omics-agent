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
    Creates a bwa-mem2 index.

    Args:
        reference_genome: Path to the reference genome in FASTA format.
        indexed_reference_genome: Path where the indexed reference genome will be saved.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bwa-mem2/index",
        inputs={"reference_genome": reference_genome},
        outputs={"indexed_reference_genome": indexed_reference_genome},
         
    )


@collect_tool()
def index_tool(
    *,
    reference_genome: str,
    indexed_reference_genome: str,
     
) -> subprocess.CompletedProcess:
    """
    Creates a bwa-mem2 index.

    Args:
        reference_genome: Path to the reference genome in FASTA format.
        indexed_reference_genome: Path where the indexed reference genome will be saved.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        reference_genome=reference_genome,
        indexed_reference_genome=indexed_reference_genome,
         
    )
