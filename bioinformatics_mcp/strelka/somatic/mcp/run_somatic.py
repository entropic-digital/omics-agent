from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_somatic(
    *,
    tumor_bam: str,
    tumor_bam_index: str,
    reference_fasta: str,
    reference_fasta_index: str,
    normal_bam: Optional[str] = None,
    normal_bam_index: Optional[str] = None,
    output_statistics: str,
    output_variants: str,
     
) -> subprocess.CompletedProcess:
    """
    Runs the Strelka tool for somatic and germline small variant calling.

    Args:
        tumor_bam: Path to the tumor bam file.
        tumor_bam_index: Path to the tumor bam index file.
        reference_fasta: Path to the reference genome sequence in fasta format.
        reference_fasta_index: Path to the index for the reference genome fasta file.
        normal_bam (optional): Path to the optional normal bam file for somatic calling.
        normal_bam_index (optional): Path to the optional normal bam index file.
        output_statistics: Path to save statistics about the calling results.
        output_variants: Path to save the called variants.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "tumor_bam": tumor_bam,
        "tumor_bam_index": tumor_bam_index,
        "reference_fasta": reference_fasta,
        "reference_fasta_index": reference_fasta_index,
    }

    if normal_bam and normal_bam_index:
        inputs.update(
            {
                "normal_bam": normal_bam,
                "normal_bam_index": normal_bam_index,
            }
        )

    outputs = {
        "output_statistics": output_statistics,
        "output_variants": output_variants,
    }

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/strelka/somatic",
        inputs=inputs,
        outputs=outputs,
         
    )


@collect_tool()
def somatic(
    *,
    tumor_bam: str,
    tumor_bam_index: str,
    reference_fasta: str,
    reference_fasta_index: str,
    normal_bam: Optional[str] = None,
    normal_bam_index: Optional[str] = None,
    output_statistics: str,
    output_variants: str,
     
) -> subprocess.CompletedProcess:
    """
    Runs the Strelka tool for somatic and germline small variant calling.

    Args:
        tumor_bam: Path to the tumor bam file.
        tumor_bam_index: Path to the tumor bam index file.
        reference_fasta: Path to the reference genome sequence in fasta format.
        reference_fasta_index: Path to the index for the reference genome fasta file.
        normal_bam (optional): Path to the optional normal bam file for somatic calling.
        normal_bam_index (optional): Path to the optional normal bam index file.
        output_statistics: Path to save statistics about the calling results.
        output_variants: Path to save the called variants.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_somatic(
        tumor_bam=tumor_bam,
        tumor_bam_index=tumor_bam_index,
        reference_fasta=reference_fasta,
        reference_fasta_index=reference_fasta_index,
        normal_bam=normal_bam,
        normal_bam_index=normal_bam_index,
        output_statistics=output_statistics,
        output_variants=output_variants,
         
    )
