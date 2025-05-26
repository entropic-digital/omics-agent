from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bampefragmentsize(
    *,
    bams: List[str],
    histogram: str,
    blacklist: Optional[str] = None,
    raw_lengths: Optional[str] = None,
    label: Optional[List[str]] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Executes deepTools bamPEFragmentSize to calculate fragment sizes for paired-end sequencing BAM files.

    Args:
        bams: List of BAM files (.bam).
        histogram: File path for the output histogram image (.png).
        blacklist (optional): BED file with regions to skip (.bed).
        raw_lengths (optional): File path for the raw fragment lengths output (.tab).
        label (optional): List of labels for plotting or an empty list for automatic labelling.
        extra (optional): Additional parameters to pass to bamPEFragmentSize.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"bams": bams, "blacklist": blacklist} if blacklist else {"bams": bams}
    outputs = (
        {"hist": histogram, "raw": raw_lengths} if raw_lengths else {"hist": histogram}
    )
    params = {"label": label, "extra": extra} if label or extra else {}

    return run_snake_wrapper(
        wrapper="file:tools/deeptools/bampefragmentsize",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def bampefragmentsize(
    *,
    bams: List[str],
    histogram: str,
    blacklist: Optional[str] = None,
    raw_lengths: Optional[str] = None,
    label: Optional[List[str]] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Executes deepTools bamPEFragmentSize to calculate fragment sizes for paired-end sequencing BAM files.

    Args:
        bams: List of BAM files (.bam).
        histogram: File path for the output histogram image (.png).
        blacklist (optional): BED file with regions to skip (.bed).
        raw_lengths (optional): File path for the raw fragment lengths output (.tab).
        label (optional): List of labels for plotting or an empty list for automatic labelling.
        extra (optional): Additional parameters to pass to bamPEFragmentSize.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bampefragmentsize(
        bams=bams,
        histogram=histogram,
        blacklist=blacklist,
        raw_lengths=raw_lengths,
        label=label,
        extra=extra,
         
    )
