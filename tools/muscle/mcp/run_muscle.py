from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_muscle(
    *,
    fasta_file: str,
    alignment_file: str,
    super5: Optional[bool] = None,
     
) -> subprocess.CompletedProcess:
    """
    Build multiple sequence alignments using MUSCLE.

    Args:
        fasta_file: Path to the input FASTA file containing sequences to align.
        alignment_file: Path to save the alignment file (output).
        super5 (optional): Specifies whether to use the Super5 algorithm to align sequences.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/muscle",
        inputs=dict(fasta_file=fasta_file),
        outputs=dict(alignment_file=alignment_file),
        params={"super5": super5} if super5 is not None else {},
         
    )


@collect_tool()
def muscle(
    *,
    fasta_file: str,
    alignment_file: str,
    super5: Optional[bool] = None,
     
) -> subprocess.CompletedProcess:
    """
    Build multiple sequence alignments using MUSCLE.

    Args:
        fasta_file: Path to the input FASTA file containing sequences to align.
        alignment_file: Path to save the alignment file (output).
        super5 (optional): Specifies whether to use the Super5 algorithm to align sequences.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_muscle(
        fasta_file=fasta_file, alignment_file=alignment_file, super5=super5,      
    )
