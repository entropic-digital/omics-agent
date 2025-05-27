from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    protein_fasta_file: str,
    output_index_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Index a protein fasta file for mapping with PALADIN.

    PALADIN is a protein sequence alignment tool designed for the accurate functional
    characterization of metagenomes.

    Args:
        protein_fasta_file: Path to the input protein FASTA file.
        output_index_file: Path to the output indexed file for PALADIN mapping.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/paladin/index",
        inputs=dict(protein_fasta_file=protein_fasta_file),
        outputs=dict(output_index_file=output_index_file),
         
    )


@collect_tool()
def paladin_index(
    *,
    protein_fasta_file: str,
    output_index_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Index a protein fasta file for mapping with PALADIN.

    This tool indexes a protein FASTA file to prepare it for mapping with PALADIN, a
    protein sequence alignment tool designed for functional profiling of metagenomes.

    Args:
        protein_fasta_file: Path to the input protein FASTA file.
        output_index_file: Path to the output indexed file for PALADIN mapping.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        protein_fasta_file=protein_fasta_file,
        output_index_file=output_index_file,
         
    )
