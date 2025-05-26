from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_printreads(
    *,
    bam_file: str,
    recalibration_table: str,
    reference_genome: str,
    output_bam: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GATK3 PrintReads.

    Args:
        bam_file: Path to the input BAM file.
        recalibration_table: Path to the recalibration table.
        reference_genome: Path to the reference genome file.
        output_bam: Path to the output BAM file.
        java_opts (optional): Additional arguments to be passed to the Java compiler (e.g., "-Xmx4G").
        extra (optional): Additional program arguments for GATK3 PrintReads.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk3/printreads",
        inputs={
            "bam_file": bam_file,
            "recalibration_table": recalibration_table,
            "reference_genome": reference_genome,
        },
        outputs={
            "output_bam": output_bam,
        },
        params={
            "java_opts": java_opts if java_opts else "",
            "extra": extra if extra else "",
        },
         
    )


@collect_tool()
def printreads(
    *,
    bam_file: str,
    recalibration_table: str,
    reference_genome: str,
    output_bam: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GATK3 PrintReads.

    Args:
        bam_file: Path to the input BAM file.
        recalibration_table: Path to the recalibration table.
        reference_genome: Path to the reference genome file.
        output_bam: Path to the output BAM file.
        java_opts (optional): Additional arguments to be passed to the Java compiler (e.g., "-Xmx4G").
        extra (optional): Additional program arguments for GATK3 PrintReads.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_printreads(
        bam_file=bam_file,
        recalibration_table=recalibration_table,
        reference_genome=reference_genome,
        output_bam=output_bam,
        java_opts=java_opts,
        extra=extra,
         
    )
