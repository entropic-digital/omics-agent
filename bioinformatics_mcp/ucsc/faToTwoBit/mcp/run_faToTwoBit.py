from typing import List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_faToTwoBit(
    *,
    input_paths: List[str],
    output_path: str,
     
) -> subprocess.CompletedProcess:
    """
    Convert *.fa or *.fa.gz genome files into *.2bit format.

    Args:
        input_paths: List of paths to genome *.fa or *.fa.gz files.
        output_path: Path to the output file with *.2bit extension.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/ucsc/faToTwoBit",
        inputs={"input_paths": input_paths},
        outputs={"output_path": output_path},
         
    )


@collect_tool()
def faToTwoBit(
    *,
    input_paths: List[str],
    output_path: str,
     
) -> subprocess.CompletedProcess:
    """
    Convert *.fa or *.fa.gz genome files into *.2bit format.

    Args:
        input_paths: List of paths to genome *.fa or *.fa.gz files.
        output_path: Path to the output file with *.2bit extension.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_faToTwoBit(input_paths=input_paths, output_path=output_path,      )
