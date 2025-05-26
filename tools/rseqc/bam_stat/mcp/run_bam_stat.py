from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bam_stat(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Summarizing mapping statistics of a BAM or SAM file.

    Args:
        input_file: Path to BAM/SAM file(s) to summarize.
        output_file: Path to the summary.
        extra (optional): Optional argument besides `--input-file`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/rseqc/bam_stat",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def bam_stat(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Summarizing mapping statistics of a BAM or SAM file.

    Args:
        input_file: Path to BAM/SAM file(s) to summarize.
        output_file: Path to the summary.
        extra (optional): Optional argument besides `--input-file`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bam_stat(
        input_file=input_file, output_file=output_file, extra=extra,      
    )
