from typing import List, Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_text(
    *,
    input_files: List[str],
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert bus files to TSV format.

    Args:
        input_files: List of input bus files.
        output_file: Path to the output TSV file.
        extra (optional): Additional optional parameters for the tool (besides --o/-output).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bustools/text",
        inputs={"input_files": input_files},
        outputs={"output_file": output_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def text(
    *,
    input_files: List[str],
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert bus files to TSV format.

    Args:
        input_files: List of input bus files.
        output_file: Path to the output TSV file.
        extra (optional): Additional optional parameters for the tool (besides --o/-output).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_text(
        input_files=input_files, output_file=output_file, extra=extra,      
    )
