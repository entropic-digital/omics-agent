from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_fastqc(
    *,
    fastq_file: str,
    html_file: str,
    zip_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Generate fastq QC statistics using FastQC.

    Args:
        fastq_file: Path to the input FASTQ file.
        html_file: Path to the output HTML file containing statistics.
        zip_file: Path to the output ZIP file containing statistics.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/fastqc",
        inputs={"fastq": fastq_file},
        outputs={"html": html_file, "zip": zip_file},
         
    )


@collect_tool()
def fastqc(
    *,
    fastq_file: str,
    html_file: str,
    zip_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Generate fastq QC statistics using FastQC.

    Args:
        fastq_file: Path to the input FASTQ file.
        html_file: Path to the output HTML file containing statistics.
        zip_file: Path to the output ZIP file containing statistics.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_fastqc(
        fastq_file=fastq_file, html_file=html_file, zip_file=zip_file
    )
