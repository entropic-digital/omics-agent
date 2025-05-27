from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_build_reference(
    *,
    peptide_reference: str,
    output_fasta: str,
    output_binary: str,
     
) -> subprocess.CompletedProcess:
    """
    Create a reference of all normal peptides in a sample.

    Args:
        peptide_reference: File path to nucleotide sequences from microphaser germline.
        output_fasta: File path to save peptide reference in amino acid FASTA format.
        output_binary: File path to save binary peptide reference for filtering.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/microphaser/build_reference",
        inputs={"peptide_reference": peptide_reference},
        outputs={"output_fasta": output_fasta, "output_binary": output_binary},
         
    )


@collect_tool()
def build_reference(
    *,
    peptide_reference: str,
    output_fasta: str,
    output_binary: str,
     
) -> subprocess.CompletedProcess:
    """
    Create a reference of all normal peptides in a sample.

    Args:
        peptide_reference: File path to nucleotide sequences from microphaser germline.
        output_fasta: File path to save peptide reference in amino acid FASTA format.
        output_binary: File path to save binary peptide reference for filtering.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_build_reference(
        peptide_reference=peptide_reference,
        output_fasta=output_fasta,
        output_binary=output_binary,
         
    )
