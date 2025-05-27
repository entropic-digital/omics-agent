from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_markduplicatesspark(
    *,
    bam_file: str,
    reference_file: str,
    output_bam: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
    spark_runner: Optional[str] = "LOCAL",
    spark_master: Optional[str] = None,
    spark_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GATK MarkDuplicatesSpark: Identifies duplicate reads in BAM files using Spark for parallel processing.

    Args:
        bam_file: Input BAM file path.
        reference_file: Reference file path.
        output_bam: Output BAM file path with marked or removed duplicates.
        java_opts (optional): Additional Java options (e.g., "-XX:ParallelGCThreads=10").
        extra (optional): Additional program arguments.
        spark_runner (optional): Spark runner mode ("LOCAL", "SPARK", or "GCS"). Default is "LOCAL".
        spark_master (optional): URL of the Spark Master. E.g., "local[number_of_cores]" for local use.
        spark_extra (optional): Additional Spark arguments.
  
    Returns:
        CompletedProcess: Information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/markduplicatesspark",
        inputs={"bam_file": bam_file, "reference_file": reference_file},
        outputs={"output_bam": output_bam},
        params={
            "java_opts": java_opts,
            "extra": extra,
            "spark_runner": spark_runner,
            "spark_master": spark_master,
            "spark_extra": spark_extra,
        },
         
    )


@collect_tool()
def markduplicatesspark(
    *,
    bam_file: str,
    reference_file: str,
    output_bam: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
    spark_runner: Optional[str] = "LOCAL",
    spark_master: Optional[str] = None,
    spark_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GATK MarkDuplicatesSpark: Identifies duplicate reads in BAM files using Spark for parallel processing.

    Args:
        bam_file: Input BAM file path.
        reference_file: Reference file path.
        output_bam: Output BAM file path with marked or removed duplicates.
        java_opts (optional): Additional Java options (e.g., "-XX:ParallelGCThreads=10").
        extra (optional): Additional program arguments.
        spark_runner (optional): Spark runner mode ("LOCAL", "SPARK", or "GCS"). Default is "LOCAL".
        spark_master (optional): URL of the Spark Master. E.g., "local[number_of_cores]" for local use.
        spark_extra (optional): Additional Spark arguments.
  
    Returns:
        CompletedProcess: Information about the completed Snakemake process.
    """
    return run_markduplicatesspark(
        bam_file=bam_file,
        reference_file=reference_file,
        output_bam=output_bam,
        java_opts=java_opts,
        extra=extra,
        spark_runner=spark_runner,
        spark_master=spark_master,
        spark_extra=spark_extra,
         
    )
