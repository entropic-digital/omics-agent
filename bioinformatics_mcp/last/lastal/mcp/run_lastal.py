from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_lastal(
    *,
    indexed_db: str,
    sequences: str,
    alignments_output: str,
     
) -> subprocess.CompletedProcess:
    """
    LAST aligns sequences by finding similar regions and is optimized for large datasets.

    Args:
        indexed_db: Path to the indexed database for mapping sequences with LAST.
        sequences: Path to the sequences to align.
        alignments_output: Path to save the resulting sequence alignments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/last/lastal",
        inputs={"indexed_db": indexed_db, "sequences": sequences},
        outputs={"alignments_output": alignments_output},
         
    )


@collect_tool()
def lastal(
    *,
    indexed_db: str,
    sequences: str,
    alignments_output: str,
     
) -> subprocess.CompletedProcess:
    """
    LAST aligns sequences by finding similar regions and is optimized for large datasets.

    Args:
        indexed_db: Path to the indexed database for mapping sequences with LAST.
        sequences: Path to the sequences to align.
        alignments_output: Path to save the resulting sequence alignments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_lastal(
        indexed_db=indexed_db,
        sequences=sequences,
        alignments_output=alignments_output,
         
    )
