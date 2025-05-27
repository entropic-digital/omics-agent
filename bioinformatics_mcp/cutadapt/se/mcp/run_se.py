from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_se(
    *,
    fastq_file: str,
    trimmed_fastq_file: str,
    stats_file: str,
    adapters: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim single-end reads using cutadapt.

    Args:
        fastq_file: Path to the input FASTQ file.
        trimmed_fastq_file: Path to the output trimmed FASTQ file.
        stats_file: Path to the output text file containing trimming statistics.
        adapters (optional): String specifying adapter options for cutadapt.
        extra (optional): Additional program arguments for cutadapt.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/cutadapt/se",
        inputs={"fastq": fastq_file},
        outputs={
            "trimmed_fastq": trimmed_fastq_file,
            "stats": stats_file,
        },
        params={
            "adapters": adapters,
            "extra": extra,
        },
         
    )


@collect_tool()
def cutadapt_se(
    *,
    fastq_file: str,
    trimmed_fastq_file: str,
    stats_file: str,
    adapters: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim single-end reads using cutadapt.

    Args:
        fastq_file: Path to the input FASTQ file.
        trimmed_fastq_file: Path to the output trimmed FASTQ file.
        stats_file: Path to the output text file containing trimming statistics.
        adapters (optional): String specifying adapter options for cutadapt.
        extra (optional): Additional program arguments for cutadapt.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_se(
        fastq_file=fastq_file,
        trimmed_fastq_file=trimmed_fastq_file,
        stats_file=stats_file,
        adapters=adapters,
        extra=extra,
         
    )
