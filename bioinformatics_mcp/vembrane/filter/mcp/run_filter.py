from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_filter(
    *,
    input_vcf: str,
    output_vcf: str,
    filter_expression: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Vembrane filter allows to simultaneously filter variants based on INFO fields, CHROM, POS, REF, ALT,
    QUAL, and the annotation field ANN. When filtering based on ANN, annotation entries are filtered first.
    If no annotation entry remains, the entire variant is deleted.

    Args:
        input_vcf: Path to the input VCF file.
        output_vcf: Path to the output VCF file.
        filter_expression (optional): Filter expression to apply to the variants.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/vembrane/filter",
        inputs=dict(input_vcf=input_vcf),
        outputs=dict(output_vcf=output_vcf),
        params={"filter_expression": filter_expression} if filter_expression else {},
         
    )


@collect_tool()
def vembrane_filter(
    *,
    input_vcf: str,
    output_vcf: str,
    filter_expression: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Vembrane filter allows to simultaneously filter variants based on INFO fields, CHROM, POS, REF, ALT,
    QUAL, and the annotation field ANN. When filtering based on ANN, annotation entries are filtered first.
    If no annotation entry remains, the entire variant is deleted.

    Args:
        input_vcf: Path to the input VCF file.
        output_vcf: Path to the output VCF file.
        filter_expression (optional): Filter expression to apply to the variants.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_filter(
        input_vcf=input_vcf,
        output_vcf=output_vcf,
        filter_expression=filter_expression,
         
    )
