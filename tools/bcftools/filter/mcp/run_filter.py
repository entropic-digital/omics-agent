from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_filter(
    *,
    input_vcf_bcf: str,
    output_filtered_vcf_bcf: str,
    uncompressed_bcf: Optional[bool] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Filter VCF/BCF file using bcftools filter.

    Args:
        input_vcf_bcf: Path to the input VCF/BCF file to be filtered.
        output_filtered_vcf_bcf: Path to the output filtered VCF/BCF file.
        uncompressed_bcf (optional): If True, specifies uncompressed BCF output.
        extra (optional): Additional arguments for bcftools filter (excluding `--threads`, `-o/--output`, `-O/--output-type`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {}
    if uncompressed_bcf is not None:
        params["uncompressed_bcf"] = uncompressed_bcf
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:tools/bcftools/filter",
        inputs={"input_vcf_bcf": input_vcf_bcf},
        outputs={"output_filtered_vcf_bcf": output_filtered_vcf_bcf},
        params=params,
         
    )


@collect_tool()
def filter_vcf_bcf(
    *,
    input_vcf_bcf: str,
    output_filtered_vcf_bcf: str,
    uncompressed_bcf: Optional[bool] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Filter VCF/BCF file using bcftools filter.

    Args:
        input_vcf_bcf: Path to the input VCF/BCF file to be filtered.
        output_filtered_vcf_bcf: Path to the output filtered VCF/BCF file.
        uncompressed_bcf (optional): If True, specifies uncompressed BCF output.
        extra (optional): Additional arguments for bcftools filter (excluding `--threads`, `-o/--output`, `-O/--output-type`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_filter(
        input_vcf_bcf=input_vcf_bcf,
        output_filtered_vcf_bcf=output_filtered_vcf_bcf,
        uncompressed_bcf=uncompressed_bcf,
        extra=extra,
         
    )
