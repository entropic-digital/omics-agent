from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_add_species(
    *,
    taxa: str,
    refFasta: str,
    params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Add species-level annotation using DADA2's `addSpecies` function.

    Args:
        taxa: Path to the RDS file containing taxonomic assignments.
        refFasta: Path to the FASTA reference database.
        params (optional): Optional arguments for `addSpecies()`, provided as Python key-value pairs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/dada2/add-species",
        inputs=dict(taxa=taxa, refFasta=refFasta),
        params=params or {},
         
    )


@collect_tool()
def add_species(
    *,
    taxa: str,
    refFasta: str,
    params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Add species-level annotation using DADA2's `addSpecies` function.

    Args:
        taxa: Path to the RDS file containing taxonomic assignments.
        refFasta: Path to the FASTA reference database.
        params (optional): Optional arguments for `addSpecies()`, provided as Python key-value pairs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_add_species(taxa=taxa, refFasta=refFasta, params=params,      )
