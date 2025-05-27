from typing import List, Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_plot(
    *,
    npo_files: List[str],
    pdf_output: Optional[str] = None,
    tsv_output: Optional[str] = None,
    json_output: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Plot Nonpareil results.

    Args:
        npo_files: List of input NPO files.
        pdf_output (optional): Path to the output PDF file with the plot.
        tsv_output (optional): Path to the output TSV file with summary stats.
        json_output (optional): Path to the output JSON file with detailed info.
        extra (optional): Additional program arguments (excluding `--pdf`, `--tsv`, or `--json`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    outputs = {}
    if pdf_output:
        outputs["pdf"] = pdf_output
    if tsv_output:
        outputs["tsv"] = tsv_output
    if json_output:
        outputs["json"] = json_output

    params = {"extra": extra} if extra else {}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/nonpareil/plot",
        inputs={"npo_files": npo_files},
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def plot(
    *,
    npo_files: List[str],
    pdf_output: Optional[str] = None,
    tsv_output: Optional[str] = None,
    json_output: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Plot Nonpareil results.

    Args:
        npo_files: List of input NPO files.
        pdf_output (optional): Path to the output PDF file with the plot.
        tsv_output (optional): Path to the output TSV file with summary stats.
        json_output (optional): Path to the output JSON file with detailed info.
        extra (optional): Additional program arguments (excluding `--pdf`, `--tsv`, or `--json`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_plot(
        npo_files=npo_files,
        pdf_output=pdf_output,
        tsv_output=tsv_output,
        json_output=json_output,
        extra=extra,
         
    )
