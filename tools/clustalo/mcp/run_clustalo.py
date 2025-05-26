from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_clustalo(
    *,
    input_sequences: str,
    output_alignment: str,
    format: str,
    threads: Optional[int] = 1,
     
) -> subprocess.CompletedProcess:
    """
    Multiple alignment of nucleic acid and protein sequences using Clustal Omega.

    Args:
        input_sequences: Path to the input sequence file (e.g., FASTA format).
        output_alignment: Path to the output alignment file.
        format: Alignment format, such as 'fasta', 'clu', etc.
        threads (optional): Number of threads to use. Defaults to 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/clustalo",
        inputs=dict(input_sequences=input_sequences),
        outputs=dict(output_alignment=output_alignment),
        params={"format": format, "threads": threads},
         
    )


@collect_tool()
def clustalo(
    *,
    input_sequences: str,
    output_alignment: str,
    format: str,
    threads: Optional[int] = 1,
     
) -> subprocess.CompletedProcess:
    """
    Multiple alignment of nucleic acid and protein sequences using Clustal Omega.

    Args:
        input_sequences: Path to the input sequence file (e.g., FASTA format).
        output_alignment: Path to the output alignment file.
        format: Alignment format, such as 'fasta', 'clu', etc.
        threads (optional): Number of threads to use. Defaults to 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_clustalo(
        input_sequences=input_sequences,
        output_alignment=output_alignment,
        format=format,
        threads=threads,
         
    )
