from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_stats(
    *,
    bam_file: str,
    bamstats_file: str,
    optional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Use bamtools to collect statistics from a BAM file.

    Args:
        bam_file: Path to the input BAM file.
        bamstats_file: Path to the output BAM stats file.
        optional_params (optional): Additional parameters to pass to bamtools.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bamtools/stats",
        inputs={"bam_file": bam_file},
        output_files={"bamstats_file": bamstats_file},
        params={"optional_params": optional_params} if optional_params else {},
         
    )


@collect_tool()
def stats(
    *,
    bam_file: str,
    bamstats_file: str,
    optional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Use bamtools to collect statistics from a BAM file.

    Args:
        bam_file: Path to the input BAM file.
        bamstats_file: Path to the output BAM stats file.
        optional_params (optional): Additional parameters to pass to bamtools.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_stats(
        bam_file=bam_file,
        bamstats_file=bamstats_file,
        optional_params=optional_params,
         
    )
