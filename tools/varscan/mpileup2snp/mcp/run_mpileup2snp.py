from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_mpileup2snp(
    *,
    mpileup_file: str,
    vcf_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Detect variants in NGS data from Samtools mpileup with VarScan.

    Args:
        mpileup_file: Path to the mpileup input file.
        vcf_file: Path for the output VCF file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/varscan/mpileup2snp",
        inputs=dict(mpileup=mpileup_file),
        outputs=dict(vcf=vcf_file),
         
    )


@collect_tool()
def mpileup2snp(
    *,
    mpileup_file: str,
    vcf_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Detect variants in NGS data from Samtools mpileup with VarScan.

    Args:
        mpileup_file: Path to the mpileup input file.
        vcf_file: Path for the output VCF file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mpileup2snp(
        mpileup_file=mpileup_file,
        vcf_file=vcf_file,
         
    )
