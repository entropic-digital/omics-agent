from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_baserecalibratorspark(
    *,
    bam_file: str,
    fasta_reference: str,
    vcf_gz: str,
    recal_table: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
    spark_runner: Optional[str] = None,
    spark_master: Optional[str] = None,
    spark_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk BaseRecalibratorSpark.

    Args:
        bam_file: Input BAM file.
        fasta_reference: Fasta reference file.
        vcf_gz: VCF file with known variants (gzipped).
        recal_table: Output recalibration table for the BAM.
        java_opts (optional): Additional Java arguments, except `-XmX` or `-Djava.io.tmpdir`.
        extra (optional): Additional program arguments for `baserecalibratorspark`.
        spark_runner (optional): Set spark runner ("LOCAL", "SPARK", or "GCS").
        spark_master (optional): URL of the Spark Master for execution.
        spark_extra (optional): Additional Spark arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {}
    if java_opts:
        params["java_opts"] = java_opts
    if extra:
        params["extra"] = extra
    if spark_runner:
        params["spark_runner"] = spark_runner
    if spark_master:
        params["spark_master"] = spark_master
    if spark_extra:
        params["spark_extra"] = spark_extra

    return run_snake_wrapper(
        wrapper="file:tools/gatk/baserecalibratorspark",
        inputs=dict(
            bam_file=bam_file,
            fasta_reference=fasta_reference,
            vcf_gz=vcf_gz,
        ),
        outputs=dict(
            recal_table=recal_table,
        ),
        params=params,
         
    )


@collect_tool()
def baserecalibratorspark(
    *,
    bam_file: str,
    fasta_reference: str,
    vcf_gz: str,
    recal_table: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
    spark_runner: Optional[str] = None,
    spark_master: Optional[str] = None,
    spark_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk BaseRecalibratorSpark.

    Args:
        bam_file: Input BAM file.
        fasta_reference: Fasta reference file.
        vcf_gz: VCF file with known variants (gzipped).
        recal_table: Output recalibration table for the BAM.
        java_opts (optional): Additional Java arguments, except `-XmX` or `-Djava.io.tmpdir`.
        extra (optional): Additional program arguments for `baserecalibratorspark`.
        spark_runner (optional): Set spark runner ("LOCAL", "SPARK", or "GCS").
        spark_master (optional): URL of the Spark Master for execution.
        spark_extra (optional): Additional Spark arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_baserecalibratorspark(
        bam_file=bam_file,
        fasta_reference=fasta_reference,
        vcf_gz=vcf_gz,
        recal_table=recal_table,
        java_opts=java_opts,
        extra=extra,
        spark_runner=spark_runner,
        spark_master=spark_master,
        spark_extra=spark_extra,
         
    )
