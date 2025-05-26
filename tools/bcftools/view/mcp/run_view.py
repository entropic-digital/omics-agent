from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_view(
    *,
    vcf_bcf_file: str,
    output_file: str,
    uncompressed_bcf: Optional[bool] = False,
    extra: Optional[str] = "",
     
) -> subprocess.CompletedProcess:
    """
    View VCF/BCF file in a different format.

    Args:
        vcf_bcf_file: Input VCF/BCF file to be processed.
        output_file: Filtered VCF/BCF file to be generated.
        uncompressed_bcf (optional): Whether the output BCF should be uncompressed. Default is False.
        extra (optional): Additional program arguments, excluding '--threads', '-o/--output', or '-O/--output-type'. Default is an empty string.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {}
    if uncompressed_bcf:
        params["uncompressed_bcf"] = uncompressed_bcf
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:tools/bcftools/view",
        inputs=dict(vcf_bcf_file=vcf_bcf_file),
        outputs=dict(output_file=output_file),
        params=params,
         
    )


@collect_tool()
def view(
    *,
    vcf_bcf_file: str,
    output_file: str,
    uncompressed_bcf: Optional[bool] = False,
    extra: Optional[str] = "",
     
) -> subprocess.CompletedProcess:
    """
    View VCF/BCF file in a different format.

    Args:
        vcf_bcf_file: Input VCF/BCF file to be processed.
        output_file: Filtered VCF/BCF file to be generated.
        uncompressed_bcf (optional): Whether the output BCF should be uncompressed. Default is False.
        extra (optional): Additional program arguments, excluding '--threads', '-o/--output', or '-O/--output-type'. Default is an empty string.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_view(
        vcf_bcf_file=vcf_bcf_file,
        output_file=output_file,
        uncompressed_bcf=uncompressed_bcf,
        extra=extra,
         
    )
