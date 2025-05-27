from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_prepare_reference(
    *,
    reference_genome: str,
    additional_args: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run rsem-prepare-reference to create index files for downstream analysis with rsem.

    Args:
        reference_genome: Path to the reference genome file.
        additional_args (optional): Additional optional arguments for rsem-prepare-reference.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/rsem/prepare-reference",
        inputs=dict(reference_genome=reference_genome),
        params={"additional_args": additional_args} if additional_args else {},
         
    )


@collect_tool()
def prepare_reference(
    *,
    reference_genome: str,
    additional_args: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run rsem-prepare-reference to create index files for downstream analysis with rsem.

    Args:
        reference_genome: Path to the reference genome file.
        additional_args (optional): Additional optional arguments for rsem-prepare-reference.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_prepare_reference(
        reference_genome=reference_genome,
        additional_args=additional_args,
         
    )
