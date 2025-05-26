from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_liftoff(
    *,
    reference_genome: str,
    target_genome: str,
    annotations: str,
    mapped_annotations: str,
    unmapped_annotations: str,
     
) -> subprocess.CompletedProcess:
    """
    Lift features from one genome assembly to another using Liftoff.

    Args:
        reference_genome: Path to the fasta formatted reference genome file.
        target_genome: Path to the fasta formatted target genome file.
        annotations: Path to the GFF/GTF formatted annotations file.
        mapped_annotations: Path to the output GFF file containing the mapped annotations.
        unmapped_annotations: Path to the output GFF file containing the unmapped annotations.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/liftoff",
        inputs=dict(
            reference_genome=reference_genome,
            target_genome=target_genome,
            annotations=annotations,
        ),
        outputs=dict(
            mapped_annotations=mapped_annotations,
            unmapped_annotations=unmapped_annotations,
        ),
         
    )


@collect_tool()
def liftoff(
    *,
    reference_genome: str,
    target_genome: str,
    annotations: str,
    mapped_annotations: str,
    unmapped_annotations: str,
     
) -> subprocess.CompletedProcess:
    """
    Lift features from one genome assembly to another using Liftoff.

    Args:
        reference_genome: Path to the fasta formatted reference genome file.
        target_genome: Path to the fasta formatted target genome file.
        annotations: Path to the GFF/GTF formatted annotations file.
        mapped_annotations: Path to the output GFF file containing the mapped annotations.
        unmapped_annotations: Path to the output GFF file containing the unmapped annotations.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_liftoff(
        reference_genome=reference_genome,
        target_genome=target_genome,
        annotations=annotations,
        mapped_annotations=mapped_annotations,
        unmapped_annotations=unmapped_annotations,
         
    )
