from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_variantfiltration(
    *,
    vcf: str,
    reference_genome: str,
    filtered_vcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk VariantFiltration.

    Args:
        vcf: Path to the input VCF file.
        reference_genome: Path to the reference genome file.
        filtered_vcf: Path to the output filtered VCF file.
        java_opts (optional): Additional arguments for the Java compiler (excluding -XmX and -Djava.io.tmpdir).
        extra (optional): Additional program-specific arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/variantfiltration",
        inputs=dict(vcf=vcf, reference_genome=reference_genome),
        outputs=dict(filtered_vcf=filtered_vcf),
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def variantfiltration(
    *,
    vcf: str,
    reference_genome: str,
    filtered_vcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk VariantFiltration.

    Args:
        vcf: Path to the input VCF file.
        reference_genome: Path to the reference genome file.
        filtered_vcf: Path to the output filtered VCF file.
        java_opts (optional): Additional arguments for the Java compiler (excluding -XmX and -Djava.io.tmpdir).
        extra (optional): Additional program-specific arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_variantfiltration(
        vcf=vcf,
        reference_genome=reference_genome,
        filtered_vcf=filtered_vcf,
        java_opts=java_opts,
        extra=extra,
         
    )
