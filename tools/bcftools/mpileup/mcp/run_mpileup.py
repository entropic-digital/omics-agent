from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_mpileup(
    *,
    alignments: str,
    ref: str,
    reference_genome_index: Optional[str] = None,
    pileup_file: str,
    uncompressed_bcf: bool = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate VCF or BCF containing genotype likelihoods for one or multiple alignment (BAM or CRAM) files.

    Args:
        alignments: SAM/BAM/CRAM file(s) to process.
        ref: Path to the reference genome.
        reference_genome_index (optional): Path to the reference genome index.
        pileup_file: Output file for the pileup results.
        uncompressed_bcf (optional): Generate an uncompressed BCF; ignored otherwise. Default is False.
        extra (optional): Additional arguments to pass to the bcftools mpileup command.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {"uncompressed_bcf": uncompressed_bcf, "extra": extra}
    # Remove entries with None values
    params = {k: v for k, v in params.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:tools/bcftools/mpileup",
        inputs={
            "alignments": alignments,
            "ref": ref,
            "reference_genome_index": reference_genome_index,
        },
        outputs={"pileup_file": pileup_file},
        params=params,
         
    )


@collect_tool()
def mpileup(
    *,
    alignments: str,
    ref: str,
    reference_genome_index: Optional[str] = None,
    pileup_file: str,
    uncompressed_bcf: bool = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate VCF or BCF containing genotype likelihoods for one or multiple alignment (BAM or CRAM) files.

    Args:
        alignments: SAM/BAM/CRAM file(s) to process.
        ref: Path to the reference genome.
        reference_genome_index (optional): Path to the reference genome index.
        pileup_file: Output file for the pileup results.
        uncompressed_bcf (optional): Generate an uncompressed BCF; ignored otherwise. Default is False.
        extra (optional): Additional arguments to pass to the bcftools mpileup command.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mpileup(
        alignments=alignments,
        ref=ref,
        reference_genome_index=reference_genome_index,
        pileup_file=pileup_file,
        uncompressed_bcf=uncompressed_bcf,
        extra=extra,
         
    )
