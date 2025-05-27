from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_bgzip(
    *,
    file: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Block compression/decompression utility.

    Args:
        file: The input file to be compressed or decompressed.
        output: The resulting compressed or decompressed file.
        extra (optional): Additional bgzip parameters.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bgzip",
        inputs={"file": file},
        outputs={"output": output},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def bgzip(
    *,
    file: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Block compression/decompression utility.

    Args:
        file: The input file to be compressed or decompressed.
        output: The resulting compressed or decompressed file.
        extra (optional): Additional bgzip parameters.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bgzip(
        file=file,
        output=output,
        extra=extra,
         
    )
