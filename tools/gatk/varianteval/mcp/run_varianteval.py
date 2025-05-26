from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_varianteval(
    *,
    vcf_files: str,
    bam_cram_files: Optional[str] = None,
    reference_genome: Optional[str] = None,
    reference_dictionary: Optional[str] = None,
    known_variants_vcf: Optional[str] = None,
    pedigree_file: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk VariantEval.

    Args:
        vcf_files: Input VCF files to evaluate.
        bam_cram_files (optional): BAM or CRAM files for additional context.
        reference_genome (optional): Reference genome file.
        reference_dictionary (optional): Reference dictionary file.
        known_variants_vcf (optional): VCF.gz file of known variants.
        pedigree_file (optional): PED (pedigree) file.
        java_opts (optional): Additional arguments for the Java compiler (excluding `-XmX` or `-Djava.io.tmpdir`).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "vcf_files": vcf_files,
        "bam_cram_files": bam_cram_files,
        "reference_genome": reference_genome,
        "reference_dictionary": reference_dictionary,
        "known_variants_vcf": known_variants_vcf,
        "pedigree_file": pedigree_file,
    }
    params = {
        "java_opts": java_opts,
        "extra": extra,
    }

    return run_snake_wrapper(
        wrapper="file:tools/gatk/varianteval",
        inputs={key: value for key, value in inputs.items() if value is not None},
        params={key: value for key, value in params.items() if value is not None},
         
    )


@collect_tool()
def varianteval(
    *,
    vcf_files: str,
    bam_cram_files: Optional[str] = None,
    reference_genome: Optional[str] = None,
    reference_dictionary: Optional[str] = None,
    known_variants_vcf: Optional[str] = None,
    pedigree_file: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk VariantEval.

    Args:
        vcf_files: Input VCF files to evaluate.
        bam_cram_files (optional): BAM or CRAM files for additional context.
        reference_genome (optional): Reference genome file.
        reference_dictionary (optional): Reference dictionary file.
        known_variants_vcf (optional): VCF.gz file of known variants.
        pedigree_file (optional): PED (pedigree) file.
        java_opts (optional): Additional arguments for the Java compiler (excluding `-XmX` or `-Djava.io.tmpdir`).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_varianteval(
        vcf_files=vcf_files,
        bam_cram_files=bam_cram_files,
        reference_genome=reference_genome,
        reference_dictionary=reference_dictionary,
        known_variants_vcf=known_variants_vcf,
        pedigree_file=pedigree_file,
        java_opts=java_opts,
        extra=extra,
         
    )
