from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_fetch(
    *,
    file_id: str,
    output_format: str,
    optional_param: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    EGA Fetch: Fetch files from EGA with pyega3.

    Args:
        file_id: The identifier of the file to fetch from EGA.
        output_format: The file format to fetch (e.g., BAM, CRAM, VCF, BCF).
        optional_param (optional): Additional optional parameter for customization.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/ega/fetch",
        inputs=dict(file_id=file_id),
        params={"output_format": output_format, "optional_param": optional_param}
        if optional_param
        else {"output_format": output_format},
         
    )


@collect_tool()
def fetch(
    *,
    file_id: str,
    output_format: str,
    optional_param: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    EGA Fetch: Fetch files from EGA with pyega3.

    Args:
        file_id: The identifier of the file to fetch from EGA.
        output_format: The file format to fetch (e.g., BAM, CRAM, VCF, BCF).
        optional_param (optional): Additional optional parameter for customization.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_fetch(
        file_id=file_id,
        output_format=output_format,
        optional_param=optional_param,
         
    )
