from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_bismark2report(
    *,
    alignment_report: str,
    nucleotide_report: Optional[str] = None,
    dedup_report: Optional[str] = None,
    splitting_report: Optional[str] = None,
    mbias_report: Optional[str] = None,
    skip_optional_reports: bool = False,
    extra: Optional[str] = None,
    html: str,
    html_dir: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate graphical HTML report from Bismark reports.

    Args:
        alignment_report: Path to the alignment report. Required.
        nucleotide_report (optional): Path to the Bismark nucleotide coverage report.
        dedup_report (optional): Path to the deduplication report.
        splitting_report (optional): Path to the Bismark methylation extractor splitting report.
        mbias_report (optional): Path to the Bismark methylation extractor mbias report.
        skip_optional_reports: Whether to skip optional reports not mentioned. Uses 'none' if true.
        extra (optional): Any additional arguments to pass to bismark2report.
        html: Path to the output HTML file (non-batch mode).
        html_dir (optional): Path to the output directory for HTML reports (batch mode).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bismark/bismark2report",
        inputs={
            "alignment_report": alignment_report,
            "nucleotide_report": nucleotide_report,
            "dedup_report": dedup_report,
            "splitting_report": splitting_report,
            "mbias_report": mbias_report,
        },
        params={
            "skip_optional_reports": skip_optional_reports,
            "extra": extra,
        },
        outputs={
            "html": html,
            "html_dir": html_dir,
        },
         
    )


@collect_tool()
def bismark2report(
    *,
    alignment_report: str,
    nucleotide_report: Optional[str] = None,
    dedup_report: Optional[str] = None,
    splitting_report: Optional[str] = None,
    mbias_report: Optional[str] = None,
    skip_optional_reports: bool = False,
    extra: Optional[str] = None,
    html: str,
    html_dir: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate graphical HTML report from Bismark reports.

    Args:
        alignment_report: Path to the alignment report. Required.
        nucleotide_report (optional): Path to the Bismark nucleotide coverage report.
        dedup_report (optional): Path to the deduplication report.
        splitting_report (optional): Path to the Bismark methylation extractor splitting report.
        mbias_report (optional): Path to the Bismark methylation extractor mbias report.
        skip_optional_reports: Whether to skip optional reports not mentioned. Uses 'none' if true.
        extra (optional): Any additional arguments to pass to bismark2report.
        html: Path to the output HTML file (non-batch mode).
        html_dir (optional): Path to the output directory for HTML reports (batch mode).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bismark2report(
        alignment_report=alignment_report,
        nucleotide_report=nucleotide_report,
        dedup_report=dedup_report,
        splitting_report=splitting_report,
        mbias_report=mbias_report,
        skip_optional_reports=skip_optional_reports,
        extra=extra,
        html=html,
        html_dir=html_dir,
         
    )
