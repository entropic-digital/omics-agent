from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_mergesamfiles(
    *,
    input_files: List[str],
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Merge sam/bam files using picard tools.

    Args:
        input_files: List of sam/bam files to be merged.
        output_file: Path to the merged sam/bam file.
        java_opts (optional): Additional arguments to pass to the Java compiler (e.g., "-XX:ParallelGCThreads=10").
        extra (optional): Additional program arguments for MergeSamFiles.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/picard/mergesamfiles",
        inputs={"input_files": input_files},
        outputs={"output_file": output_file},
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def mergesamfiles(
    *,
    input_files: List[str],
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Merge sam/bam files using picard tools.

    Args:
        input_files: List of sam/bam files to be merged.
        output_file: Path to the merged sam/bam file.
        java_opts (optional): Additional arguments to pass to the Java compiler (e.g., "-XX:ParallelGCThreads=10").
        extra (optional): Additional program arguments for MergeSamFiles.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mergesamfiles(
        input_files=input_files,
        output_file=output_file,
        java_opts=java_opts,
        extra=extra,
         
    )
