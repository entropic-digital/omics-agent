from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_gfatools(
    *,
    gfa_file: str,
    command: str = "view",
    output_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Tools for manipulating sequence graphs in the GFA and rGFA formats.

    Args:
        gfa_file: Input GFA file.
        command: Command to specify the operation. Options are:
            "view" [default], "stat", "gfa2fa", "gfa2bed", "blacklist",
            "bubble", "asm", "sql", or "version".
        output_file (optional): Path to the output file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gfatools",
        inputs=dict(gfa_file=gfa_file),
        params={"command": command, "output_file": output_file}
        if output_file
        else {"command": command},
         
    )


@collect_tool()
def gfatools(
    *,
    gfa_file: str,
    command: str = "view",
    output_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Tools for manipulating sequence graphs in the GFA and rGFA formats.

    Args:
        gfa_file: Input GFA file.
        command: Command to specify the operation. Options are:
            "view" [default], "stat", "gfa2fa", "gfa2bed", "blacklist",
            "bubble", "asm", "sql", or "version".
        output_file (optional): Path to the output file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_gfatools(
        gfa_file=gfa_file,
        command=command,
        output_file=output_file,
         
    )
