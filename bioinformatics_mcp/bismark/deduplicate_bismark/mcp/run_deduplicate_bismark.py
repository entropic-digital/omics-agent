from typing import List, Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_deduplicate_bismark(
    *,
    bam_files: List[str],
    extra: Optional[str] = None,
    output_bam: Optional[str] = None,
    output_report: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Deduplicate Bismark Bam Files.

    Args:
        bam_files: List of paths to one or multiple *.bam files aligned by Bismark.
        extra (optional): Additional deduplicate_bismark arguments.
        output_bam (optional): Resultant bam file path. If not provided, will default to `NAME.deduplicated.bam`.
        output_report (optional): Resultant deduplication report path. If not provided, will default to `NAME.deduplication_report.txt`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"bam_files": bam_files}
    params = {"extra": extra} if extra else {}
    outputs = (
        {"bam": output_bam, "report": output_report}
        if output_bam or output_report
        else {}
    )

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bismark/deduplicate_bismark",
        inputs=inputs,
        params=params,
        outputs=outputs,
         
    )


@collect_tool()
def deduplicate_bismark(
    *,
    bam_files: List[str],
    extra: Optional[str] = None,
    output_bam: Optional[str] = None,
    output_report: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Deduplicate Bismark Bam Files.

    Args:
        bam_files: List of paths to one or multiple *.bam files aligned by Bismark.
        extra (optional): Additional deduplicate_bismark arguments.
        output_bam (optional): Resultant bam file path. If not provided, will default to `NAME.deduplicated.bam`.
        output_report (optional): Resultant deduplication report path. If not provided, will default to `NAME.deduplication_report.txt`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_deduplicate_bismark(
        bam_files=bam_files,
        extra=extra,
        output_bam=output_bam,
        output_report=output_report,
         
    )
