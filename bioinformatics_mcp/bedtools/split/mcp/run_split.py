from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_split(
    *,
    bed: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Splits a BED file balancing the number of subfiles by line count and base pairs.

    Args:
        bed: Path to the input BED file.
        extra (optional): Additional program arguments (except `-i`, `-n`, or `-p`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bedtools/split",
        inputs=dict(bed=bed),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def split(
    *,
    bed: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Splits a BED file balancing the number of subfiles by line count and base pairs.

    Args:
        bed: Path to the input BED file.
        extra (optional): Additional program arguments (except `-i`, `-n`, or `-p`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_split(bed=bed, extra=extra,      )
