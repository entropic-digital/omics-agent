from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_quant(
    *,
    index: str,
    r: Optional[str] = None,
    r1: Optional[str] = None,
    r2: Optional[str] = None,
    output: str,
    bam: str,
    libType: str,
    gtf: Optional[str] = None,
    extra: Optional[str] = None,
    threads: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Quantify transcripts using Salmon.

    Args:
        index: Path to Salmon indexed sequences.
        r (optional): Path to unpaired reads.
        r1 (optional): Path to upstream reads file.
        r2 (optional): Path to downstream reads file.
        output: Path to quantification file.
        bam: Path to pseudo-bam file.
        libType: Format string describing the library type.
        gtf (optional): Optional path to a GTF formatted genome annotation.
        extra (optional): Additional command line parameters.
        threads (optional): Number of threads to use.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "index": index,
        "r": r,
        "r1": r1,
        "r2": r2,
    }
    # Remove None values from inputs
    inputs = {key: value for key, value in inputs.items() if value is not None}

    params = {
        "libType": libType,
        "extra": extra,
        "gtf": gtf,
    }
    # Remove None values from params
    params = {key: value for key, value in params.items() if value is not None}

    outputs = {
        "output": output,
        "bam": bam,
    }

    return run_snake_wrapper(
        wrapper="file:tools/salmon/quant",
        inputs=inputs,
        outputs=outputs,
        params=params,
        threads=threads,
         
    )


@collect_tool()
def quant(
    *,
    index: str,
    r: Optional[str] = None,
    r1: Optional[str] = None,
    r2: Optional[str] = None,
    output: str,
    bam: str,
    libType: str,
    gtf: Optional[str] = None,
    extra: Optional[str] = None,
    threads: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Quantify transcripts using Salmon.

    Args:
        index: Path to Salmon indexed sequences.
        r (optional): Path to unpaired reads.
        r1 (optional): Path to upstream reads file.
        r2 (optional): Path to downstream reads file.
        output: Path to quantification file.
        bam: Path to pseudo-bam file.
        libType: Format string describing the library type.
        gtf (optional): Optional path to a GTF formatted genome annotation.
        extra (optional): Additional command line parameters.
        threads (optional): Number of threads to use.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_quant(
        index=index,
        r=r,
        r1=r1,
        r2=r2,
        output=output,
        bam=bam,
        libType=libType,
        gtf=gtf,
        extra=extra,
        threads=threads,
         
    )
