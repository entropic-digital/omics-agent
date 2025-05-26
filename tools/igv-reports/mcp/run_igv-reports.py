from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_igv_reports(
    *,
    bam: str,
    vcf: str,
    html: str,
     
) -> subprocess.CompletedProcess:
    """
    Create self-contained igv.js HTML pages.

    Args:
        bam: Input BAM file.
        vcf: Input VCF file.
        html: Output HTML file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/igv-reports",
        inputs={"bam": bam, "vcf": vcf},
        outputs={"html": html},
         
    )


@collect_tool()
def igv_reports(
    *,
    bam: str,
    vcf: str,
    html: str,
     
) -> subprocess.CompletedProcess:
    """
    Create self-contained igv.js HTML pages.

    Args:
        bam: Input BAM file.
        vcf: Input VCF file.
        html: Output HTML file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_igv_reports(bam=bam, vcf=vcf, html=html,      )
