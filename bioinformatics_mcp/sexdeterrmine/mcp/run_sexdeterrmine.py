from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_sexdeterrmine(
    *,
    depth: str,
    output: str,
     
) -> subprocess.CompletedProcess:
    """
    Calculate the relative coverage of X and Y chromosomes, and their associated error bars, out of capture data.

    Args:
        depth: Path to samtools depths file across multiple samples with a header line giving sample names.
        output: Path to the result table.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/sexdeterrmine",
        inputs=dict(depth=depth),
        outputs=dict(output=output),
        params={},
         
    )


@collect_tool()
def sexdeterrmine(
    *,
    depth: str,
    output: str,
     
) -> subprocess.CompletedProcess:
    """
    Calculate the relative coverage of X and Y chromosomes, and their associated error bars, out of capture data.

    Args:
        depth: Path to samtools depths file across multiple samples with a header line giving sample names.
        output: Path to the result table.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_sexdeterrmine(
        depth=depth,
        output=output,
         
    )
