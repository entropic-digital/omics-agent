from typing import Optional, List
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_coveragebed(
    *,
    a: str,
    b: List[str],
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Returns the depth and breadth of coverage of features from B on the intervals in A.

    Args:
        a: Path to the feature file (BAM/BED/GFF/VCF). This file is compared to `b`.
        b: Path or list of paths to file(s) (BAM/BED/GFF/VCF).
        output: Path to the coverage file.
        extra (optional): Additional program arguments (except `-a` and `-b`).
  
    Notes:
        * This program/wrapper does not handle multi-threading.

    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/bedtools/coveragebed",
        inputs={"a": a, "b": b},
        outputs={"output": output},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def coveragebed(
    *,
    a: str,
    b: List[str],
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Returns the depth and breadth of coverage of features from B on the intervals in A.

    Args:
        a: Path to the feature file (BAM/BED/GFF/VCF). This file is compared to `b`.
        b: Path or list of paths to file(s) (BAM/BED/GFF/VCF).
        output: Path to the coverage file.
        extra (optional): Additional program arguments (except `-a` and `-b`).
  
    Notes:
        * This program/wrapper does not handle multi-threading.

    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_coveragebed(
        a=a,
        b=b,
        output=output,
        extra=extra,
         
    )
