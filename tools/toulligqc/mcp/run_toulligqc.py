from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_toulligqc(
    *,
    input_path: str,
    output_path: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    A post sequencing QC tool for Oxford Nanopore sequencers.

    Args:
        input_path: Path to input data. Can be either a sequencing summary file, fastq file
            (uncompressed/compressed) or bam file.
        output_path: Path to store the QC results report and plots.
        extra (optional): Optional parameters for `toulligqc`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/toulligqc",
        inputs=dict(input=input_path),
        outputs=dict(output=output_path),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def toulligqc(
    *,
    input_path: str,
    output_path: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    A post sequencing QC tool for Oxford Nanopore sequencers.

    Args:
        input_path: Path to input data. Can be either a sequencing summary file, fastq file
            (uncompressed/compressed) or bam file.
        output_path: Path to store the QC results report and plots.
        extra (optional): Optional parameters for `toulligqc`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_toulligqc(
        input_path=input_path,
        output_path=output_path,
        extra=extra,
         
    )
