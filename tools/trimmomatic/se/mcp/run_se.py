from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_se(
    *,
    input_fastq: str,
    output_fastq: str,
    adapter_sequences: Optional[str] = None,
    min_length: Optional[int] = None,
    phred_quality: Optional[int] = None,
    threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Trim single-end reads with trimmomatic.

    Args:
        input_fastq: Path to the input FASTQ file.
        output_fastq: Path to the output FASTQ file.
        adapter_sequences (optional): Path to the adapter sequences file.
        min_length (optional): Minimum read length to keep.
        phred_quality (optional): Minimum quality threshold.
        threads: Number of threads to use. Defaults to 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/trimmomatic/se",
        inputs={"input_fastq": input_fastq},
        outputs={"output_fastq": output_fastq},
        params={
            "adapter_sequences": adapter_sequences,
            "min_length": min_length,
            "phred_quality": phred_quality,
            "threads": threads,
        },
         
    )


@collect_tool()
def trimmomatic_se(
    *,
    input_fastq: str,
    output_fastq: str,
    adapter_sequences: Optional[str] = None,
    min_length: Optional[int] = None,
    phred_quality: Optional[int] = None,
    threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Trim single-end reads with trimmomatic.

    Args:
        input_fastq: Path to the input FASTQ file.
        output_fastq: Path to the output FASTQ file.
        adapter_sequences (optional): Path to the adapter sequences file.
        min_length (optional): Minimum read length to keep.
        phred_quality (optional): Minimum quality threshold.
        threads: Number of threads to use. Defaults to 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_se(
        input_fastq=input_fastq,
        output_fastq=output_fastq,
        adapter_sequences=adapter_sequences,
        min_length=min_length,
        phred_quality=phred_quality,
        threads=threads,
         
    )
