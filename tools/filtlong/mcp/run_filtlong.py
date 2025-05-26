from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_filtlong(
    *,
    reads: str,
    output: str,
    length_weight: Optional[float] = None,
    quality_weight: Optional[float] = None,
    min_length: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Quality filtering tool for long reads.

    Args:
        reads: Path to the input reads file.
        output: Path to the output filtered reads file.
        length_weight (optional): Weight for the read length in filtering.
        quality_weight (optional): Weight for read quality in filtering.
        min_length (optional): Minimum read length to include in the output.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "length_weight": length_weight,
        "quality_weight": quality_weight,
        "min_length": min_length,
    }
    return run_snake_wrapper(
        wrapper="file:tools/filtlong",
        inputs=dict(reads=reads),
        outputs=dict(output=output),
        params={k: v for k, v in params.items() if v is not None},
         
    )


@collect_tool()
def filtlong(
    *,
    reads: str,
    output: str,
    length_weight: Optional[float] = None,
    quality_weight: Optional[float] = None,
    min_length: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Quality filtering tool for long reads.

    Args:
        reads: Path to the input reads file.
        output: Path to the output filtered reads file.
        length_weight (optional): Weight for the read length in filtering.
        quality_weight (optional): Weight for read quality in filtering.
        min_length (optional): Minimum read length to include in the output.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_filtlong(
        reads=reads,
        output=output,
        length_weight=length_weight,
        quality_weight=quality_weight,
        min_length=min_length,
         
    )
