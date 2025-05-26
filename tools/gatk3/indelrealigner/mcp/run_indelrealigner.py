from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_indelrealigner(
    *,
    bam_file: str,
    reference_genome: str,
    target_intervals: str,
    indel_realigned_bam: str,
    indel_realigned_bai: Optional[str] = None,
    temp_dir: Optional[str] = None,
    bed_file: Optional[str] = None,
    known_variation_vcf: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GATK3 IndelRealigner.

    Args:
        bam_file: Input BAM file.
        reference_genome: Reference genome file.
        target_intervals: Target intervals to realign.
        indel_realigned_bam: Output indel realigned BAM file.
        indel_realigned_bai (optional): Output indel realigned BAI file.
        temp_dir (optional): Temporary directory.
        bed_file (optional): BED file.
        known_variation_vcf (optional): Known variation VCF files.
        java_opts (optional): Additional arguments to be passed to the Java compiler (memory is inferred).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "bam_file": bam_file,
        "reference_genome": reference_genome,
        "target_intervals": target_intervals,
    }
    outputs = {"indel_realigned_bam": indel_realigned_bam}
    params = {}

    if indel_realigned_bai:
        outputs["indel_realigned_bai"] = indel_realigned_bai
    if temp_dir:
        outputs["temp_dir"] = temp_dir
    if bed_file:
        inputs["bed_file"] = bed_file
    if known_variation_vcf:
        inputs["known_variation_vcf"] = known_variation_vcf
    if java_opts:
        params["java_opts"] = java_opts
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:tools/gatk3/indelrealigner",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def indelrealigner(
    *,
    bam_file: str,
    reference_genome: str,
    target_intervals: str,
    indel_realigned_bam: str,
    indel_realigned_bai: Optional[str] = None,
    temp_dir: Optional[str] = None,
    bed_file: Optional[str] = None,
    known_variation_vcf: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GATK3 IndelRealigner.

    Args:
        bam_file: Input BAM file.
        reference_genome: Reference genome file.
        target_intervals: Target intervals to realign.
        indel_realigned_bam: Output indel realigned BAM file.
        indel_realigned_bai (optional): Output indel realigned BAI file.
        temp_dir (optional): Temporary directory.
        bed_file (optional): BED file.
        known_variation_vcf (optional): Known variation VCF files.
        java_opts (optional): Additional arguments to be passed to the Java compiler (memory is inferred).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_indelrealigner(
        bam_file=bam_file,
        reference_genome=reference_genome,
        target_intervals=target_intervals,
        indel_realigned_bam=indel_realigned_bam,
        indel_realigned_bai=indel_realigned_bai,
        temp_dir=temp_dir,
        bed_file=bed_file,
        known_variation_vcf=known_variation_vcf,
        java_opts=java_opts,
        extra=extra,
         
    )
