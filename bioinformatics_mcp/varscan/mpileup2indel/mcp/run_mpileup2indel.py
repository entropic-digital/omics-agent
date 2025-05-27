from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_mpileup2indel(
    *,
    mpileup_file: str,
    vcf_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Detect indels in NGS data from mpileup files using VarScan.

    Args:
        mpileup_file: Path to the input mpileup file.
        vcf_file: Path to the output VCF file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/varscan/mpileup2indel",
        inputs=dict(mpileup_file=mpileup_file),
        outputs=dict(vcf_file=vcf_file),
         
    )


@collect_tool()
def mpileup2indel(
    *,
    mpileup_file: str,
    vcf_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Detect indels in NGS data from mpileup files using VarScan.

    Args:
        mpileup_file: Path to the input mpileup file.
        vcf_file: Path to the output VCF file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mpileup2indel(
        mpileup_file=mpileup_file,
        vcf_file=vcf_file,
         
    )
