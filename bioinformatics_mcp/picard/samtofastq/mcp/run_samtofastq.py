from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_samtofastq(
    *,
    input_file: str,
    output_fastq1: str,
    output_fastq2: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Converts a SAM or BAM file to FASTQ format.

    Args:
        input_file: Path to the input SAM or BAM file.
        output_fastq1: Path to the first output FASTQ file.
        output_fastq2 (optional): Path to the second output FASTQ file, if paired-end reads.
        java_opts (optional): Additional arguments for the Java compiler, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program-specific parameters.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {"java_opts": java_opts, "extra": extra}
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/picard/samtofastq",
        inputs={"input_file": input_file},
        outputs={"output_fastq1": output_fastq1, "output_fastq2": output_fastq2},
        params={k: v for k, v in params.items() if v is not None},
         
    )


@collect_tool()
def samtofastq(
    *,
    input_file: str,
    output_fastq1: str,
    output_fastq2: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Converts a SAM or BAM file to FASTQ format.

    Args:
        input_file: Path to the input SAM or BAM file.
        output_fastq1: Path to the first output FASTQ file.
        output_fastq2 (optional): Path to the second output FASTQ file, if paired-end reads.
        java_opts (optional): Additional arguments for the Java compiler, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program-specific parameters.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_samtofastq(
        input_file=input_file,
        output_fastq1=output_fastq1,
        output_fastq2=output_fastq2,
        java_opts=java_opts,
        extra=extra,
         
    )
