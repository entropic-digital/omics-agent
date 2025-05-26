from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_filter(
    *,
    input_vcf: str,
    output_vcf: str,
    filter_expression: Optional[str] = None,
    chr_filter: Optional[str] = None,
    quality_threshold: Optional[int] = None,
    depth_threshold: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Filter VCF files using vcftools.

    Args:
        input_vcf: Path to the input VCF file.
        output_vcf: Path to the output VCF file.
        filter_expression (optional): Apply a custom filter expression.
        chr_filter (optional): Filter by a specific chromosome.
        quality_threshold (optional): Minimum quality score threshold.
        depth_threshold (optional): Minimum depth threshold.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {}
    if filter_expression:
        params["filter_expression"] = filter_expression
    if chr_filter:
        params["chr_filter"] = chr_filter
    if quality_threshold:
        params["quality_threshold"] = quality_threshold
    if depth_threshold:
        params["depth_threshold"] = depth_threshold

    return run_snake_wrapper(
        wrapper="file:tools/vcftools/filter",
        inputs=dict(input_vcf=input_vcf, output_vcf=output_vcf),
        params=params,
         
    )


@collect_tool()
def filter_vcf(
    *,
    input_vcf: str,
    output_vcf: str,
    filter_expression: Optional[str] = None,
    chr_filter: Optional[str] = None,
    quality_threshold: Optional[int] = None,
    depth_threshold: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Filter VCF files using vcftools.

    Args:
        input_vcf: Path to the input VCF file.
        output_vcf: Path to the output VCF file.
        filter_expression (optional): Apply a custom filter expression.
        chr_filter (optional): Filter by a specific chromosome.
        quality_threshold (optional): Minimum quality score threshold.
        depth_threshold (optional): Minimum depth threshold.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_filter(
        input_vcf=input_vcf,
        output_vcf=output_vcf,
        filter_expression=filter_expression,
        chr_filter=chr_filter,
        quality_threshold=quality_threshold,
        depth_threshold=depth_threshold,
         
    )
