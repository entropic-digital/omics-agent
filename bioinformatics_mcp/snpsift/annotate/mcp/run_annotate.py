from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_annotate(
    *,
    vcf_input: str,
    annotation_vcf: str,
    output_vcf: str,
     
) -> subprocess.CompletedProcess:
    """
    Annotate a VCF file using fields from another VCF file with SnpSift.

    Args:
        vcf_input: VCF-formatted file to be annotated.
        annotation_vcf: VCF-formatted file to be used as the annotation source.
        output_vcf: VCF-formatted file to store the annotated results.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/snpsift/annotate",
        inputs=dict(vcf_input=vcf_input, annotation_vcf=annotation_vcf),
        outputs=dict(output_vcf=output_vcf),
        params={},
         
    )


@collect_tool()
def annotate(
    *,
    vcf_input: str,
    annotation_vcf: str,
    output_vcf: str,
     
) -> subprocess.CompletedProcess:
    """
    Annotate a VCF file using fields from another VCF file with SnpSift.

    Args:
        vcf_input: VCF-formatted file to be annotated.
        annotation_vcf: VCF-formatted file to be used as the annotation source.
        output_vcf: VCF-formatted file to store the annotated results.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_annotate(
        vcf_input=vcf_input,
        annotation_vcf=annotation_vcf,
        output_vcf=output_vcf,
         
    )
