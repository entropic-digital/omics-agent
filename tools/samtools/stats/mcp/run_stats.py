from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_stats(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate statistics using samtools.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path to the output statistics file.
        extra (optional): Additional program arguments (not `-@/--threads`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/samtools/stats",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def stats(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate statistics using samtools.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path to the output statistics file.
        extra (optional): Additional program arguments (not `-@/--threads`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_stats(
        input_file=input_file,
        output_file=output_file,
        extra=extra,
         
    )
