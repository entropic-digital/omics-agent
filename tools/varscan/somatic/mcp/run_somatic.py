from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_somatic(
    *,
    normal_pileup: str,
    tumor_pileup: str,
    output_vcf: str,
     
) -> subprocess.CompletedProcess:
    """
    Varscan Somatic calls variants and identifies their somatic status using
    pileup files from a matched tumor-normal pair.

    Args:
        normal_pileup: Path to the normal sample pileup file.
        tumor_pileup: Path to the tumor sample pileup file.
        output_vcf: Path to the output VCF file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/varscan/somatic",
        inputs=dict(normal_pileup=normal_pileup, tumor_pileup=tumor_pileup),
        outputs=dict(output_vcf=output_vcf),
         
    )


@collect_tool()
def somatic(
    *,
    normal_pileup: str,
    tumor_pileup: str,
    output_vcf: str,
     
) -> subprocess.CompletedProcess:
    """
    Varscan Somatic calls variants and identifies their somatic status using
    pileup files from a matched tumor-normal pair.

    Args:
        normal_pileup: Path to the normal sample pileup file.
        tumor_pileup: Path to the tumor sample pileup file.
        output_vcf: Path to the output VCF file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_somatic(
        normal_pileup=normal_pileup,
        tumor_pileup=tumor_pileup,
        output_vcf=output_vcf,
         
    )
