from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_variantrecalibrator(
    *,
    vcf_file: str,
    recal_file: str,
    tranches_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GATK VariantRecalibrator.

    Args:
        vcf_file: Path to the input VCF file.
        recal_file: Name of the output .recal file.
        tranches_file: Name of the output .tranches file.
        java_opts (optional): Additional Java options (excluding -XmX or -Djava.io.tmpdir).
        extra (optional): Additional arguments for VariantRecalibrator.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/variantrecalibrator",
        inputs=dict(vcf=vcf_file),
        outputs=dict(recal=recal_file, tranches=tranches_file),
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def variantrecalibrator(
    *,
    vcf_file: str,
    recal_file: str,
    tranches_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GATK VariantRecalibrator.

    Args:
        vcf_file: Path to the input VCF file.
        recal_file: Name of the output .recal file.
        tranches_file: Name of the output .tranches file.
        java_opts (optional): Additional Java options (excluding -XmX or -Djava.io.tmpdir).
        extra (optional): Additional arguments for VariantRecalibrator.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_variantrecalibrator(
        vcf_file=vcf_file,
        recal_file=recal_file,
        tranches_file=tranches_file,
        java_opts=java_opts,
        extra=extra,
         
    )
