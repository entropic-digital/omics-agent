from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_collate(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Shuffles and groups reads together by their names using samtools collate.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path to the output SAM/BAM/CRAM file.
        extra (optional): Additional program arguments (excluding `-@/--threads`, `--reference`, `-o`, or `-O/--output-fmt`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/samtools/collate",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def collate(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Shuffles and groups reads together by their names using samtools collate.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path to the output SAM/BAM/CRAM file.
        extra (optional): Additional program arguments (excluding `-@/--threads`, `--reference`, `-o`, or `-O/--output-fmt`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collate(
        input_file=input_file,
        output_file=output_file,
        extra=extra,
         
    )
