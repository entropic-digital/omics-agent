from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_chm_eval_sample(
    *,
    first_n: Optional[int] = None,
    bam: str,
    bai: str,
     
) -> subprocess.CompletedProcess:
    """
    Download CHM-eval sample for benchmarking variant calling.

    Args:
        first_n (optional): Grab only the first `n` elements.
        bam: Path to CHM-eval sample (BAM formatted).
        bai: Path to the corresponding BAM index.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/benchmark/chm-eval-sample",
        outputs={"bam": bam, "bai": bai},
        params={"first_n": first_n} if first_n is not None else {},
         
    )


@collect_tool()
def chm_eval_sample(
    *,
    first_n: Optional[int] = None,
    bam: str,
    bai: str,
     
) -> subprocess.CompletedProcess:
    """
    Download CHM-eval sample for benchmarking variant calling.

    Args:
        first_n (optional): Grab only the first `n` elements.
        bam: Path to CHM-eval sample (BAM formatted).
        bai: Path to the corresponding BAM index.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_chm_eval_sample(first_n=first_n, bam=bam, bai=bai,      )
