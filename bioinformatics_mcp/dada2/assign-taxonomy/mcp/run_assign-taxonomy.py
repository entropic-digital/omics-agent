from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_assign_taxonomy(
    *,
    seqs: str,
    refFasta: str,
    params: Optional[str] = None,
    output: str,
     
) -> subprocess.CompletedProcess:
    """
    Classify sequences against a reference database using dada2 `assignTaxonomy` function.

    Args:
        seqs: Path to the input RDS file containing the chimera-free sequence table.
        refFasta: Path to the FASTA reference database.
        params (optional): Optional parameters for `assignTaxonomy`
            provided as Python `key=value` pairs.
        output: Path to the output RDS file containing the taxonomic assignments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/dada2/assign-taxonomy",
        inputs=dict(seqs=seqs, refFasta=refFasta),
        params=dict(params=params) if params else {},
        outputs=dict(output=output),
         
    )


@collect_tool()
def assign_taxonomy(
    *,
    seqs: str,
    refFasta: str,
    params: Optional[str] = None,
    output: str,
     
) -> subprocess.CompletedProcess:
    """
    Classify sequences against a reference database using dada2 `assignTaxonomy` function.

    Args:
        seqs: Path to the input RDS file containing the chimera-free sequence table.
        refFasta: Path to the FASTA reference database.
        params (optional): Optional parameters for `assignTaxonomy`
            provided as Python `key=value` pairs.
        output: Path to the output RDS file containing the taxonomic assignments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_assign_taxonomy(
        seqs=seqs,
        refFasta=refFasta,
        params=params,
        output=output,
         
    )
