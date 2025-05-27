from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_align(
    *,
    input_reads: str,
    output_bam: str,
    genome_dir: str,
    threads: int,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads with STAR.

    Args:
        input_reads: Path to the input reads file (e.g., FASTQ).
        output_bam: Path to save the output BAM file.
        genome_dir: Path to the STAR genome directory.
        threads: Number of threads to use.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/star/align",
        inputs={"reads": input_reads},
        outputs={"bam": output_bam},
        params={"genome_dir": genome_dir, "threads": threads, "extra": extra}
        if extra
        else {"genome_dir": genome_dir, "threads": threads},
         
    )


@collect_tool()
def star(
    *,
    input_reads: str,
    output_bam: str,
    genome_dir: str,
    threads: int,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads with STAR.

    Args:
        input_reads: Path to the input reads file (e.g., FASTQ).
        output_bam: Path to save the output BAM file.
        genome_dir: Path to the STAR genome directory.
        threads: Number of threads to use.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_align(
        input_reads=input_reads,
        output_bam=output_bam,
        genome_dir=genome_dir,
        threads=threads,
        extra=extra,
         
    )
