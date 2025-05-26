from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_chm_eval_kit(
    *,
    tag: str,
    version: str,
    output: str,
     
) -> subprocess.CompletedProcess:
    """
    Download CHM-eval kit for benchmarking variant calling.

    Args:
        tag: Release tag, see official Git repository.
        version: Release version, see official Git repository.
        output: Path to CHM-eval kit directory.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/benchmark/chm-eval-kit",
        inputs={},
        params={"tag": tag, "version": version},
        outputs={"output": output},
         
    )


@collect_tool()
def chm_eval_kit(
    *,
    tag: str,
    version: str,
    output: str,
     
) -> subprocess.CompletedProcess:
    """
    Download CHM-eval kit for benchmarking variant calling.

    Args:
        tag: Release tag, see official Git repository.
        version: Release version, see official Git repository.
        output: Path to CHM-eval kit directory.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_chm_eval_kit(tag=tag, version=version, output=output,      )
