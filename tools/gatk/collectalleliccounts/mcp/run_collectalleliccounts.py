from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_collectalleliccounts(
    *,
    bam: str,
    intervals: str,
    ref: str,
    counts: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collects reference and alternate allele counts at specified sites.

    Args:
        bam: BAM/SAM/CRAM file containing reads.
        intervals: One or more genomic intervals over which to operate.
        ref: Reference FASTA file.
        counts: Output file - tab-separated values (TSV) with allelic counts and a SAM-style header.
        java_opts (optional): Additional arguments to be passed to the Java compiler,
            e.g., "-XX:ParallelGCThreads=10" (not for `-XmX` or `-Djava.io.tmpdir`).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/collectalleliccounts",
        inputs=dict(bam=bam, intervals=intervals, ref=ref),
        outputs=dict(counts=counts),
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def collectalleliccounts(
    *,
    bam: str,
    intervals: str,
    ref: str,
    counts: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collects reference and alternate allele counts at specified sites (GATK CollectAllelicCounts).

    Args:
        bam: BAM/SAM/CRAM file containing reads.
        intervals: One or more genomic intervals over which to operate.
        ref: Reference FASTA file.
        counts: Output file - tab-separated values (TSV) with allelic counts and a SAM-style header.
        java_opts (optional): Additional arguments to be passed to the Java compiler,
            e.g., "-XX:ParallelGCThreads=10" (not for `-XmX` or `-Djava.io.tmpdir`).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collectalleliccounts(
        bam=bam,
        intervals=intervals,
        ref=ref,
        counts=counts,
        java_opts=java_opts,
        extra=extra,
         
    )
