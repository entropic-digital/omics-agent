from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_prepare(
    *,
    output_file: str,
    citation: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Download and prepare UniProt references for PALADIN mapping. PALADIN is a protein sequence
    alignment tool designed for the accurate functional characterization of metagenomes.

    Args:
        output_file: Path to the prepared UniProt file for mapping with PALADIN.
        citation (optional): Citation details for PALADIN usage.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/paladin/prepare",
        inputs={},
        outputs={"output_file": output_file},
        params={"citation": citation} if citation else {},
         
    )


@collect_tool()
def prepare(
    *,
    output_file: str,
    citation: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Download and prepare UniProt references for PALADIN mapping. PALADIN is a protein sequence
    alignment tool designed for the accurate functional characterization of metagenomes.

    Args:
        output_file: Path to the prepared UniProt file for mapping with PALADIN.
        citation (optional): Citation details for PALADIN usage.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_prepare(output_file=output_file, citation=citation,      )
