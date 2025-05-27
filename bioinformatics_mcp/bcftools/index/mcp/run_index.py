from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    input_file: str,
    output: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index VCF/BCF file.

    Args:
        input_file: Path to the input VCF/BCF file to be indexed.
        output (optional): Path to the output index file. If not provided, it will be determined automatically.
        extra (optional): Additional command-line arguments to pass to bcftools (excluding `--threads`, `-o/--output`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bcftools/index",
        inputs={"input_file": input_file},
        outputs={"output": output} if output else {},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def index(
    *,
    input_file: str,
    output: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index VCF/BCF file.

    Args:
        input_file: Path to the input VCF/BCF file to be indexed.
        output (optional): Path to the output index file. If not provided, it will be determined automatically.
        extra (optional): Additional command-line arguments to pass to bcftools (excluding `--threads`, `-o/--output`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        input_file=input_file,
        output=output,
        extra=extra,
         
    )
