from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_calmd(
    *,
    input_file: str,
    output_file: str,
    index_file: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculates MD and NM tags.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path to the output SAM/BAM/CRAM file.
        index_file (optional): Path to the optional output index file.
        extra (optional): Additional program arguments (except `-@/--threads`, `--write-index`, `-m`, `-o`, `-O/--output-fmt`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/samtools/calmd",
        inputs=dict(input_file=input_file),
        outputs=dict(output_file=output_file, index_file=index_file)
        if index_file
        else {"output_file": output_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def calmd(
    *,
    input_file: str,
    output_file: str,
    index_file: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculates MD and NM tags.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path to the output SAM/BAM/CRAM file.
        index_file (optional): Path to the optional output index file.
        extra (optional): Additional program arguments (except `-@/--threads`, `--write-index`, `-m`, `-o`, `-O/--output-fmt`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_calmd(
        input_file=input_file,
        output_file=output_file,
        index_file=index_file,
        extra=extra,
         
    )
