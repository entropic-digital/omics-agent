from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_flagstat(
    *,
    bam_file: str,
    flag_statistics: str,
     
) -> subprocess.CompletedProcess:
    """
    Outputs some statistics drawn from read flags using sambamba flagstat.

    Args:
        bam_file: Path to the BAM file.
        flag_statistics: Path to the output file containing flag statistics.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/sambamba/flagstat",
        inputs={"bam_file": bam_file},
        outputs={"flag_statistics": flag_statistics},
         
    )


@collect_tool()
def flagstat(
    *,
    bam_file: str,
    flag_statistics: str,
     
) -> subprocess.CompletedProcess:
    """
    Outputs some statistics drawn from read flags using sambamba flagstat.

    Args:
        bam_file: Path to the BAM file.
        flag_statistics: Path to the output file containing flag statistics.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_flagstat(bam_file=bam_file, flag_statistics=flag_statistics,      )
