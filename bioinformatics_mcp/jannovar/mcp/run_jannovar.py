from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_jannovar(
    *,
    input_vcf: str,
    db_path: str,
    output_vcf: str,
    output_json: str,
    genome_version: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Annotate predicted effect of nucleotide changes using Jannovar.

    Args:
        input_vcf: Path to the input VCF file to annotate.
        db_path: Path to the Jannovar database for annotation.
        output_vcf: Path to the output annotated VCF file.
        output_json: Path to the output JSON file.
        genome_version (optional): Genome version to use for annotation (default is None).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/jannovar",
        inputs={
            "input_vcf": input_vcf,
            "db_path": db_path,
        },
        outputs={
            "output_vcf": output_vcf,
            "output_json": output_json,
        },
        params={"genome_version": genome_version} if genome_version else {},
         
    )


@collect_tool()
def jannovar(
    *,
    input_vcf: str,
    db_path: str,
    output_vcf: str,
    output_json: str,
    genome_version: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Annotate predicted effect of nucleotide changes using Jannovar.

    Args:
        input_vcf: Path to the input VCF file to annotate.
        db_path: Path to the Jannovar database for annotation.
        output_vcf: Path to the output annotated VCF file.
        output_json: Path to the output JSON file.
        genome_version (optional): Genome version to use for annotation (default is None).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_jannovar(
        input_vcf=input_vcf,
        db_path=db_path,
        output_vcf=output_vcf,
        output_json=output_json,
        genome_version=genome_version,
         
    )
