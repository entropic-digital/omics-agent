from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_hmmbuild(
    *,
    sequence_alignment_file: str,
    profile_hmm: str,
     
) -> subprocess.CompletedProcess:
    """
    Construct profile HMM(s) from multiple sequence alignment(s).

    Args:
        sequence_alignment_file: Path to the sequence alignment file.
        profile_hmm: Path to save the generated profile HMM.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/hmmer/hmmbuild",
        inputs={"sequence_alignment_file": sequence_alignment_file},
        outputs={"profile_hmm": profile_hmm},
         
    )


@collect_tool()
def hmmbuild(
    *,
    sequence_alignment_file: str,
    profile_hmm: str,
     
) -> subprocess.CompletedProcess:
    """
    Construct profile HMM(s) from multiple sequence alignment(s).

    Args:
        sequence_alignment_file: Path to the sequence alignment file.
        profile_hmm: Path to save the generated profile HMM.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_hmmbuild(
        sequence_alignment_file=sequence_alignment_file,
        profile_hmm=profile_hmm,
         
    )
