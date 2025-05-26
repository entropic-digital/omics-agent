from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_baserecalibrator(
    *,
    bam_file: str,
    fasta_reference: str,
    known_variants: str,
    recalibration_table: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GATK BaseRecalibrator.

    Args:
        bam_file: Input BAM file path.
        fasta_reference: Path to the reference FASTA file.
        known_variants: Path to the VCF.gz file of known variants.
        recalibration_table: Output path for the recalibration table.
        java_opts (optional): Additional arguments for the Java compiler.
        extra (optional): Additional arguments for the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/baserecalibrator",
        inputs=dict(
            bam_file=bam_file,
            fasta_reference=fasta_reference,
            known_variants=known_variants,
        ),
        outputs=dict(recalibration_table=recalibration_table),
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def baserecalibrator(
    *,
    bam_file: str,
    fasta_reference: str,
    known_variants: str,
    recalibration_table: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GATK BaseRecalibrator.

    Args:
        bam_file: Input BAM file path.
        fasta_reference: Path to the reference FASTA file.
        known_variants: Path to the VCF.gz file of known variants.
        recalibration_table: Output path for the recalibration table.
        java_opts (optional): Additional arguments for the Java compiler.
        extra (optional): Additional arguments for the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_baserecalibrator(
        bam_file=bam_file,
        fasta_reference=fasta_reference,
        known_variants=known_variants,
        recalibration_table=recalibration_table,
        java_opts=java_opts,
        extra=extra,
         
    )
