from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_pear(
    *,
    input_files: tuple[str, str],
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    PEAR: ultrafast, memory-efficient and highly accurate pair-end read merger.

    Args:
        input_files: A tuple containing paths to the paired FASTQ files.
        output_file: Path to the merged FASTQ output file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/pear",
        inputs=dict(input_files=input_files),
        outputs=dict(output_file=output_file),
         
    )


@collect_tool()
def pear(
    *,
    input_files: tuple[str, str],
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    PEAR: ultrafast, memory-efficient and highly accurate pair-end read merger.

    Args:
        input_files: A tuple containing paths to the paired FASTQ files.
        output_file: Path to the merged FASTQ output file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_pear(input_files=input_files, output_file=output_file,      )
