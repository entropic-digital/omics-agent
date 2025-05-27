from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_applyvqsr(
    *,
    vcf_file: str,
    recalibration_file: str,
    tranches_file: str,
    output_vcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk ApplyVQSR.

    Args:
        vcf_file: Input VCF file.
        recalibration_file: Recalibration file.
        tranches_file: Tranches file.
        output_vcf: Path to output Variant-QualityScore-Recalibrated VCF file.
        java_opts (optional): Additional arguments for the Java compiler (e.g., "-XX:ParallelGCThreads=10").
                              Note: Do not include -XmX or -Djava.io.tmpdir, as they are handled automatically.
        extra (optional): Additional program arguments for ApplyVQSR.
  
    Returns:
        subprocess.CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/applyvqsr",
        inputs={
            "vcf_file": vcf_file,
            "recalibration_file": recalibration_file,
            "tranches_file": tranches_file,
        },
        outputs={
            "output_vcf": output_vcf,
        },
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def applyvqsr(
    *,
    vcf_file: str,
    recalibration_file: str,
    tranches_file: str,
    output_vcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk ApplyVQSR.

    Args:
        vcf_file: Input VCF file.
        recalibration_file: Recalibration file.
        tranches_file: Tranches file.
        output_vcf: Path to output Variant-QualityScore-Recalibrated VCF file.
        java_opts (optional): Additional arguments for the Java compiler (e.g., "-XX:ParallelGCThreads=10").
                              Note: Do not include -XmX or -Djava.io.tmpdir, as they are handled automatically.
        extra (optional): Additional program arguments for ApplyVQSR.
  
    Returns:
        subprocess.CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_applyvqsr(
        vcf_file=vcf_file,
        recalibration_file=recalibration_file,
        tranches_file=tranches_file,
        output_vcf=output_vcf,
        java_opts=java_opts,
        extra=extra,
         
    )
