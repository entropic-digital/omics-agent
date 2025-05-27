from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_mem(
    *,
    input_file: str,
    reference_file: str,
    output_file: str,
    threads: int = 1,
    additional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    BWA-MEME is a practical and efficient seeding algorithm based on a suffix array
    search algorithm that solves the challenges in utilizing learned indices for SMEM
    search which is extensively used in the seeding phase.

    Args:
        input_file: Path to the input file containing sequencing reads.
        reference_file: Path to the reference genome file.
        output_file: Path for the SAM output produced by BWA-MEME.
        threads (optional): Number of threads to use for computation (default is 1).
        additional_params (optional): Additional command-line parameters for BWA-MEME.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bwa-meme/mem",
        inputs={
            "input_file": input_file,
            "reference_file": reference_file,
        },
        outputs={
            "output_file": output_file,
        },
        params={
            "threads": threads,
            "additional_params": additional_params,
        },
         
    )


@collect_tool()
def mem(
    *,
    input_file: str,
    reference_file: str,
    output_file: str,
    threads: int = 1,
    additional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    BWA-MEME is a practical and efficient seeding algorithm based on a suffix array
    search algorithm that solves the challenges in utilizing learned indices for SMEM
    search which is extensively used in the seeding phase.

    Args:
        input_file: Path to the input file containing sequencing reads.
        reference_file: Path to the reference genome file.
        output_file: Path for the SAM output produced by BWA-MEME.
        threads (optional): Number of threads to use for computation (default is 1).
        additional_params (optional): Additional command-line parameters for BWA-MEME.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mem(
        input_file=input_file,
        reference_file=reference_file,
        output_file=output_file,
        threads=threads,
        additional_params=additional_params,
         
    )
