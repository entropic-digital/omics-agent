from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_haplotypecaller(
    *,
    bam_file: str,
    gvcf_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GATK HaplotypeCaller.

    Args:
        bam_file: Path to the input BAM file.
        gvcf_file: Path to the output GVCF file.
        java_opts (optional): Additional arguments for the Java compiler (excluding -XmX and -Djava.io.tmpdir).
        extra (optional): Additional GATK program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/haplotypecaller",
        inputs=dict(bam_file=bam_file),
        outputs=dict(gvcf_file=gvcf_file),
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def haplotypecaller(
    *,
    bam_file: str,
    gvcf_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GATK HaplotypeCaller.

    Args:
        bam_file: Path to the input BAM file.
        gvcf_file: Path to the output GVCF file.
        java_opts (optional): Additional arguments for the Java compiler (excluding -XmX and -Djava.io.tmpdir).
        extra (optional): Additional GATK program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_haplotypecaller(
        bam_file=bam_file,
        gvcf_file=gvcf_file,
        java_opts=java_opts,
        extra=extra,
         
    )
