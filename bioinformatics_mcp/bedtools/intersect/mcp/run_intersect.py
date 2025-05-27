from typing import Optional, Union, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_intersect(
    *,
    left: str,
    right: Union[str, List[str]],
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Intersect BED/BAM/VCF files with bedtools.

    Args:
        left: Path to the left region file. Each feature in the left region file
              is compared to the right region(s) file(s) in search of overlaps.
              (BAM/BED/GFF/VCF formatted)
        right: Path or list of paths to region(s) file(s). (BAM/BED/GFF/VCF formatted)
        output: Path to the intersection.
        extra (optional): Additional program arguments (except `-a` (left) and `-b` (right)).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bedtools/intersect",
        inputs={"left": left, "right": right},
        outputs={"output": output},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def intersectBed(
    *,
    left: str,
    right: Union[str, List[str]],
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Intersect BED/BAM/VCF files with bedtools.

    Args:
        left: Path to the left region file. Each feature in the left region file
              is compared to the right region(s) file(s) in search of overlaps.
              (BAM/BED/GFF/VCF formatted)
        right: Path or list of paths to region(s) file(s). (BAM/BED/GFF/VCF formatted)
        output: Path to the intersection.
        extra (optional): Additional program arguments (except `-a` (left) and `-b` (right)).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_intersect(left=left, right=right, output=output, extra=extra,      )
