from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_samxe(
    *,
    fastq: List[str],
    sai: List[str],
    idx: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map paired-end reads with either bwa samse or sampe.

    Args:
        fastq: List of FASTQ file(s).
        sai: List of SAI file(s).
        idx: Path to the BWA reference genome index.
        output: SAM/BAM alignment file to generate.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/bwa/samxe",
        inputs=dict(fastq=fastq, sai=sai, idx=idx),
        outputs=dict(output=output),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def samxe(
    *,
    fastq: List[str],
    sai: List[str],
    idx: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map paired-end reads with either bwa samse or sampe.

    Args:
        fastq: List of FASTQ file(s).
        sai: List of SAI file(s).
        idx: Path to the BWA reference genome index.
        output: SAM/BAM alignment file to generate.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_samxe(
        fastq=fastq,
        sai=sai,
        idx=idx,
        output=output,
        extra=extra,
         
    )
