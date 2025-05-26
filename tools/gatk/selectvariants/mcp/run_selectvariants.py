from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_selectvariants(
    *,
    vcf: str,
    reference_genome: str,
    filtered_vcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk SelectVariants.

    Args:
        vcf: Path to the input VCF file.
        reference_genome: Path to the reference genome.
        filtered_vcf: Path to the output filtered VCF file.
        java_opts (optional): Additional arguments to be passed to the Java compiler.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/selectvariants",
        inputs=dict(vcf=vcf, reference_genome=reference_genome),
        outputs=dict(filtered_vcf=filtered_vcf),
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def selectvariants(
    *,
    vcf: str,
    reference_genome: str,
    filtered_vcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk SelectVariants.

    Args:
        vcf: Path to the input VCF file.
        reference_genome: Path to the reference genome.
        filtered_vcf: Path to the output filtered VCF file.
        java_opts (optional): Additional arguments to be passed to the Java compiler.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_selectvariants(
        vcf=vcf,
        reference_genome=reference_genome,
        filtered_vcf=filtered_vcf,
        java_opts=java_opts,
        extra=extra,
         
    )
