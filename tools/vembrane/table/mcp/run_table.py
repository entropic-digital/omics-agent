from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_table(
    *,
    input_vcf: str,
    output_table: str,
     
) -> subprocess.CompletedProcess:
    """
    Vembrane table allows generating table-like textfiles from VCFs based on any INFO field, CHROM, POS, REF, ALT, QUAL, and the annotation field ANN.

    Args:
        input_vcf: Path to the input VCF-formatted file.
        output_table: Path to the output table-like textfile to be generated.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/vembrane/table",
        inputs={"input_vcf": input_vcf},
        outputs={"output_table": output_table},
         
    )


@collect_tool()
def table(
    *,
    input_vcf: str,
    output_table: str,
     
) -> subprocess.CompletedProcess:
    """
    Vembrane table allows generating table-like textfiles from VCFs based on any INFO field, CHROM, POS, REF, ALT, QUAL, and the annotation field ANN.

    Args:
        input_vcf: Path to the input VCF-formatted file.
        output_table: Path to the output table-like textfile to be generated.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_table(
        input_vcf=input_vcf,
        output_table=output_table,
         
    )
