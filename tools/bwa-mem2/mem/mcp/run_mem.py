from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_mem(
    *,
    reads: List[str],
    idx: List[str],
    output: str,
    extra: Optional[str] = None,
    sorting: str = "none",
    sort_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Bwa-mem2 alignment process using the upgraded bwa-mem algorithm.

    Args:
        reads: List of path(s) to FASTQ file(s).
        idx: List of paths to indexed reference genome files. Required index files include “.0123”, “.amb”, “.ann”, “.bwt.2bit.64”, “.pac”.
        output: Path to the output SAM/BAM/CRAM file.
        extra (optional): Additional arguments for bwa-mem2.
        sorting: Sorting method to use - 'none', 'samtools', or 'picard' (default: 'none').
        sort_extra (optional): Additional arguments for samtools/picard sorting.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/bwa-mem2/mem",
        inputs={"reads": reads, "idx": idx},
        outputs={"output": output},
        params={
            "extra": extra,
            "sorting": sorting,
            "sort_extra": sort_extra,
        },
         
    )


@collect_tool()
def mem(
    *,
    reads: List[str],
    idx: List[str],
    output: str,
    extra: Optional[str] = None,
    sorting: str = "none",
    sort_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Bwa-mem2 alignment process using the upgraded bwa-mem algorithm.

    Args:
        reads: List of path(s) to FASTQ file(s).
        idx: List of paths to indexed reference genome files. Required index files include “.0123”, “.amb”, “.ann”, “.bwt.2bit.64”, “.pac”.
        output: Path to the output SAM/BAM/CRAM file.
        extra (optional): Additional arguments for bwa-mem2.
        sorting: Sorting method to use - 'none', 'samtools', or 'picard' (default: 'none').
        sort_extra (optional): Additional arguments for samtools/picard sorting.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mem(
        reads=reads,
        idx=idx,
        output=output,
        extra=extra,
        sorting=sorting,
        sort_extra=sort_extra,
         
    )
