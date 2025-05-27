from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_baserecalibrator(
    *,
    bam_file: str,
    vcf_files: str,
    reference_genome: str,
    recalibration_table: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk3 BaseRecalibrator.

    Args:
        bam_file: Path to the input BAM file.
        vcf_files: Paths to the input VCF files.
        reference_genome: Path to the reference genome.
        recalibration_table: Path to the output recalibration table.
        java_opts (optional): Additional arguments to pass to the Java compiler (e.g., "-Xmx4G").
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk3/baserecalibrator",
        inputs={
            "bam_file": bam_file,
            "vcf_files": vcf_files,
            "reference_genome": reference_genome,
        },
        outputs={
            "recalibration_table": recalibration_table,
        },
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def baserecalibrator(
    *,
    bam_file: str,
    vcf_files: str,
    reference_genome: str,
    recalibration_table: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk3 BaseRecalibrator.

    Args:
        bam_file: Path to the input BAM file.
        vcf_files: Paths to the input VCF files.
        reference_genome: Path to the reference genome.
        recalibration_table: Path to the output recalibration table.
        java_opts (optional): Additional arguments to pass to the Java compiler (e.g., "-Xmx4G").
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_baserecalibrator(
        bam_file=bam_file,
        vcf_files=vcf_files,
        reference_genome=reference_genome,
        recalibration_table=recalibration_table,
        java_opts=java_opts,
        extra=extra,
         
    )
