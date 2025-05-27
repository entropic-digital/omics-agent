from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_setupreference(
    *,
    reference: str,
    optional_param: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GRIDSS setupreference - a once-off setup to generate additional files based on a reference genome.

    Args:
        reference: Path to the reference genome file.
        optional_param (optional): Additional optional parameter for setupreference.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gridss/setupreference",
        inputs=dict(reference=reference),
        params={"optional_param": optional_param} if optional_param else {},
         
    )


@collect_tool()
def setupreference(
    *,
    reference: str,
    optional_param: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GRIDSS setupreference - a once-off setup to generate additional files based on a reference genome.

    Args:
        reference: Path to the reference genome file.
        optional_param (optional): Additional optional parameter for setupreference.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_setupreference(
        reference=reference, optional_param=optional_param,      
    )
