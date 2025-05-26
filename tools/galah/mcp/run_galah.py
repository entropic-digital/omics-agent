from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_galah(
    *,
    fasta_files: List[str],
    clusters: str,
    repres: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GALAH: More scalable dereplication for metagenome-assembled genomes.

    Args:
        fasta_files: List of input FASTA file paths.
        clusters: Path to the output file containing representative<TAB>member lines.
        repres: Path to the output directory for representative FASTA files.
        extra (optional): Additional program arguments for GALAH.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/galah",
        inputs={"fasta_files": fasta_files},
        outputs={"clusters": clusters, "repres": repres},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def galah(
    *,
    fasta_files: List[str],
    clusters: str,
    repres: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GALAH: More scalable dereplication for metagenome-assembled genomes.

    Args:
        fasta_files: List of input FASTA file paths.
        clusters: Path to the output file containing representative<TAB>member lines.
        repres: Path to the output directory for representative FASTA files.
        extra (optional): Additional program arguments for GALAH.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_galah(
        fasta_files=fasta_files,
        clusters=clusters,
        repres=repres,
        extra=extra,
         
    )
