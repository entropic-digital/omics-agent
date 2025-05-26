from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_fastx(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Converts a SAM, BAM or CRAM file into FASTQ or FASTA format using samtools fastx.

    Args:
        input_file: Path to the input SAM, BAM, or CRAM file.
        output_file: Path to the output FASTQ or FASTA file.
        extra (optional): Additional command-line arguments for samtools (excluding `-@/--threads` or `-o`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/samtools/fastx",
        inputs={"input": input_file},
        outputs={"output": output_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def fastx(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Converts a SAM, BAM or CRAM file into FASTQ or FASTA format using samtools fastx.

    Args:
        input_file: Path to the input SAM, BAM, or CRAM file.
        output_file: Path to the output FASTQ or FASTA file.
        extra (optional): Additional command-line arguments for samtools (excluding `-@/--threads` or `-o`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_fastx(
        input_file=input_file, output_file=output_file, extra=extra,      
    )
