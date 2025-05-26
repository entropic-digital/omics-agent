from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_view(
    *,
    input_file: str,
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Filter and/or view BAM files using Sambamba.

    Args:
        input_file: Path to the input BAM/SAM file.
        output_file: Path to the output (filtered) BAM/SAM file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/sambamba/view",
        inputs=dict(input_file=input_file),
        outputs=dict(output_file=output_file),
         
    )


@collect_tool()
def view(
    *,
    input_file: str,
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Filter and/or view BAM files using Sambamba.

    Args:
        input_file: Path to the input BAM/SAM file.
        output_file: Path to the output (filtered) BAM/SAM file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_view(input_file=input_file, output_file=output_file,      )
