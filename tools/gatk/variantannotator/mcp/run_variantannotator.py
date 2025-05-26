from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_variantannotator(
    *,
    vcf_file: str,
    bam_file: str,
    reference_genome: str,
    known_variation_vcf: str,
    annotated_vcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk VariantAnnotator.

    Args:
        vcf_file: Path to the input VCF file.
        bam_file: Path to the input BAM file.
        reference_genome: Path to the reference genome.
        known_variation_vcf: Path to the VCF of known variation.
        annotated_vcf: Path to the output annotated VCF file.
        java_opts (optional): Additional Java compiler options, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional GATK VariantAnnotator arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/variantannotator",
        inputs={
            "vcf_file": vcf_file,
            "bam_file": bam_file,
            "reference_genome": reference_genome,
            "known_variation_vcf": known_variation_vcf,
        },
        outputs={
            "annotated_vcf": annotated_vcf,
        },
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def variantannotator(
    *,
    vcf_file: str,
    bam_file: str,
    reference_genome: str,
    known_variation_vcf: str,
    annotated_vcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk VariantAnnotator.

    Args:
        vcf_file: Path to the input VCF file.
        bam_file: Path to the input BAM file.
        reference_genome: Path to the reference genome.
        known_variation_vcf: Path to the VCF of known variation.
        annotated_vcf: Path to the output annotated VCF file.
        java_opts (optional): Additional Java compiler options, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional GATK VariantAnnotator arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_variantannotator(
        vcf_file=vcf_file,
        bam_file=bam_file,
        reference_genome=reference_genome,
        known_variation_vcf=known_variation_vcf,
        annotated_vcf=annotated_vcf,
        java_opts=java_opts,
        extra=extra,
         
    )
