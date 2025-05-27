from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_profiler_illumina(
    *,
    input_file: str,
    output_file: str,
    extra_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Use the ART Profiler to create a base quality score profile for Illumina read data.

    Args:
        input_file: Path to the input fastq-formatted file. Supported extensions:
            fastq, fastq.gz, fq, fq.gz.
        output_file: Path to the output txt-formatted profile.
        extra_params (optional): Any additional parameters to pass to the profiler.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/art/profiler_illumina",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file},
        params={"extra_params": extra_params} if extra_params else {},
         
    )


@collect_tool()
def profiler_illumina(
    *,
    input_file: str,
    output_file: str,
    extra_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Decorator-wrapped function to execute the ART Profiler for Illumina read data.

    Args:
        input_file: Path to the input fastq-formatted file. Supported extensions:
            fastq, fastq.gz, fq, fq.gz.
        output_file: Path to the output txt-formatted profile.
        extra_params (optional): Any additional parameters to pass to the profiler.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_profiler_illumina(
        input_file=input_file,
        output_file=output_file,
        extra_params=extra_params,
         
    )
