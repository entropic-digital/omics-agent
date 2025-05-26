from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_filter_trim(
    *,
    fwd: str,
    rev: Optional[str] = None,
    filt: str,
    filt_rev: Optional[str] = None,
    stats: str,
     
) -> subprocess.CompletedProcess:
    """
    DADA2 Quality filtering of single or paired-end reads using the `filterAndTrim` function.

    Args:
        fwd: Forward FASTQ file without primer sequences.
        rev (optional): Reverse FASTQ file without primer sequences.
        filt: Compressed filtered forward FASTQ file.
        filt_rev (optional): Compressed filtered reverse FASTQ file.
        stats: .tsv file with the number of processed and filtered reads per sample.
     
    Returns:
        CompletedProcess instance with information about the Snakemake execution process.
    """
    inputs = {"fwd": fwd}
    if rev:
        inputs["rev"] = rev

    outputs = {"filt": filt, "stats": stats}
    if filt_rev:
        outputs["filt_rev"] = filt_rev

    return run_snake_wrapper(
        wrapper="file:tools/dada2/filter-trim",
        inputs=inputs,
        outputs=outputs,
        params=kwargs,
    )


@collect_tool()
def filter_trim(
    *,
    fwd: str,
    rev: Optional[str] = None,
    filt: str,
    filt_rev: Optional[str] = None,
    stats: str,
     
) -> subprocess.CompletedProcess:
    """
    DADA2 Quality filtering of single or paired-end reads using the `filterAndTrim` function.

    Args:
        fwd: Forward FASTQ file without primer sequences.
        rev (optional): Reverse FASTQ file without primer sequences.
        filt: Compressed filtered forward FASTQ file.
        filt_rev (optional): Compressed filtered reverse FASTQ file.
        stats: .tsv file with the number of processed and filtered reads per sample.
     
    Returns:
        CompletedProcess instance with information about the Snakemake execution process.
    """
    return run_filter_trim(
        fwd=fwd,
        rev=rev,
        filt=filt,
        filt_rev=filt_rev,
        stats=stats,
         
    )
