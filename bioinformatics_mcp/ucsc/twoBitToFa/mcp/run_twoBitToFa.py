from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_twoBitToFa(
    *,
    input_twoBit: str,
    output_fa: str,
     
) -> subprocess.CompletedProcess:
    """
    Convert *.2bit file to *.fa file.

    Args:
        input_twoBit: Path to genome *.2bit file.
        output_fa: Path to output *.fa file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/ucsc/twoBitToFa",
        inputs=dict(input_twoBit=input_twoBit),
        outputs=dict(output_fa=output_fa),
         
    )


@collect_tool()
def twoBitToFa(
    *,
    input_twoBit: str,
    output_fa: str,
     
) -> subprocess.CompletedProcess:
    """
    Convert *.2bit file to *.fa file.

    Args:
        input_twoBit: Path to genome *.2bit file.
        output_fa: Path to output *.fa file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_twoBitToFa(
        input_twoBit=input_twoBit,
        output_fa=output_fa,
         
    )
