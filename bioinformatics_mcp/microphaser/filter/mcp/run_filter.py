from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_filter(
    *,
    neopeptides_fasta: str,
    information_tsv: str,
    sample_specific_normal_binary: str,
    filtered_neopeptides_fasta: str,
    corresponding_normal_peptides_fasta: str,
    filtered_information_tsv: str,
    removed_self_identical_peptides_tsv: str,
     
) -> subprocess.CompletedProcess:
    """
    Translate and filter neopeptides from microphaser output.

    Args:
        neopeptides_fasta: Path to the neopeptides FASTA (nucleotide sequences from microphaser somatic).
        information_tsv: Path to the information TSV file (from microphaser somatic).
        sample_specific_normal_binary: Path to the sample-specific normal/wildtype peptides binary file (created using microphaser build).
        filtered_neopeptides_fasta: Path where the filtered neopeptides in amino acid FASTA format should be written.
        corresponding_normal_peptides_fasta: Path where the corresponding normal peptides in amino acid FASTA format should be written.
        filtered_information_tsv: Path where the filtered information TSV file should be written.
        removed_self_identical_peptides_tsv: Path where the self-identical peptides removed from the neopeptide set should be written.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/microphaser/filter",
        inputs=dict(
            neopeptides_fasta=neopeptides_fasta,
            information_tsv=information_tsv,
            sample_specific_normal_binary=sample_specific_normal_binary,
        ),
        outputs=dict(
            filtered_neopeptides_fasta=filtered_neopeptides_fasta,
            corresponding_normal_peptides_fasta=corresponding_normal_peptides_fasta,
            filtered_information_tsv=filtered_information_tsv,
            removed_self_identical_peptides_tsv=removed_self_identical_peptides_tsv,
        ),
         
    )


@collect_tool()
def filter(
    *,
    neopeptides_fasta: str,
    information_tsv: str,
    sample_specific_normal_binary: str,
    filtered_neopeptides_fasta: str,
    corresponding_normal_peptides_fasta: str,
    filtered_information_tsv: str,
    removed_self_identical_peptides_tsv: str,
     
) -> subprocess.CompletedProcess:
    """
    Translate and filter neopeptides from microphaser output.

    Args:
        neopeptides_fasta: Path to the neopeptides FASTA (nucleotide sequences from microphaser somatic).
        information_tsv: Path to the information TSV file (from microphaser somatic).
        sample_specific_normal_binary: Path to the sample-specific normal/wildtype peptides binary file (created using microphaser build).
        filtered_neopeptides_fasta: Path where the filtered neopeptides in amino acid FASTA format should be written.
        corresponding_normal_peptides_fasta: Path where the corresponding normal peptides in amino acid FASTA format should be written.
        filtered_information_tsv: Path where the filtered information TSV file should be written.
        removed_self_identical_peptides_tsv: Path where the self-identical peptides removed from the neopeptide set should be written.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_filter(
        neopeptides_fasta=neopeptides_fasta,
        information_tsv=information_tsv,
        sample_specific_normal_binary=sample_specific_normal_binary,
        filtered_neopeptides_fasta=filtered_neopeptides_fasta,
        corresponding_normal_peptides_fasta=corresponding_normal_peptides_fasta,
        filtered_information_tsv=filtered_information_tsv,
        removed_self_identical_peptides_tsv=removed_self_identical_peptides_tsv,
         
    )
