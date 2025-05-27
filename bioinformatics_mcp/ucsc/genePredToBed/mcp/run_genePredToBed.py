from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_genePredToBed(
    *,
    input_path: str,
    output_path: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert from genePred to bed format.

    Args:
        input_path: Path to a genePred file.
        output_path: Path to the output bed12 file.
        extra (optional): Optional parameters for `genePredToBed`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/ucsc/genePredToBed",
        inputs={"input": input_path},
        outputs={"output": output_path},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def genePredToBed(
    *,
    input_path: str,
    output_path: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert from genePred to bed format.

    Args:
        input_path: Path to a genePred file.
        output_path: Path to the output bed12 file.
        extra (optional): Optional parameters for `genePredToBed`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_genePredToBed(
        input_path=input_path, output_path=output_path, extra=extra,      
    )
