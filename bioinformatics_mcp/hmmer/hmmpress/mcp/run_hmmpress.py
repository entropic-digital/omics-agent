from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_hmmpress(
    *,
    hmm_database: str,
    binary_format_hmm_database: str,
     
) -> subprocess.CompletedProcess:
    """
    Format an HMM database into a binary format for hmmscan.

    Args:
        hmm_database: Input HMM database file.
        binary_format_hmm_database: Output binary format HMM database file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/hmmer/hmmpress",
        inputs=dict(hmm_database=hmm_database),
        outputs=dict(binary_format_hmm_database=binary_format_hmm_database),
         
    )


@collect_tool()
def hmmpress(
    *,
    hmm_database: str,
    binary_format_hmm_database: str,
     
) -> subprocess.CompletedProcess:
    """
    Format an HMM database into a binary format for hmmscan.

    Args:
        hmm_database: Input HMM database file.
        binary_format_hmm_database: Output binary format HMM database file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_hmmpress(
        hmm_database=hmm_database,
        binary_format_hmm_database=binary_format_hmm_database,
         
    )
