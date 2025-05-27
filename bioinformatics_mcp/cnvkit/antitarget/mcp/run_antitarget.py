from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_antitarget(
    *,
    bed: str,
    accessible: str,
    output_bed: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Derive a BED file for off-target/"antitarget" regions based on the input target BED file.

    Args:
        bed: Path to the input BED file with chromosomal coordinates of the tiled regions.
        accessible: Sequence-accessible coordinates in chromosomes from the reference genome.
        output_bed: Path to the output BED file for antitarget regions.
        extra (optional): Additional parameters passed to the cnvkit antitarget command.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/cnvkit/antitarget",
        inputs=dict(bed=bed, accessible=accessible),
        outputs=dict(bed=output_bed),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def antitarget(
    *,
    bed: str,
    accessible: str,
    output_bed: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Derive a BED file for off-target/"antitarget" regions based on the input target BED file.

    Args:
        bed: Path to the input BED file with chromosomal coordinates of the tiled regions.
        accessible: Sequence-accessible coordinates in chromosomes from the reference genome.
        output_bed: Path to the output BED file for antitarget regions.
        extra (optional): Additional parameters passed to the cnvkit antitarget command.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_antitarget(
        bed=bed, accessible=accessible, output_bed=output_bed, extra=extra,      
    )
