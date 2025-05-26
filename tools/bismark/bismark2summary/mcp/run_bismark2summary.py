from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bismark2summary(
    *,
    bam: str,
    html: str,
    txt: str,
    extra: Optional[str] = None,
    title: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate summary graphical HTML report from several Bismark text report files.

    Args:
        bam: One or several (space separated) BAM file paths, aligned BAM files with Bismark reports in the same folder.
             It is recommended to add dependencies for all required reports using rules order or specifying them in the input section.
        html: Output HTML report path (e.g., 'bismark_summary_report.html').
        txt: Output TXT table path (e.g., 'bismark_summary_report.txt'), containing the same data as the HTML report but with suffix '.txt'.
        extra (optional): Any additional arguments.
        title (optional): Optional custom title for the report.
            
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/bismark/bismark2summary",
        inputs={"bam": bam},
        outputs={"html": html, "txt": txt},
        params={"extra": extra, "title": title},
         
    )


@collect_tool()
def bismark2summary(
    *,
    bam: str,
    html: str,
    txt: str,
    extra: Optional[str] = None,
    title: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate summary graphical HTML report from several Bismark text report files.

    Args:
        bam: One or several (space separated) BAM file paths, aligned BAM files with Bismark reports in the same folder.
             It is recommended to add dependencies for all required reports using rules order or specifying them in the input section.
        html: Output HTML report path (e.g., 'bismark_summary_report.html').
        txt: Output TXT table path (e.g., 'bismark_summary_report.txt'), containing the same data as the HTML report but with suffix '.txt'.
        extra (optional): Any additional arguments.
        title (optional): Optional custom title for the report.
            
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bismark2summary(
        bam=bam,
        html=html,
        txt=txt,
        extra=extra,
        title=title,
         
    )
