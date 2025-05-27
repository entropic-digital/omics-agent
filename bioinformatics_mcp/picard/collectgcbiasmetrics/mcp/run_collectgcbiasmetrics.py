from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_collectgcbiasmetrics(
    *,
    bam_file: str,
    ref_flat: str,
    gc_metrics_txt: str,
    gc_metrics_pdf: str,
    gc_summary_txt: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run picard CollectGcBiasMetrics to generate QC metrics pertaining to GC bias.

    Args:
        bam_file: BAM file of RNA-seq data aligned to genome.
        ref_flat: REF_FLAT formatted file of transcriptome annotations.
        gc_metrics_txt: Output GC metrics text file.
        gc_metrics_pdf: Output GC metrics PDF figure.
        gc_summary_txt: Output GC summary metrics text file.
        java_opts (optional): Additional arguments to pass to the Java compiler.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/picard/collectgcbiasmetrics",
        inputs={
            "bam_file": bam_file,
            "ref_flat": ref_flat,
        },
        outputs={
            "gc_metrics_txt": gc_metrics_txt,
            "gc_metrics_pdf": gc_metrics_pdf,
            "gc_summary_txt": gc_summary_txt,
        },
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def collectgcbiasmetrics(
    *,
    bam_file: str,
    ref_flat: str,
    gc_metrics_txt: str,
    gc_metrics_pdf: str,
    gc_summary_txt: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run picard CollectGcBiasMetrics to generate QC metrics pertaining to GC bias.

    Args:
        bam_file: BAM file of RNA-seq data aligned to genome.
        ref_flat: REF_FLAT formatted file of transcriptome annotations.
        gc_metrics_txt: Output GC metrics text file.
        gc_metrics_pdf: Output GC metrics PDF figure.
        gc_summary_txt: Output GC summary metrics text file.
        java_opts (optional): Additional arguments to pass to the Java compiler.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collectgcbiasmetrics(
        bam_file=bam_file,
        ref_flat=ref_flat,
        gc_metrics_txt=gc_metrics_txt,
        gc_metrics_pdf=gc_metrics_pdf,
        gc_summary_txt=gc_summary_txt,
        java_opts=java_opts,
        extra=extra,
         
    )
