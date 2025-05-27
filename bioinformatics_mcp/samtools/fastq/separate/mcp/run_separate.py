from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_separate(
    *,
    bam_file: str,
    fastq1: str,
    fastq2: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert a bam file with paired-end reads back to unaligned reads in two separate fastq files using `samtools`.

    Args:
        bam_file: Path to input BAM file containing paired-end reads.
        fastq1: Path to output FASTQ file for first pair of reads.
        fastq2: Path to output FASTQ file for second pair of reads.
        extra (optional): Additional arguments for `samtools fastq`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/samtools/fastq/separate",
        inputs={"bam_file": bam_file},
        outputs={"fastq1": fastq1, "fastq2": fastq2},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def separate(
    *,
    bam_file: str,
    fastq1: str,
    fastq2: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert a bam file with paired-end reads back to unaligned reads in two separate fastq files using `samtools`.

    Args:
        bam_file: Path to input BAM file containing paired-end reads.
        fastq1: Path to output FASTQ file for first pair of reads.
        fastq2: Path to output FASTQ file for second pair of reads.
        extra (optional): Additional arguments for `samtools fastq`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_separate(
        bam_file=bam_file, fastq1=fastq1, fastq2=fastq2, extra=extra,      
    )
