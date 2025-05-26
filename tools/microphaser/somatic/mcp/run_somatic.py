from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_somatic(
    *,
    bam_file: str,
    bcf_file: str,
    fasta_reference: str,
    gtf_annotation_file: str,
    mutated_peptide_fasta: str,
    wildtype_peptide_fasta: str,
    information_tsv: str,
     
) -> subprocess.CompletedProcess:
    """
    Predict mutated neopeptides and their wildtype counterparts from NGS data.

    Args:
        bam_file: Path to the input BAM file.
        bcf_file: Path to the input BCF file.
        fasta_reference: Path to the FASTA reference file.
        gtf_annotation_file: Path to the GTF annotation file.
        mutated_peptide_fasta: Path to the output file for mutated peptide FASTA.
        wildtype_peptide_fasta: Path to the output file for wildtype peptide FASTA.
        information_tsv: Path to the output TSV file with additional information.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/microphaser/somatic",
        inputs={
            "bam_file": bam_file,
            "bcf_file": bcf_file,
            "fasta_reference": fasta_reference,
            "gtf_annotation_file": gtf_annotation_file,
        },
        outputs={
            "mutated_peptide_fasta": mutated_peptide_fasta,
            "wildtype_peptide_fasta": wildtype_peptide_fasta,
            "information_tsv": information_tsv,
        },
         
    )


@collect_tool()
def somatic(
    *,
    bam_file: str,
    bcf_file: str,
    fasta_reference: str,
    gtf_annotation_file: str,
    mutated_peptide_fasta: str,
    wildtype_peptide_fasta: str,
    information_tsv: str,
     
) -> subprocess.CompletedProcess:
    """
    Predict mutated neopeptides and their wildtype counterparts from NGS data.

    Args:
        bam_file: Path to the input BAM file.
        bcf_file: Path to the input BCF file.
        fasta_reference: Path to the FASTA reference file.
        gtf_annotation_file: Path to the GTF annotation file.
        mutated_peptide_fasta: Path to the output file for mutated peptide FASTA.
        wildtype_peptide_fasta: Path to the output file for wildtype peptide FASTA.
        information_tsv: Path to the output TSV file with additional information.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_somatic(
        bam_file=bam_file,
        bcf_file=bcf_file,
        fasta_reference=fasta_reference,
        gtf_annotation_file=gtf_annotation_file,
        mutated_peptide_fasta=mutated_peptide_fasta,
        wildtype_peptide_fasta=wildtype_peptide_fasta,
        information_tsv=information_tsv,
         
    )
