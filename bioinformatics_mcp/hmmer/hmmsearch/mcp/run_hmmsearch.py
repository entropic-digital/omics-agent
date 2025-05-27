from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_hmmsearch(
    *,
    hmm_profiles: str,
    sequence_database: str,
    matches_output: str,
     
) -> subprocess.CompletedProcess:
    """
    HMMER hmmsearch: search profile(s) against a sequence database.

    Args:
        hmm_profiles (str): Path to the HMM profiles file.
        sequence_database (str): Path to the sequence database file.
        matches_output (str): Path where matches output will be stored.
  
    Returns:
        subprocess.CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/hmmer/hmmsearch",
        inputs=dict(
            hmm_profiles=hmm_profiles,
            sequence_database=sequence_database,
        ),
        outputs=dict(
            matches_output=matches_output,
        ),
         
    )


@collect_tool()
def hmmsearch(
    *,
    hmm_profiles: str,
    sequence_database: str,
    matches_output: str,
     
) -> subprocess.CompletedProcess:
    """
    HMMER hmmsearch: search profile(s) against a sequence database.

    Args:
        hmm_profiles (str): Path to the HMM profiles file.
        sequence_database (str): Path to the sequence database file.
        matches_output (str): Path where matches output will be stored.
  
    Returns:
        subprocess.CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_hmmsearch(
        hmm_profiles=hmm_profiles,
        sequence_database=sequence_database,
        matches_output=matches_output,
         
    )
