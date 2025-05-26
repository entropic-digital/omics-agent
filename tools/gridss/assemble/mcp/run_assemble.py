from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_assemble(
    *,
    input_file: str,
    output_file: str,
    reference_genome: str,
    threads: Optional[int] = 1,
    temp_dir: Optional[str] = None,
    memory_limit: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GRIDSS assemble module performs genome-wide break-end assembly.

    Args:
        input_file: Path to the input file for GRIDSS assembly.
        output_file: Path where the output will be written.
        reference_genome: Path to the reference genome file.
        threads (optional): Number of CPU threads to use. Defaults to 1.
        temp_dir (optional): Path to the temporary directory.
        memory_limit (optional): Amount of memory to use, e.g., '8G', '16G'.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gridss/assemble",
        inputs=dict(input_file=input_file),
        outputs=dict(output_file=output_file),
        params={
            "reference_genome": reference_genome,
            "threads": threads,
            "temp_dir": temp_dir,
            "memory_limit": memory_limit,
        },
         
    )


@collect_tool()
def assemble(
    *,
    input_file: str,
    output_file: str,
    reference_genome: str,
    threads: Optional[int] = 1,
    temp_dir: Optional[str] = None,
    memory_limit: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GRIDSS assemble module performs genome-wide break-end assembly.

    Args:
        input_file: Path to the input file for GRIDSS assembly.
        output_file: Path where the output will be written.
        reference_genome: Path to the reference genome file.
        threads (optional): Number of CPU threads to use. Defaults to 1.
        temp_dir (optional): Path to the temporary directory.
        memory_limit (optional): Amount of memory to use, e.g., '8G', '16G'.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_assemble(
        input_file=input_file,
        output_file=output_file,
        reference_genome=reference_genome,
        threads=threads,
        temp_dir=temp_dir,
        memory_limit=memory_limit,
         
    )
