from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_call(
    *,
    input_vcf: str,
    output_vcf: str,
    reference: Optional[str] = None,
    uncompressed_bcf: bool = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call variants with `bcftools call`.

    Args:
        input_vcf: Path to the input VCF file.
        output_vcf: Path to the output VCF/BCF file.
        reference (optional): Path to the reference genome file.
        uncompressed_bcf (optional): Flag specifying that BCF output should be uncompressed. Defaults to False.
        extra (optional): Additional program arguments not including `--threads`, `-o/--output`, or `-O/--output-type`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "reference": reference,
        "uncompressed_bcf": uncompressed_bcf,
        "extra": extra,
    }
    params = {k: v for k, v in params.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:tools/bcftools/call",
        inputs=dict(input_vcf=input_vcf),
        outputs=dict(output_vcf=output_vcf),
        params=params,
         
    )


@collect_tool()
def bcftools_call(
    *,
    input_vcf: str,
    output_vcf: str,
    reference: Optional[str] = None,
    uncompressed_bcf: bool = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call variants with `bcftools call`.

    Args:
        input_vcf: Path to the input VCF file.
        output_vcf: Path to the output VCF/BCF file.
        reference (optional): Path to the reference genome file.
        uncompressed_bcf (optional): Flag specifying that BCF output should be uncompressed. Defaults to False.
        extra (optional): Additional program arguments not including `--threads`, `-o/--output`, or `-O/--output-type`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_call(
        input_vcf=input_vcf,
        output_vcf=output_vcf,
        reference=reference,
        uncompressed_bcf=uncompressed_bcf,
        extra=extra,
         
    )
