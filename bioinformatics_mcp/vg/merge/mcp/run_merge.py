from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_merge(
    *,
    input_graphs: str,
    output_merged: str,
    temp_dir: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate a joint id space across each graph and merge them all.

    Args:
        input_graphs: Path to the input graphical files to be merged.
        output_merged: Path to the output merged graph file.
        temp_dir (optional): Path to the temporary directory for intermediate files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/vg/merge",
        inputs=dict(input_graphs=input_graphs),
        outputs=dict(output_merged=output_merged),
        params={"temp_dir": temp_dir} if temp_dir else {},
         
    )


@collect_tool()
def merge(
    *,
    input_graphs: str,
    output_merged: str,
    temp_dir: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate a joint id space across each graph and merge them all.

    Args:
        input_graphs: Path to the input graphical files to be merged.
        output_merged: Path to the output merged graph file.
        temp_dir (optional): Path to the temporary directory for intermediate files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_merge(
        input_graphs=input_graphs,
        output_merged=output_merged,
        temp_dir=temp_dir,
         
    )
