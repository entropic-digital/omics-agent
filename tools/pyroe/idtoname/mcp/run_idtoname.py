from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_idtoname(
    *,
    genome_annotation: str,
    output_mapping: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create a 2-column tab-separated file mapping IDs to names.

    Args:
        genome_annotation: Path to genome annotation (GTF or GFF3).
        output_mapping: Path to gene ID <-> gene names mapping.
        extra (optional): Optional parameters to be passed to pyroe.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/pyroe/idtoname",
        inputs={"genome_annotation": genome_annotation},
        outputs={"output_mapping": output_mapping},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def idtoname(
    *,
    genome_annotation: str,
    output_mapping: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create a 2-column tab-separated file mapping IDs to names.

    Args:
        genome_annotation: Path to genome annotation (GTF or GFF3).
        output_mapping: Path to gene ID <-> gene names mapping.
        extra (optional): Optional parameters to be passed to pyroe.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_idtoname(
        genome_annotation=genome_annotation,
        output_mapping=output_mapping,
        extra=extra,
         
    )
