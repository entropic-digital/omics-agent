from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_deepvariant(
    *,
    fasta: str,
    bam: str,
    vcf: str,
    visual_report_html: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call genetic variants using deep neural network.

    Args:
        fasta: Path to the input FASTA file.
        bam: Path to the input BAM file.
        vcf: Path to the output VCF file.
        visual_report_html: Path to the output visual report HTML file.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/deepvariant",
        inputs={"fasta": fasta, "bam": bam},
        outputs={"vcf": vcf, "visual_report_html": visual_report_html},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def deepvariant(
    *,
    fasta: str,
    bam: str,
    vcf: str,
    visual_report_html: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call genetic variants using deep neural network.

    Args:
        fasta: Path to the input FASTA file.
        bam: Path to the input BAM file.
        vcf: Path to the output VCF file.
        visual_report_html: Path to the output visual report HTML file.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_deepvariant(
        fasta=fasta,
        bam=bam,
        vcf=vcf,
        visual_report_html=visual_report_html,
        extra=extra,
         
    )
