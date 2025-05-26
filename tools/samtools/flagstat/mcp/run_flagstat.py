from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_flagstat(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Use samtools to create a flagstat file from a BAM or SAM file.

    Args:
        input_file: Path to the input BAM or SAM file (.bam, .sam).
        output_file: Path to the output flagstat file (.flagstat).
        extra (optional): Additional program arguments (not `-@/--threads`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/samtools/flagstat",
        inputs=dict(input_file=input_file),
        outputs=dict(output_file=output_file),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def flagstat(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Use samtools to create a flagstat file from a BAM or SAM file.

    Args:
        input_file: Path to the input BAM or SAM file (.bam, .sam).
        output_file: Path to the output flagstat file (.flagstat).
        extra (optional): Additional program arguments (not `-@/--threads`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_flagstat(
        input_file=input_file, output_file=output_file, extra=extra,      
    )
