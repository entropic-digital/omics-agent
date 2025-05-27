from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_complement(
    *,
    in_file: str,
    genome: str,
    out_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Maps all regions of the genome which are not covered by the input.

    Args:
        in_file: Interval file (BED/GFF/VCF) containing regions of interest.
        genome: Genome file specifying the chromosome sizes.
        out_file: Output file to store the complemented regions in BED/GFF/VCF format.
        extra (optional): Additional program arguments (except `-i` and `-g`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bedtools/complement",
        inputs={"in_file": in_file, "genome": genome},
        outputs={"out_file": out_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def complementBed(
    *,
    in_file: str,
    genome: str,
    out_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Maps all regions of the genome which are not covered by the input.

    Args:
        in_file: Interval file (BED/GFF/VCF) containing regions of interest.
        genome: Genome file specifying the chromosome sizes.
        out_file: Output file to store the complemented regions in BED/GFF/VCF format.
        extra (optional): Additional program arguments (except `-i` and `-g`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_complement(
        in_file=in_file,
        genome=genome,
        out_file=out_file,
        extra=extra,
         
    )
