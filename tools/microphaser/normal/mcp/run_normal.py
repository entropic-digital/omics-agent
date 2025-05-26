from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_normal(
    *,
    bam_file: str,
    bcf_file: str,
    fasta_reference: str,
    gtf_annotation_file: str,
    peptide_fasta: str,
     
) -> subprocess.CompletedProcess:
    """
    Predict sample-specific normal peptides with integrated germline variants from NGS data.

    Args:
        bam_file: Input BAM file containing aligned reads.
        bcf_file: Input BCF file containing variant calls.
        fasta_reference: Reference genome in FASTA format.
        gtf_annotation_file: GTF annotation file for genomic features.
        peptide_fasta: Output file for sample-specific peptide fasta (nucleotide sequences).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/microphaser/normal",
        inputs=dict(
            bam_file=bam_file,
            bcf_file=bcf_file,
            fasta_reference=fasta_reference,
            gtf_annotation_file=gtf_annotation_file,
        ),
        outputs=dict(peptide_fasta=peptide_fasta),
         
    )


@collect_tool()
def normal(
    *,
    bam_file: str,
    bcf_file: str,
    fasta_reference: str,
    gtf_annotation_file: str,
    peptide_fasta: str,
     
) -> subprocess.CompletedProcess:
    """
    Predict sample-specific normal peptides with integrated germline variants from NGS data.

    Args:
        bam_file: Input BAM file containing aligned reads.
        bcf_file: Input BCF file containing variant calls.
        fasta_reference: Reference genome in FASTA format.
        gtf_annotation_file: GTF annotation file for genomic features.
        peptide_fasta: Output file for sample-specific peptide fasta (nucleotide sequences).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_normal(
        bam_file=bam_file,
        bcf_file=bcf_file,
        fasta_reference=fasta_reference,
        gtf_annotation_file=gtf_annotation_file,
        peptide_fasta=peptide_fasta,
         
    )
