from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_run(
    *,
    input_vcf: str,
    output_dir: str,
    assembly: str,
    genome: Optional[str] = None,
    modules: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Runs OpenCRAVAT. Annotates variant calls with OpenCRAVAT.

    Args:
        input_vcf: Path to the input VCF file.
        output_dir: Directory where output files will be stored.
        assembly: Genome assembly version (e.g., hg19, hg38).
        genome (optional): Reference genome file.
        modules (optional): Additional OpenCRAVAT modules to be used.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/open-cravat/run",
        inputs={"input_vcf": input_vcf},
        outputs={"output_dir": output_dir},
        params={
            "assembly": assembly,
            "genome": genome,
            "modules": modules,
        },
         
    )


@collect_tool()
def run(
    *,
    input_vcf: str,
    output_dir: str,
    assembly: str,
    genome: Optional[str] = None,
    modules: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Runs OpenCRAVAT. Annotates variant calls with OpenCRAVAT.

    Args:
        input_vcf: Path to the input VCF file.
        output_dir: Directory where output files will be stored.
        assembly: Genome assembly version (e.g., hg19, hg38).
        genome (optional): Reference genome file.
        modules (optional): Additional OpenCRAVAT modules to be used.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_run(
        input_vcf=input_vcf,
        output_dir=output_dir,
        assembly=assembly,
        genome=genome,
        modules=modules,
         
    )
