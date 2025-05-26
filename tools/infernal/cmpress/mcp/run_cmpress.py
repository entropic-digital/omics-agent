from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_cmpress(
    *,
    cmfile: str,
    output_dir: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Starting from a CM database <cmfile> in standard Infernal-1.1 format, construct binary compressed datafiles for cmscan.

    Infernal ('INFERence of RNA ALignment') is for searching DNA sequence databases for RNA structure and sequence
    similarities. It is an implementation of a special case of profile stochastic context-free grammars called
    covariance models (CMs). A CM is like a sequence profile, but it scores a combination of sequence consensus and
    RNA secondary structure consensus, so in many cases, it is more capable of identifying RNA homologs that conserve
    their secondary structure more than their primary sequence.

    Args:
        cmfile: RNA covariance models (CMs) file path.
        output_dir (optional): Directory to output CMs prepared for use with cmscan.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/infernal/cmpress",
        inputs={"cmfile": cmfile},
        outputs={"output_dir": output_dir} if output_dir else {},
         
    )


@collect_tool()
def cmpress(
    *,
    cmfile: str,
    output_dir: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Starting from a CM database <cmfile> in standard Infernal-1.1 format, construct binary compressed datafiles for cmscan.

    Infernal ('INFERence of RNA ALignment') is for searching DNA sequence databases for RNA structure and sequence
    similarities. It is an implementation of a special case of profile stochastic context-free grammars called
    covariance models (CMs). A CM is like a sequence profile, but it scores a combination of sequence consensus and
    RNA secondary structure consensus, so in many cases, it is more capable of identifying RNA homologs that conserve
    their secondary structure more than their primary sequence.

    Args:
        cmfile: RNA covariance models (CMs) file path.
        output_dir (optional): Directory to output CMs prepared for use with cmscan.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_cmpress(
        cmfile=cmfile,
        output_dir=output_dir,
         
    )
