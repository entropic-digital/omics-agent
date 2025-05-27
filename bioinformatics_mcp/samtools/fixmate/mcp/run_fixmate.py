from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_fixmate(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Use samtools to correct mate information after BWA mapping.

    Args:
        input_file: Path to input BAM or SAM file.
        output_file: Path to output BAM or SAM file.
        extra (optional): Additional parameters for the samtools command (excluding -@/--threads or -O/--output-fmt).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/samtools/fixmate",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def fixmate(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Use samtools to correct mate information after BWA mapping.

    Args:
        input_file: Path to input BAM or SAM file.
        output_file: Path to output BAM or SAM file.
        extra (optional): Additional parameters for the samtools command (excluding -@/--threads or -O/--output-fmt).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_fixmate(
        input_file=input_file,
        output_file=output_file,
        extra=extra,
         
    )
