from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_purge_dups(
    *,
    input_paf: str,
    output_bed: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Purge haplotigs and overlaps in an assembly based on read depth.

    Args:
        input_paf: Self-aligned split assembly in PAF format.
        output_bed: Output BED file.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/purge_dups/purge_dups",
        inputs=dict(input_paf=input_paf),
        outputs=dict(output_bed=output_bed),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def purge_dups(
    *,
    input_paf: str,
    output_bed: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Purge haplotigs and overlaps in an assembly based on read depth.

    Args:
        input_paf: Self-aligned split assembly in PAF format.
        output_bed: Output BED file.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_purge_dups(
        input_paf=input_paf, output_bed=output_bed, extra=extra,      
    )
