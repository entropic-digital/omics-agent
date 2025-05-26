from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_tximport(
    *,
    input_files: List[str],
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Import and summarize transcript-level estimates for both transcript-level and gene-level analysis.

    Args:
        input_files: A list of paths to count data.
        output_file: Path to the tximport RDS object.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/tximport",
        inputs={"input_files": input_files},
        outputs={"output_file": output_file},
        params={},
         
    )


@collect_tool()
def tximport(
    *,
    input_files: List[str],
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Import and summarize transcript-level estimates for both transcript-level and gene-level analysis.

    Args:
        input_files: A list of paths to count data.
        output_file: Path to the tximport RDS object.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_tximport(
        input_files=input_files,
        output_file=output_file,
         
    )
