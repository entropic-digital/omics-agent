from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_xg(
    *,
    variation_graph: str,
    output_xg: str,
    temp_dir: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create an xg index on variation graphs.

    Args:
        variation_graph: Path to the input variation graph file (.vg).
        output_xg: Path to the output xg file.
        temp_dir (optional): Temporary directory for intermediate files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/vg/index/xg",
        inputs=dict(variation_graph=variation_graph),
        outputs=dict(output_xg=output_xg),
        params={"temp_dir": temp_dir} if temp_dir else {},
         
    )


@collect_tool()
def xg(
    *,
    variation_graph: str,
    output_xg: str,
    temp_dir: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Create an xg index on variation graphs.

    Args:
        variation_graph: Path to the input variation graph file (.vg).
        output_xg: Path to the output xg file.
        temp_dir (optional): Temporary directory for intermediate files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_xg(
        variation_graph=variation_graph,
        output_xg=output_xg,
        temp_dir=temp_dir,
         
    )
