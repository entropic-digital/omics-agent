from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_pe(
    *,
    input_fastq1: str,
    input_fastq2: str,
    output_trimmed1: str,
    output_trimmed2: str,
    output_report1: str,
    output_report2: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim paired-end reads using trim_galore.

    Args:
        input_fastq1: Path to the first paired-end FASTQ file (can be gzip compressed).
        input_fastq2: Path to the second paired-end FASTQ file (can be gzip compressed).
        output_trimmed1: Path to the first trimmed paired-end FASTQ file.
        output_trimmed2: Path to the second trimmed paired-end FASTQ file.
        output_report1: Path to the trimming report for the first FASTQ file.
        output_report2: Path to the trimming report for the second FASTQ file.
        extra (optional): Additional parameters for trim_galore.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/trim_galore/pe",
        inputs={
            "fastq1": input_fastq1,
            "fastq2": input_fastq2,
        },
        outputs={
            "trimmed1": output_trimmed1,
            "trimmed2": output_trimmed2,
            "report1": output_report1,
            "report2": output_report2,
        },
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def trim_galore_pe(
    *,
    input_fastq1: str,
    input_fastq2: str,
    output_trimmed1: str,
    output_trimmed2: str,
    output_report1: str,
    output_report2: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim paired-end reads using trim_galore.

    Args:
        input_fastq1: Path to the first paired-end FASTQ file (can be gzip compressed).
        input_fastq2: Path to the second paired-end FASTQ file (can be gzip compressed).
        output_trimmed1: Path to the first trimmed paired-end FASTQ file.
        output_trimmed2: Path to the second trimmed paired-end FASTQ file.
        output_report1: Path to the trimming report for the first FASTQ file.
        output_report2: Path to the trimming report for the second FASTQ file.
        extra (optional): Additional parameters for trim_galore.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_pe(
        input_fastq1=input_fastq1,
        input_fastq2=input_fastq2,
        output_trimmed1=output_trimmed1,
        output_trimmed2=output_trimmed2,
        output_report1=output_report1,
        output_report2=output_report2,
        extra=extra,
         
    )
