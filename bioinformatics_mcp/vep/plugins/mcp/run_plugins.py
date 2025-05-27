from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_vep_download_plugins(
    *,
    name: str,
    description: str,
    authors: str,
     
) -> subprocess.CompletedProcess:
    """
    Download VEP plugins.

    Args:
        name: Name of the tool.
        description: Description of the tool's functionality.
        authors: Authors of the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/vep/plugins",
        inputs=dict(name=name, description=description, authors=authors),
        params={},
         
    )


@collect_tool()
def vep_download_plugins(
    *,
    name: str,
    description: str,
    authors: str,
     
) -> subprocess.CompletedProcess:
    """
    Download VEP plugins.

    Args:
        name: Name of the tool.
        description: Description of the tool's functionality.
        authors: Authors of the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_vep_download_plugins(
        name=name, description=description, authors=authors,      
    )
