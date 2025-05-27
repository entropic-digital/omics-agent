from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_rnaseq(
    *,
    bam_file: str,
    gtf_file: str,
    qc_report: str,
     
) -> subprocess.CompletedProcess:
    """
    Run qualimap rnaseq to create a QC report for RNA-seq data.

    Args:
        bam_file: BAM file of RNA-seq data aligned to genome.
        gtf_file: GTF file containing genome annotations.
        qc_report: QC report output file in html/pdf format.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/qualimap/rnaseq",
        inputs=dict(bam_file=bam_file, gtf_file=gtf_file),
        outputs=dict(qc_report=qc_report),
         
    )


@collect_tool()
def rnaseq(
    *,
    bam_file: str,
    gtf_file: str,
    qc_report: str,
     
) -> subprocess.CompletedProcess:
    """
    Run qualimap rnaseq to create a QC report for RNA-seq data.

    Args:
        bam_file: BAM file of RNA-seq data aligned to genome.
        gtf_file: GTF file containing genome annotations.
        qc_report: QC report output file in html/pdf format.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_rnaseq(
        bam_file=bam_file, gtf_file=gtf_file, qc_report=qc_report,      
    )
