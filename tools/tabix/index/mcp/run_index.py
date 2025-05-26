from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    input_file: str,
    output_file: str,
    params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Process a given file with tabix to create an index.

    Args:
        input_file: Bgzip compressed input file (e.g., BED.gz, GFF.gz, or VCF.gz).
        output_file: Output Tabix index file.
        params (optional): Tabix index parameters (e.g., `-p vcf`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/tabix/index",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file},
        params={"params": params} if params else {},
         
    )


@collect_tool()
def index(
    *,
    input_file: str,
    output_file: str,
    params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Process a given file with tabix to create an index.

    Args:
        input_file: Bgzip compressed input file (e.g., BED.gz, GFF.gz, or VCF.gz).
        output_file: Output Tabix index file.
        params (optional): Tabix index parameters (e.g., `-p vcf`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        input_file=input_file,
        output_file=output_file,
        params=params,
         
    )
