from typing import Optional, List, Union
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_fastp(
    *,
    fastq_files: List[str],
    trimmed_fastq_files: List[str],
    unpaired_reads: Optional[Union[str, List[str]]] = None,
    merged_reads: Optional[str] = None,
    failed_reads: Optional[str] = None,
    json_stats: str,
    html_stats: str,
    adapters: Optional[Union[str, List[str]]] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run fastp to trim and perform QC on fastq reads.

    Args:
        fastq_files: Input fastq file(s).
        trimmed_fastq_files: Output trimmed fastq file(s).
        unpaired_reads (optional): Output unpaired reads, either in a single file or separate files.
        merged_reads (optional): Output file for merged reads.
        failed_reads (optional): Output file for failed reads.
        json_stats: Output JSON file containing trimming statistics.
        html_stats: Output HTML file containing trimming statistics.
        adapters (optional): Adapter sequences to use for trimming.
        extra (optional): Additional arguments to pass to fastp.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "adapters": adapters,
        "extra": extra,
    }
    params = {k: v for k, v in params.items() if v is not None}

    outputs = {
        "trimmed_fastq_files": trimmed_fastq_files,
        "unpaired_reads": unpaired_reads,
        "merged_reads": merged_reads,
        "failed_reads": failed_reads,
        "json_stats": json_stats,
        "html_stats": html_stats,
    }
    outputs = {k: v for k, v in outputs.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:tools/fastp",
        inputs={"fastq_files": fastq_files},
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def fastp(
    *,
    fastq_files: List[str],
    trimmed_fastq_files: List[str],
    unpaired_reads: Optional[Union[str, List[str]]] = None,
    merged_reads: Optional[str] = None,
    failed_reads: Optional[str] = None,
    json_stats: str,
    html_stats: str,
    adapters: Optional[Union[str, List[str]]] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run fastp to trim and perform QC on fastq reads.

    Args:
        fastq_files: Input fastq file(s).
        trimmed_fastq_files: Output trimmed fastq file(s).
        unpaired_reads (optional): Output unpaired reads, either in a single file or separate files.
        merged_reads (optional): Output file for merged reads.
        failed_reads (optional): Output file for failed reads.
        json_stats: Output JSON file containing trimming statistics.
        html_stats: Output HTML file containing trimming statistics.
        adapters (optional): Adapter sequences to use for trimming.
        extra (optional): Additional arguments to pass to fastp.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_fastp(
        fastq_files=fastq_files,
        trimmed_fastq_files=trimmed_fastq_files,
        unpaired_reads=unpaired_reads,
        merged_reads=merged_reads,
        failed_reads=failed_reads,
        json_stats=json_stats,
        html_stats=html_stats,
        adapters=adapters,
        extra=extra,
         
    )
