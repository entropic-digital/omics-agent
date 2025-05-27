from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_collectreadcounts(
    *,
    bam: str,
    intervals: str,
    counts: str,
    mergingRule: Optional[str] = "OVERLAPPING_ONLY",
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collects read counts at specified intervals. The count for each interval is calculated by counting the number of read starts that lie in the interval.

    Args:
        bam: BAM/SAM/CRAM file containing reads.
        intervals: One or more genomic intervals over which to operate.
        counts: Output file for read counts (`tsv` or `hdf5`).
        mergingRule (optional): Interval merging rule for abutting intervals (default: `OVERLAPPING_ONLY`).
        java_opts (optional): Additional arguments to be passed to the java compiler, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/collectreadcounts",
        inputs=dict(bam=bam, intervals=intervals),
        outputs=dict(counts=counts),
        params={
            "mergingRule": mergingRule,
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def collectreadcounts(
    *,
    bam: str,
    intervals: str,
    counts: str,
    mergingRule: Optional[str] = "OVERLAPPING_ONLY",
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collects read counts at specified intervals. The count for each interval is calculated by counting the number of read starts that lie in the interval.

    Args:
        bam: BAM/SAM/CRAM file containing reads.
        intervals: One or more genomic intervals over which to operate.
        counts: Output file for read counts (`tsv` or `hdf5`).
        mergingRule (optional): Interval merging rule for abutting intervals (default: `OVERLAPPING_ONLY`).
        java_opts (optional): Additional arguments to be passed to the java compiler, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collectreadcounts(
        bam=bam,
        intervals=intervals,
        counts=counts,
        mergingRule=mergingRule,
        java_opts=java_opts,
        extra=extra,
         
    )
