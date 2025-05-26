from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_pe(
    *,
    input_fastq1: str,
    input_fastq2: str,
    output_trimmed_fastq1: str,
    output_trimmed_fastq2: str,
    output_stats: str,
    adapters: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim paired-end reads using cutadapt.

    Args:
        input_fastq1: Path to the first input paired-end FASTQ file.
        input_fastq2: Path to the second input paired-end FASTQ file.
        output_trimmed_fastq1: Path to the first trimmed paired-end FASTQ file.
        output_trimmed_fastq2: Path to the second trimmed paired-end FASTQ file.
        output_stats: Path to the text file containing trimming statistics.
        adapters (optional): Additional adapter options for cutadapt.
        extra (optional): Additional arguments passed to the cutadapt command.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/cutadapt/pe",
        inputs={
            "fastq1": input_fastq1,
            "fastq2": input_fastq2,
        },
        outputs={
            "trimmed_fastq1": output_trimmed_fastq1,
            "trimmed_fastq2": output_trimmed_fastq2,
            "stats": output_stats,
        },
        params={
            "adapters": adapters,
            "extra": extra,
        },
         
    )


@collect_tool()
def cutadapt_pe(
    *,
    input_fastq1: str,
    input_fastq2: str,
    output_trimmed_fastq1: str,
    output_trimmed_fastq2: str,
    output_stats: str,
    adapters: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim paired-end reads using cutadapt.

    Args:
        input_fastq1: Path to the first input paired-end FASTQ file.
        input_fastq2: Path to the second input paired-end FASTQ file.
        output_trimmed_fastq1: Path to the first trimmed paired-end FASTQ file.
        output_trimmed_fastq2: Path to the second trimmed paired-end FASTQ file.
        output_stats: Path to the text file containing trimming statistics.
        adapters (optional): Additional adapter options for cutadapt.
        extra (optional): Additional arguments passed to the cutadapt command.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_pe(
        input_fastq1=input_fastq1,
        input_fastq2=input_fastq2,
        output_trimmed_fastq1=output_trimmed_fastq1,
        output_trimmed_fastq2=output_trimmed_fastq2,
        output_stats=output_stats,
        adapters=adapters,
        extra=extra,
         
    )
