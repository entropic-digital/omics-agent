from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_interleaved(
    *,
    input_bam: str,
    output_fastq: str,
    extra: Optional[str] = None,
    threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Convert a BAM file back to unaligned reads in a single interleaved FASTQ file using samtools.

    Args:
        input_bam: Path to the input BAM file.
        output_fastq: Path to the output interleaved FASTQ file.
        extra (optional): Additional program arguments for samtools (excluding `-@/--threads` or `-o`).
        threads: Number of threads to use. Defaults to 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/samtools/fastq/interleaved",
        inputs={"input_bam": input_bam},
        outputs={"output_fastq": output_fastq},
        params={"extra": extra, "threads": threads},
         
    )


@collect_tool()
def interleaved(
    *,
    input_bam: str,
    output_fastq: str,
    extra: Optional[str] = None,
    threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Convert a BAM file back to unaligned reads in a single interleaved FASTQ file using samtools.

    Args:
        input_bam: Path to the input BAM file.
        output_fastq: Path to the output interleaved FASTQ file.
        extra (optional): Additional program arguments for samtools (excluding `-@/--threads` or `-o`).
        threads: Number of threads to use. Defaults to 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_interleaved(
        input_bam=input_bam,
        output_fastq=output_fastq,
        extra=extra,
        threads=threads,
         
    )
