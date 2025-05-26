from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bamqc(
    *,
    bam_file: str,
    qc_report: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run qualimap bamqc to create a QC report for aligned NGS data.

    Args:
        bam_file: BAM file of data aligned to genome.
        qc_report: Output QC report in TXT format (genome_results.txt).
        extra (optional): Additional program arguments for qualimap bamqc.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/qualimap/bamqc",
        inputs=dict(bam_file=bam_file),
        outputs=dict(qc_report=qc_report),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def bamqc(
    *,
    bam_file: str,
    qc_report: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run qualimap bamqc to create a QC report for aligned NGS data.

    Args:
        bam_file: BAM file of data aligned to genome.
        qc_report: Output QC report in TXT format (genome_results.txt).
        extra (optional): Additional program arguments for qualimap bamqc.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bamqc(
        bam_file=bam_file,
        qc_report=qc_report,
        extra=extra,
         
    )
