from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_estimatelibrarycomplexity(
    *,
    input_file: str,
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GATK EstimateLibraryComplexity.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path where the metrics file will be saved.
        java_opts (optional): Additional arguments for the Java compiler, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program-specific arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/estimatelibrarycomplexity",
        inputs=dict(input_file=input_file),
        outputs=dict(output_file=output_file),
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def estimatelibrarycomplexity(
    *,
    input_file: str,
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GATK EstimateLibraryComplexity.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path where the metrics file will be saved.
        java_opts (optional): Additional arguments for the Java compiler, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program-specific arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_estimatelibrarycomplexity(
        input_file=input_file,
        output_file=output_file,
        java_opts=java_opts,
        extra=extra,
         
    )
