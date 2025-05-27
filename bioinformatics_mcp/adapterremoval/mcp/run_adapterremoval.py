from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_adapterremoval(
    *,
    sample: Optional[str] = None,
    fq: Optional[str] = None,
    fq1: Optional[str] = None,
    fq2: Optional[str] = None,
    singleton: Optional[str] = None,
    collapsed: Optional[str] = None,
    collapsed_trunc: Optional[str] = None,
    discarded: Optional[str] = None,
    settings: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run AdapterRemoval tool for adapter trimming, identification, and read merging.

    Args:
        sample: Path to the raw FASTQ file with R1 reads. For paired-end (PE), include R2 reads as well.
        fq: Path to generate single FASTQ file (SE only).
        fq1: Path to output FASTQ file for R1 reads (PE only).
        fq2: Path to output FASTQ file for R2 reads (PE only).
        singleton: Path to output FASTQ file containing singleton reads (PE only).
        collapsed: Path to output FASTQ file containing collapsed overlapping mate-pairs (PE only).
        collapsed_trunc: Path to output FASTQ file containing quality-trimmed collapsed reads (PE only).
        discarded: Path to output FASTQ file containing reads that did not pass filters.
        settings: Path to generate settings and statistics output file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/adapterremoval",
        inputs=dict(sample=sample),
        outputs=dict(
            fq=fq,
            fq1=fq1,
            fq2=fq2,
            singleton=singleton,
            collapsed=collapsed,
            collapsed_trunc=collapsed_trunc,
            discarded=discarded,
            settings=settings,
        ),
         
    )


@collect_tool()
def adapterremoval(
    *,
    sample: Optional[str] = None,
    fq: Optional[str] = None,
    fq1: Optional[str] = None,
    fq2: Optional[str] = None,
    singleton: Optional[str] = None,
    collapsed: Optional[str] = None,
    collapsed_trunc: Optional[str] = None,
    discarded: Optional[str] = None,
    settings: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    AdapterRemoval tool for rapid adapter trimming, identification, and read merging.

    Args:
        sample: Path to the raw FASTQ file with R1 reads. For paired-end (PE), include R2 reads as well.
        fq: Path to generate single FASTQ file (SE only).
        fq1: Path to output FASTQ file for R1 reads (PE only).
        fq2: Path to output FASTQ file for R2 reads (PE only).
        singleton: Path to output FASTQ file containing singleton reads (PE only).
        collapsed: Path to output FASTQ file containing collapsed overlapping mate-pairs (PE only).
        collapsed_trunc: Path to output FASTQ file containing quality-trimmed collapsed reads (PE only).
        discarded: Path to output FASTQ file containing reads that did not pass filters.
        settings: Path to generate settings and statistics output file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_adapterremoval(
        sample=sample,
        fq=fq,
        fq1=fq1,
        fq2=fq2,
        singleton=singleton,
        collapsed=collapsed,
        collapsed_trunc=collapsed_trunc,
        discarded=discarded,
        settings=settings,
         
    )
