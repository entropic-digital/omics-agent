from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_collectrnaseqmetrics(
    *,
    bam_file: str,
    ref_flat_file: str,
    reference_fasta: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run picard CollectRnaSeqMetrics to generate QC metrics for RNA-seq data.

    Args:
        bam_file: BAM file of RNA-seq data aligned to genome.
        ref_flat_file: REF_FLAT formatted file of transcriptome annotations.
        reference_fasta (optional): Reference FASTA file.
        java_opts (optional): Additional arguments for the Java compiler (except -XmX or -Djava.io.tmpdir).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/picard/collectrnaseqmetrics",
        inputs={
            "bam_file": bam_file,
            "ref_flat_file": ref_flat_file,
            "reference_fasta": reference_fasta,
        },
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def collectrnaseqmetrics(
    *,
    bam_file: str,
    ref_flat_file: str,
    reference_fasta: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run picard CollectRnaSeqMetrics to generate QC metrics for RNA-seq data.

    Args:
        bam_file: BAM file of RNA-seq data aligned to genome.
        ref_flat_file: REF_FLAT formatted file of transcriptome annotations.
        reference_fasta (optional): Reference FASTA file.
        java_opts (optional): Additional arguments for the Java compiler (except -XmX or -Djava.io.tmpdir).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collectrnaseqmetrics(
        bam_file=bam_file,
        ref_flat_file=ref_flat_file,
        reference_fasta=reference_fasta,
        java_opts=java_opts,
        extra=extra,
         
    )
