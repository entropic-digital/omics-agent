from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_slop(
    *,
    input_file: str,
    output_file: str,
    genome: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Increase the size of each feature in a BED/BAM/VCF file by a specified factor.

    Args:
        input_file: Path to an interval file (BED/GFF/VCF).
        output_file: Path to the expanded intervals file.
        genome: Path to a genome file.
        extra (optional): Additional program arguments (except for `-i` or `-g`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bedtools/slop",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file},
        params={"genome": genome, "extra": extra} if extra else {"genome": genome},
         
    )


@collect_tool()
def slopBed(
    *,
    input_file: str,
    output_file: str,
    genome: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Increase the size of each feature in a BED/BAM/VCF file by a specified factor.

    Args:
        input_file: Path to an interval file (BED/GFF/VCF).
        output_file: Path to the expanded intervals file.
        genome: Path to a genome file.
        extra (optional): Additional program arguments (except for `-i` or `-g`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_slop(
        input_file=input_file,
        output_file=output_file,
        genome=genome,
        extra=extra,
         
    )
