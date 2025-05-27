from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_assign_species(
    *,
    seqs: str,
    refFasta: str,
    params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Classify sequences against a reference database using the DADA2 `assignSpecies` function.

    Args:
        seqs: Path to the RDS file containing the chimera-free sequence table.
        refFasta: Path to the genus-species FASTA reference database.
        params (optional): Additional parameters for `assignTaxonomy` function, provided as key=value pairs.
         
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/dada2/assign-species",
        inputs={"seqs": seqs, "refFasta": refFasta},
        params=params or {},
         
    )


@collect_tool()
def assign_species(
    *,
    seqs: str,
    refFasta: str,
    params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Classify sequences against a reference database using the DADA2 `assignSpecies` function.

    Args:
        seqs: Path to the RDS file containing the chimera-free sequence table.
        refFasta: Path to the genus-species FASTA reference database.
        params (optional): Additional parameters for `assignTaxonomy` function, provided as key=value pairs.
         
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_assign_species(
        seqs=seqs,
        refFasta=refFasta,
        params=params,
         
    )
