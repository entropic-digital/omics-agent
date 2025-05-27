from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_mem(
    *,
    fastq_files: List[str],
    reference_genome: str,
    output_file: str,
    extra: Optional[str] = None,
    sorting: Optional[str] = "none",
    sort_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads using bwa mem, with optional sorting using samtools or picard.

    Args:
        fastq_files: List of input FASTQ file(s).
        reference_genome: Path to the reference genome.
        output_file: Path to the resulting SAM/BAM/CRAM file.
        extra (optional): Additional arguments for bwa mem.
        sorting (optional): Sorting method ("none", "samtools", "fgbio", or "picard").
        sort_extra (optional): Extra arguments for samtools or picard.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bwa/mem",
        inputs={"fastq_files": fastq_files, "reference_genome": reference_genome},
        outputs={"output_file": output_file},
        params={
            "extra": extra,
            "sorting": sorting,
            "sort_extra": sort_extra,
        },
         
    )


@collect_tool()
def bwa_mem(
    *,
    fastq_files: List[str],
    reference_genome: str,
    output_file: str,
    extra: Optional[str] = None,
    sorting: Optional[str] = "none",
    sort_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads using bwa mem, with optional sorting using samtools or picard.

    Args:
        fastq_files: List of input FASTQ file(s).
        reference_genome: Path to the reference genome.
        output_file: Path to the resulting SAM/BAM/CRAM file.
        extra (optional): Additional arguments for bwa mem.
        sorting (optional): Sorting method ("none", "samtools", "fgbio", or "picard").
        sort_extra (optional): Extra arguments for samtools or picard.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mem(
        fastq_files=fastq_files,
        reference_genome=reference_genome,
        output_file=output_file,
        extra=extra,
        sorting=sorting,
        sort_extra=sort_extra,
         
    )
