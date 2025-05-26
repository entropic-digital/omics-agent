from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_getpileupsummaries(
    *,
    bam: str,
    intervals: str,
    variants: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Summarizes counts of reads that support reference, alternate, and other alleles.

    Args:
        bam: Path to BAM file (sorted and indexed)
        intervals: Path to one or more BED genomic intervals over which to operate
        variants: Path to a VCF containing allele frequencies (pbgzipped and tabix indexed)
        output: Path to output table
        extra (optional): Additional parameters
           
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/getpileupsummaries",
        inputs=dict(bam=bam, intervals=intervals, variants=variants),
        outputs=dict(output=output),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def getpileupsummaries(
    *,
    bam: str,
    intervals: str,
    variants: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Summarizes counts of reads that support reference, alternate, and other alleles.

    Args:
        bam: Path to BAM file (sorted and indexed)
        intervals: Path to one or more BED genomic intervals over which to operate
        variants: Path to a VCF containing allele frequencies (pbgzipped and tabix indexed)
        output: Path to output table
        extra (optional): Additional parameters
           
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process
    """
    return run_getpileupsummaries(
        bam=bam,
        intervals=intervals,
        variants=variants,
        output=output,
        extra=extra,
         
    )
