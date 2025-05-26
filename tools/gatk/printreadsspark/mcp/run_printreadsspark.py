from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_printreadsspark(
    *,
    bam_file: str,
    reference_file: str,
    reference_dict: str,
    filtered_bam_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
    spark_runner: Optional[str] = None,
    spark_master: Optional[str] = None,
    spark_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Write reads from a SAM format file (SAM/BAM/CRAM) that pass specified criteria to a new file using GATK PrintReadsSpark.

    Args:
        bam_file: Input BAM file to be filtered.
        reference_file: Reference genome file to be used.
        reference_dict: Reference dictionary file.
        filtered_bam_file: Output filtered BAM file.
        java_opts (optional): Java options to pass to the compiler, e.g. "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments for PrintReadsSpark.
        spark_runner (optional): Spark runner, e.g., "LOCAL", "SPARK", or "GCS".
        spark_master (optional): URL for Spark Master. Set to "local[number_of_cores]" for local execution.
        spark_extra (optional): Additional Spark arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/printreadsspark",
        inputs={
            "bam_file": bam_file,
            "reference_file": reference_file,
            "reference_dict": reference_dict,
        },
        outputs={"filtered_bam_file": filtered_bam_file},
        params={
            "java_opts": java_opts,
            "extra": extra,
            "spark_runner": spark_runner,
            "spark_master": spark_master,
            "spark_extra": spark_extra,
        },
         
    )


@collect_tool()
def printreadsspark(
    *,
    bam_file: str,
    reference_file: str,
    reference_dict: str,
    filtered_bam_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
    spark_runner: Optional[str] = None,
    spark_master: Optional[str] = None,
    spark_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Write reads from a SAM format file (SAM/BAM/CRAM) that pass specified criteria to a new file using GATK PrintReadsSpark.

    Args:
        bam_file: Input BAM file to be filtered.
        reference_file: Reference genome file to be used.
        reference_dict: Reference dictionary file.
        filtered_bam_file: Output filtered BAM file.
        java_opts (optional): Java options to pass to the compiler, e.g. "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments for PrintReadsSpark.
        spark_runner (optional): Spark runner, e.g., "LOCAL", "SPARK", or "GCS".
        spark_master (optional): URL for Spark Master. Set to "local[number_of_cores]" for local execution.
        spark_extra (optional): Additional Spark arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_printreadsspark(
        bam_file=bam_file,
        reference_file=reference_file,
        reference_dict=reference_dict,
        filtered_bam_file=filtered_bam_file,
        java_opts=java_opts,
        extra=extra,
        spark_runner=spark_runner,
        spark_master=spark_master,
        spark_extra=spark_extra,
         
    )
