from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_refgenie(
    *,
    action: str,
    genome: Optional[str] = None,
    tag: Optional[str] = None,
    config: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Deploy biomedical reference datasets via refgenie.

    Args:
        action: The refgenie action to perform (e.g., 'build', 'pull', etc.)
        genome (optional): The genome to target in the action.
        tag (optional): A tag associated with the genome (e.g., 'default', 'latest', etc.)
        config (optional): Path to the refgenie configuration file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/refgenie",
        inputs={
            "action": action,
            "genome": genome,
            "tag": tag,
            "config": config,
        },
        params={},
         
    )


@collect_tool()
def refgenie(
    *,
    action: str,
    genome: Optional[str] = None,
    tag: Optional[str] = None,
    config: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Deploy biomedical reference datasets via refgenie.

    Args:
        action: The refgenie action to perform (e.g., 'build', 'pull', etc.)
        genome (optional): The genome to target in the action.
        tag (optional): A tag associated with the genome (e.g., 'default', 'latest', etc.)
        config (optional): Path to the refgenie configuration file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_refgenie(
        action=action,
        genome=genome,
        tag=tag,
        config=config,
         
    )
