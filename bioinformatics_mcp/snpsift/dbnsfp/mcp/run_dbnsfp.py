from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_dbnsfp(
    *,
    calls: str,
    dbnsfp_file: str,
    annotated_calls: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Annotate using integrated annotation from dbNSFP with SnpSift.

    Args:
        calls: Path to the file containing calls to be annotated.
        dbnsfp_file: Path to the dbNSFP text file.
        annotated_calls: Path to the output file with annotated calls.
        extra (optional): Additional parameters for customizing the annotation process.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/snpsift/dbnsfp",
        inputs=dict(calls=calls, dbnsfp_file=dbnsfp_file),
        outputs=dict(annotated_calls=annotated_calls),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def dbnsfp_tool(
    *,
    calls: str,
    dbnsfp_file: str,
    annotated_calls: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Annotate using integrated annotation from dbNSFP with SnpSift.

    Args:
        calls: Path to the file containing calls to be annotated.
        dbnsfp_file: Path to the dbNSFP text file.
        annotated_calls: Path to the output file with annotated calls.
        extra (optional): Additional parameters for customizing the annotation process.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_dbnsfp(
        calls=calls,
        dbnsfp_file=dbnsfp_file,
        annotated_calls=annotated_calls,
        extra=extra,
         
    )
