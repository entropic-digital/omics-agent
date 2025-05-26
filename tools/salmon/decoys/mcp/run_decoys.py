from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_decoys(
    *,
    transcriptome: str,
    genome: str,
    gentrome: str,
    decoys: str,
    threads: Optional[int] = 1,
     
) -> subprocess.CompletedProcess:
    """
    Generate gentrome sequences and gather decoy sequences.

    Args:
        transcriptome: Path to transcriptome sequences, fasta (gz/bz2) formatted.
        genome: Path to genome sequences, fasta (gz/bz2) formatted.
        gentrome: Path to gentrome, fasta (gz/bz2) formatted.
        decoys: Path to text file containing decoy sequence names.
        threads (optional): Number of threads for processing. Defaults to 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/salmon/decoys",
        inputs=dict(transcriptome=transcriptome, genome=genome),
        outputs=dict(gentrome=gentrome, decoys=decoys),
        params={"threads": threads},
         
    )


@collect_tool()
def decoys(
    *,
    transcriptome: str,
    genome: str,
    gentrome: str,
    decoys: str,
    threads: Optional[int] = 1,
     
) -> subprocess.CompletedProcess:
    """
    MCP Tool to generate gentrome sequences and gather decoy sequences.

    Args:
        transcriptome: Path to transcriptome sequences, fasta (gz/bz2) formatted.
        genome: Path to genome sequences, fasta (gz/bz2) formatted.
        gentrome: Path to gentrome, fasta (gz/bz2) formatted.
        decoys: Path to text file containing decoy sequence names.
        threads (optional): Number of threads for processing. Defaults to 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_decoys(
        transcriptome=transcriptome,
        genome=genome,
        gentrome=gentrome,
        decoys=decoys,
        threads=threads,
         
    )
