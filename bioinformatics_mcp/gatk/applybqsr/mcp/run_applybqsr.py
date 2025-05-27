from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_applybqsr(
    *,
    bam_file: str,
    fasta_reference: str,
    recalibration_table: str,
    recalibrated_bam_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk ApplyBQSR.

    Args:
        bam_file: Input BAM file.
        fasta_reference: Input FASTA reference file.
        recalibration_table: Recalibration table for the BAM.
        recalibrated_bam_file: Output recalibrated BAM file.
        java_opts (optional): Additional arguments for the Java compiler (excluding `-XmX` or `-Djava.io.tmpdir`).
        extra (optional): Additional arguments for the ApplyBQSR program.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/applybqsr",
        inputs=dict(
            bam_file=bam_file,
            fasta_reference=fasta_reference,
            recalibration_table=recalibration_table,
        ),
        outputs=dict(
            recalibrated_bam_file=recalibrated_bam_file,
        ),
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def applybqsr(
    *,
    bam_file: str,
    fasta_reference: str,
    recalibration_table: str,
    recalibrated_bam_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk ApplyBQSR.

    Args:
        bam_file: Input BAM file.
        fasta_reference: Input FASTA reference file.
        recalibration_table: Recalibration table for the BAM.
        recalibrated_bam_file: Output recalibrated BAM file.
        java_opts (optional): Additional arguments for the Java compiler (excluding `-XmX` or `-Djava.io.tmpdir`).
        extra (optional): Additional arguments for the ApplyBQSR program.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_applybqsr(
        bam_file=bam_file,
        fasta_reference=fasta_reference,
        recalibration_table=recalibration_table,
        recalibrated_bam_file=recalibrated_bam_file,
        java_opts=java_opts,
        extra=extra,
         
    )
