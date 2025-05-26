from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_makeTagDirectory(
    *,
    input_bam: str,
    output_directory: str,
    genome: Optional[str] = None,
    additional_options: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create a tag directory with the HOMER suite.

    Args:
        input_bam: Path to the input BAM file.
        output_directory: Path to the output tag directory.
        genome (optional): Genome selection for HOMER.
        additional_options (optional): Additional command-line options for HOMER.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/homer/makeTagDirectory",
        inputs=dict(input_bam=input_bam),
        outputs=dict(output_directory=output_directory),
        params={
            "genome": genome,
            "additional_options": additional_options,
        },
         
    )


@collect_tool()
def makeTagDirectory(
    *,
    input_bam: str,
    output_directory: str,
    genome: Optional[str] = None,
    additional_options: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create a tag directory with the HOMER suite.

    Args:
        input_bam: Path to the input BAM file.
        output_directory: Path to the output tag directory.
        genome (optional): Genome selection for HOMER.
        additional_options (optional): Additional command-line options for HOMER.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_makeTagDirectory(
        input_bam=input_bam,
        output_directory=output_directory,
        genome=genome,
        additional_options=additional_options,
         
    )
