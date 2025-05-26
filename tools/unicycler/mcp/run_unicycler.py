from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_unicycler(
    *,
    input_reads: str,
    output_assembly: str,
    additional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Assemble bacterial genomes with Unicycler.

    Args:
        input_reads: Path to the Fastq-formatted reads for assembly.
        output_assembly: Path to save the assembled reads.
        additional_params (optional): Additional parameters for Unicycler.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/unicycler",
        inputs=dict(input_reads=input_reads),
        outputs=dict(output_assembly=output_assembly),
        params={"additional_params": additional_params} if additional_params else {},
         
    )


@collect_tool()
def unicycler(
    *,
    input_reads: str,
    output_assembly: str,
    additional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Assemble bacterial genomes with Unicycler.

    You may find additional information on `Unicycler's <https://github.com/rrwick/Unicycler>`_ github page.

    Args:
        input_reads: Path to the Fastq-formatted reads for assembly.
        output_assembly: Path to save the assembled reads.
        additional_params (optional): Additional parameters for Unicycler.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_unicycler(
        input_reads=input_reads,
        output_assembly=output_assembly,
        additional_params=additional_params,
         
    )
