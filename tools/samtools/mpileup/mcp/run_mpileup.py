from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_mpileup(
    *,
    bam_file: str,
    reference_fasta: Optional[str] = None,
    region: Optional[str] = None,
    output_path: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate pileup using samtools.

    Args:
        bam_file: Path to the input BAM file.
        reference_fasta (optional): Path to the reference genome in FASTA format.
        region (optional): Genomic region for mpileup (e.g., "chr1:1000-2000").
        output_path: Path to write output pileup file.
        extra (optional): Additional command-line parameters to pass to mpileup.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/samtools/mpileup",
        inputs={"bam_file": bam_file, "reference_fasta": reference_fasta}
        if reference_fasta
        else {"bam_file": bam_file},
        outputs={"output_path": output_path},
        params={"region": region, "extra": extra} if any([region, extra]) else {},
         
    )


@collect_tool()
def mpileup(
    *,
    bam_file: str,
    reference_fasta: Optional[str] = None,
    region: Optional[str] = None,
    output_path: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate pileup using samtools.

    Args:
        bam_file: Path to the input BAM file.
        reference_fasta (optional): Path to the reference genome in FASTA format.
        region (optional): Genomic region for mpileup (e.g., "chr1:1000-2000").
        output_path: Path to write output pileup file.
        extra (optional): Additional command-line parameters to pass to mpileup.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mpileup(
        bam_file=bam_file,
        reference_fasta=reference_fasta,
        region=region,
        output_path=output_path,
        extra=extra,
         
    )
