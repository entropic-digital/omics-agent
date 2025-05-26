from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_se(
    *,
    input_reads: str,
    output_reads: str,
    quality_threshold: int,
    length_threshold: int,
    format: Optional[str] = "fastq",
    gzip_output: bool = False,
    phred_type: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim single-end reads with sickle.

    Args:
        input_reads: Path to the input single-end reads file.
        output_reads: Path for the output trimmed reads.
        quality_threshold: Minimum quality score to keep a read.
        length_threshold: Minimum read length to retain after trimming.
        format (optional): Format of the input file (default: "fastq").
        gzip_output (optional): Whether to gzip the output files (default: False).
        phred_type (optional): Specify Phred type ('33' or '64', optional).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/sickle/se",
        inputs=dict(input_reads=input_reads),
        outputs=dict(output_reads=output_reads),
        params={
            "quality_threshold": quality_threshold,
            "length_threshold": length_threshold,
            "format": format,
            "gzip_output": gzip_output,
            "phred_type": phred_type,
        },
         
    )


@collect_tool()
def se(
    *,
    input_reads: str,
    output_reads: str,
    quality_threshold: int,
    length_threshold: int,
    format: Optional[str] = "fastq",
    gzip_output: bool = False,
    phred_type: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim single-end reads with sickle.

    Args:
        input_reads: Path to the input single-end reads file.
        output_reads: Path for the output trimmed reads.
        quality_threshold: Minimum quality score to keep a read.
        length_threshold: Minimum read length to retain after trimming.
        format (optional): Format of the input file (default: "fastq").
        gzip_output (optional): Whether to gzip the output files (default: False).
        phred_type (optional): Specify Phred type ('33' or '64', optional).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_se(
        input_reads=input_reads,
        output_reads=output_reads,
        quality_threshold=quality_threshold,
        length_threshold=length_threshold,
        format=format,
        gzip_output=gzip_output,
        phred_type=phred_type,
         
    )
