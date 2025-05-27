from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_revertsam(
    *,
    input_file: str,
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Reverts SAM or BAM files to a previous state.

    Args:
        input_file: Path to the input SAM/BAM file.
        output_file: Path to the output SAM/BAM file.
        java_opts (optional): Additional arguments for the Java compiler, e.g., "-XX:ParallelGCThreads=10". Excludes `-XmX` or `-Djava.io.tmpdir`.
        extra (optional): Additional program arguments for RevertSam.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {}
    if java_opts:
        params["java_opts"] = java_opts
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/picard/revertsam",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file},
        params=params,
         
    )


@collect_tool()
def revertsam(
    *,
    input_file: str,
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Reverts SAM or BAM files to a previous state.

    Args:
        input_file: Path to the input SAM/BAM file.
        output_file: Path to the output SAM/BAM file.
        java_opts (optional): Additional arguments for the Java compiler, e.g., "-XX:ParallelGCThreads=10". Excludes `-XmX` or `-Djava.io.tmpdir`.
        extra (optional): Additional program arguments for RevertSam.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_revertsam(
        input_file=input_file,
        output_file=output_file,
        java_opts=java_opts,
        extra=extra,
         
    )
