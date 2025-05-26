from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


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
        wrapper="file:tools/vep/plugins",
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
