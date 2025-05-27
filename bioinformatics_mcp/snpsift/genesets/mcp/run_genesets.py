from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_genesets(
    *,
    calls_file: str,
    gmt_file: str,
    annotated_calls_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Annotate using GMT genes sets with SnpSift.

    Args:
        calls_file: File containing calls to be annotated.
        gmt_file: GMT-formatted annotation file.
        annotated_calls_file: File to store the annotated calls.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/snpsift/genesets",
        inputs=dict(calls=calls_file, annotations=gmt_file),
        outputs=dict(annotated_calls=annotated_calls_file),
         
    )


@collect_tool()
def genesets(
    *,
    calls_file: str,
    gmt_file: str,
    annotated_calls_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Annotate using GMT genes sets with SnpSift.

    Args:
        calls_file: File containing calls to be annotated.
        gmt_file: GMT-formatted annotation file.
        annotated_calls_file: File to store the annotated calls.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_genesets(
        calls_file=calls_file,
        gmt_file=gmt_file,
        annotated_calls_file=annotated_calls_file,
         
    )
