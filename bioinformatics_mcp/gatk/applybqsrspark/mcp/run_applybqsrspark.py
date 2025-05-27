from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_applybqsrspark(
    *,
    bam: str,
    fasta: str,
    recal_table: str,
    output_bam: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
    spark_runner: Optional[str] = None,
    spark_master: Optional[str] = None,
    spark_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    ApplyBQSRSpark: Applies base quality score recalibration on Spark.

    Args:
        bam: Path to the input BAM file.
        fasta: Path to the reference FASTA file.
        recal_table: Path to the recalibration table for the BAM file.
        output_bam: Path to the output recalibrated BAM file.
        java_opts (optional): Additional Java options, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments for ApplyBQSRSpark.
        spark_runner (optional): Specify Spark runner. Options: "LOCAL", "SPARK", or "GCS".
        spark_master (optional): URL of the Spark Master for job submission. Use "local[number_of_cores]" for local execution.
        spark_extra (optional): Additional Spark arguments.
  
    Returns:
        subprocess.CompletedProcess: Contains information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/applybqsrspark",
        inputs=dict(
            bam=bam,
            fasta=fasta,
            recal_table=recal_table,
        ),
        outputs=dict(output_bam=output_bam),
        params={
            "java_opts": java_opts,
            "extra": extra,
            "spark_runner": spark_runner,
            "spark_master": spark_master,
            "spark_extra": spark_extra,
        },
         
    )


@collect_tool()
def applybqsrspark(
    *,
    bam: str,
    fasta: str,
    recal_table: str,
    output_bam: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
    spark_runner: Optional[str] = None,
    spark_master: Optional[str] = None,
    spark_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    ApplyBQSRSpark: Applies base quality score recalibration on Spark.

    Args:
        bam: Path to the input BAM file.
        fasta: Path to the reference FASTA file.
        recal_table: Path to the recalibration table for the BAM file.
        output_bam: Path to the output recalibrated BAM file.
        java_opts (optional): Additional Java options, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments for ApplyBQSRSpark.
        spark_runner (optional): Specify Spark runner. Options: "LOCAL", "SPARK", or "GCS".
        spark_master (optional): URL of the Spark Master for job submission. Use "local[number_of_cores]" for local execution.
        spark_extra (optional): Additional Spark arguments.
  
    Returns:
        subprocess.CompletedProcess: Contains information about the completed Snakemake process.
    """
    return run_applybqsrspark(
        bam=bam,
        fasta=fasta,
        recal_table=recal_table,
        output_bam=output_bam,
        java_opts=java_opts,
        extra=extra,
        spark_runner=spark_runner,
        spark_master=spark_master,
        spark_extra=spark_extra,
         
    )
