from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_trim_galore_se(
    *,
    fastq: str,
    trimmed_fastq: str,
    trimming_report: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim unpaired reads using trim_galore.

    Args:
        fastq: Path to the input fastq file with untrimmed reads (can be gzip compressed).
        trimmed_fastq: Path to the output trimmed fastq file.
        trimming_report: Path to the output trimming report.
        extra (optional): Additional parameters to be passed to trim_galore.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/trim_galore/se",
        inputs={"fastq": fastq},
        outputs={
            "trimmed_fastq": trimmed_fastq,
            "trimming_report": trimming_report,
        },
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def trim_galore_se(
    *,
    fastq: str,
    trimmed_fastq: str,
    trimming_report: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim unpaired reads using trim_galore.

    Args:
        fastq: Path to the input fastq file with untrimmed reads (can be gzip compressed).
        trimmed_fastq: Path to the output trimmed fastq file.
        trimming_report: Path to the output trimming report.
        extra (optional): Additional parameters to be passed to trim_galore.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_trim_galore_se(
        fastq=fastq,
        trimmed_fastq=trimmed_fastq,
        trimming_report=trimming_report,
        extra=extra,
         
    )
