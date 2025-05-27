from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_aln(
    *,
    fastq: str,
    idx: str,
    sai: str,
    extra: Optional[str] = None,
    sorting: Optional[str] = "none",
    sort_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads with BWA aln.

    Args:
        fastq: Path to the input FASTQ file(s).
        idx: Path to the BWA reference genome index.
        sai: Path for the output SAI file.
        extra (optional): Additional arguments for bwa aln.
        sorting (optional): Sorting method; one of 'none', 'samtools', or 'picard' (default: 'none').
        sort_extra (optional): Extra arguments for samtools/picard sorting.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bwa/aln",
        inputs=dict(fastq=fastq, idx=idx),
        outputs=dict(sai=sai),
        params={
            "extra": extra,
            "sorting": sorting,
            "sort_extra": sort_extra,
        },
         
    )


@collect_tool()
def aln(
    *,
    fastq: str,
    idx: str,
    sai: str,
    extra: Optional[str] = None,
    sorting: Optional[str] = "none",
    sort_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads with BWA aln.

    Args:
        fastq: Path to the input FASTQ file(s).
        idx: Path to the BWA reference genome index.
        sai: Path for the output SAI file.
        extra (optional): Additional arguments for bwa aln.
        sorting (optional): Sorting method; one of 'none', 'samtools', or 'picard' (default: 'none').
        sort_extra (optional): Extra arguments for samtools/picard sorting.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_aln(
        fastq=fastq,
        idx=idx,
        sai=sai,
        extra=extra,
        sorting=sorting,
        sort_extra=sort_extra,
         
    )
