from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_verifybamid2(
    *,
    bam_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run verifybamid2.

    Args:
        bam_file: Path to the input BAM file.
        extra (optional): Additional arguments to be passed to the program.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/verifybamid/verifybamid2",
        inputs=dict(bam_file=bam_file),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def verifybamid2(
    *,
    bam_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run verifybamid2.

    Args:
        bam_file: Path to the input BAM file.
        extra (optional): Additional arguments to be passed to the program.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_verifybamid2(bam_file=bam_file, extra=extra,      )
