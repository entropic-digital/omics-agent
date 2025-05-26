from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_gwascat(
    *,
    calls: str,
    gwas_catalog: str,
    annotated_calls: str,
     
) -> subprocess.CompletedProcess:
    """
    Annotate genetic variant calls using the GWAS Catalog with SnpSift.

    Args:
        calls: Path to the input genetic variant calls file (vcf, bcf, vcf.gz).
        gwas_catalog: Path to the GWAS Catalog TSV-formatted file.
        annotated_calls: Path to the output file for the annotated calls (vcf, bcf, vcf.gz).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/snpsift/gwascat",
        inputs={"calls": calls, "gwas_catalog": gwas_catalog},
        outputs={"annotated_calls": annotated_calls},
         
    )


@collect_tool()
def gwascat(
    *,
    calls: str,
    gwas_catalog: str,
    annotated_calls: str,
     
) -> subprocess.CompletedProcess:
    """
    SnpSift GWAS Catalog annotation tool.

    Args:
        calls: Path to the input genetic variant calls file (vcf, bcf, vcf.gz).
        gwas_catalog: Path to the GWAS Catalog TSV-formatted file.
        annotated_calls: Path to the output file for the annotated calls (vcf, bcf, vcf.gz).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_gwascat(
        calls=calls,
        gwas_catalog=gwas_catalog,
        annotated_calls=annotated_calls,
         
    )
