from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_variantstotable(
    *,
    vcf_file: str,
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk VariantsToTable.

    Args:
        vcf_file: A VCF file to convert to a table.
        output_file: A tab-delimited file containing the values of the requested fields in the VCF file.
        java_opts (optional): Additional arguments to be passed to the Java compiler, e.g. '-XX:ParallelGCThreads=10'.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/variantstotable",
        inputs={"vcf_file": vcf_file},
        outputs={"output_file": output_file},
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def variantstotable(
    *,
    vcf_file: str,
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk VariantsToTable.

    Args:
        vcf_file: A VCF file to convert to a table.
        output_file: A tab-delimited file containing the values of the requested fields in the VCF file.
        java_opts (optional): Additional arguments to be passed to the Java compiler, e.g. '-XX:ParallelGCThreads=10'.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_variantstotable(
        vcf_file=vcf_file,
        output_file=output_file,
        java_opts=java_opts,
        extra=extra,
         
    )
