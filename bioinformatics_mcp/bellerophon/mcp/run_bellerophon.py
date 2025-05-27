from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_bellerophon(
    *,
    forward_reads: str,
    reverse_reads: str,
    output: str,
    sort: str = "none",
    sort_extra: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Filter mapped reads where the mapping spans a junction, retaining the 5-prime read.

    Args:
        forward_reads: Input file for forward reads (BAM format).
        reverse_reads: Input file for reverse reads (BAM format).
        output: Output file in SAM/BAM/CRAM format.
        sort: Sorting method; one of 'none', 'queryname', or 'coordinate' (default: 'none').
        sort_extra (optional): Additional arguments for the samtools sort command.
        extra (optional): Additional program arguments passed to Bellerophon.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bellerophon",
        inputs=dict(forward_reads=forward_reads, reverse_reads=reverse_reads),
        outputs=dict(output=output),
        params={
            "sort": sort,
            "sort_extra": sort_extra,
            "extra": extra,
        },
         
    )


@collect_tool()
def bellerophon(
    *,
    forward_reads: str,
    reverse_reads: str,
    output: str,
    sort: str = "none",
    sort_extra: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Filter mapped reads where the mapping spans a junction, retaining the 5-prime read.

    Args:
        forward_reads: Input file for forward reads (BAM format).
        reverse_reads: Input file for reverse reads (BAM format).
        output: Output file in SAM/BAM/CRAM format.
        sort: Sorting method; one of 'none', 'queryname', or 'coordinate' (default: 'none').
        sort_extra (optional): Additional arguments for the samtools sort command.
        extra (optional): Additional program arguments passed to Bellerophon.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bellerophon(
        forward_reads=forward_reads,
        reverse_reads=reverse_reads,
        output=output,
        sort=sort,
        sort_extra=sort_extra,
        extra=extra,
         
    )
