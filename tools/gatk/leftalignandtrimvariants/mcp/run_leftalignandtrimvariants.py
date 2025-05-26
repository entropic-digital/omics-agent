from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_leftalignandtrimvariants(
    *,
    variant_call_set: str,
    output_vcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk LeftAlignAndTrimVariants.

    Args:
        variant_call_set: Path to the variant call set to left-align and trim.
        output_vcf: Path to the left-aligned output VCF.
        java_opts (optional): Additional arguments for the Java compiler (excluding `-XmX` and `-Djava.io.tmpdir`).
        extra (optional): Additional arguments for the GATK LeftAlignAndTrimVariants tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/leftalignandtrimvariants",
        inputs=dict(variant_call_set=variant_call_set),
        outputs=dict(output_vcf=output_vcf),
        params={"java_opts": java_opts, "extra": extra} if java_opts or extra else {},
         
    )


@collect_tool()
def leftalignandtrimvariants(
    *,
    variant_call_set: str,
    output_vcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk LeftAlignAndTrimVariants.

    Args:
        variant_call_set: Path to the variant call set to left-align and trim.
        output_vcf: Path to the left-aligned output VCF.
        java_opts (optional): Additional arguments for the Java compiler (excluding `-XmX` and `-Djava.io.tmpdir`).
        extra (optional): Additional arguments for the GATK LeftAlignAndTrimVariants tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_leftalignandtrimvariants(
        variant_call_set=variant_call_set,
        output_vcf=output_vcf,
        java_opts=java_opts,
        extra=extra,
         
    )
