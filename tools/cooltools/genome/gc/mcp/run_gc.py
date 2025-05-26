from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_gc(
    *,
    bed_file: str,
    genome_fasta: str,
    output_tsv: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate GC content for a genome in bins.

    Args:
        bed_file: Path to the input .bed file with bin coordinates.
        genome_fasta: Path to the input fasta file with the genome sequence.
        output_tsv: Path to the output .tsv file with GC content in bins.
        extra (optional): Any additional arguments to pass.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/cooltools/genome/gc",
        inputs=dict(bed_file=bed_file, genome_fasta=genome_fasta),
        outputs=dict(output_tsv=output_tsv),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def gc_tool(
    *,
    bed_file: str,
    genome_fasta: str,
    output_tsv: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate GC content for a genome in bins.

    Args:
        bed_file: Path to the input .bed file with bin coordinates.
        genome_fasta: Path to the input fasta file with the genome sequence.
        output_tsv: Path to the output .tsv file with GC content in bins.
        extra (optional): Any additional arguments to pass.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_gc(
        bed_file=bed_file,
        genome_fasta=genome_fasta,
        output_tsv=output_tsv,
        extra=extra,
         
    )
