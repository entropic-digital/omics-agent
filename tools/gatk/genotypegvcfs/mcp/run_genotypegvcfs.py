from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_genotypegvcfs(
    *,
    input_gvcf_or_db: str,
    reference_genome: str,
    output_vcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk GenotypeGVCFs.

    Args:
        input_gvcf_or_db: Path to the GVCF files or GenomicsDB workspace.
        reference_genome: Path to the reference genome file.
        output_vcf: Path to the output VCF file with genotypes.
        java_opts (optional): Extra arguments passed to the Java compiler (excluding -XmX and -Djava.io.tmpdir).
        extra (optional): Additional program arguments for `gatk GenotypeGVCFs`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/genotypegvcfs",
        inputs=dict(gvcf_or_db=input_gvcf_or_db, reference=reference_genome),
        outputs=dict(vcf=output_vcf),
        params={
            key: value
            for key, value in (("java_opts", java_opts), ("extra", extra))
            if value is not None
        },
         
    )


@collect_tool()
def genotypegvcfs(
    *,
    input_gvcf_or_db: str,
    reference_genome: str,
    output_vcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk GenotypeGVCFs.

    Args:
        input_gvcf_or_db: Path to the GVCF files or GenomicsDB workspace.
        reference_genome: Path to the reference genome file.
        output_vcf: Path to the output VCF file with genotypes.
        java_opts (optional): Extra arguments passed to the Java compiler (excluding -XmX and -Djava.io.tmpdir).
        extra (optional): Additional program arguments for `gatk GenotypeGVCFs`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_genotypegvcfs(
        input_gvcf_or_db=input_gvcf_or_db,
        reference_genome=reference_genome,
        output_vcf=output_vcf,
        java_opts=java_opts,
        extra=extra,
         
    )
