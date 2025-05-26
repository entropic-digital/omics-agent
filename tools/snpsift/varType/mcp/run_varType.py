from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_varType(
    *,
    input_vcf: str,
    output_vcf: str,
     
) -> subprocess.CompletedProcess:
    """
    Add an INFO field denoting variant type with SnpSift.

    Args:
        input_vcf: Path to the input VCF-formatted file.
        output_vcf: Path to the output VCF-formatted file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/snpsift/varType",
        inputs=dict(input_vcf=input_vcf),
        outputs=dict(output_vcf=output_vcf),
        params={},
         
    )


@collect_tool()
def varType(
    *,
    input_vcf: str,
    output_vcf: str,
     
) -> subprocess.CompletedProcess:
    """
    Add an INFO field denoting variant type with SnpSift.

    Args:
        input_vcf: Path to the input VCF-formatted file.
        output_vcf: Path to the output VCF-formatted file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_varType(input_vcf=input_vcf, output_vcf=output_vcf,      )
