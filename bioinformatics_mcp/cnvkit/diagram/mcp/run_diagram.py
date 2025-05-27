from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_diagram(
    *,
    cns_file: Optional[str] = None,
    cnr_or_cnn_file: Optional[str] = None,
    output_pdf: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Draws copy number (either individual bins or segments) on chromosomes as an ideogram.

    If both the bin-level log2 ratios and segmentation calls are given,
    they are displayed side-by-side on each chromosome (segments on the left side, bins on the right side).

    Args:
        cns_file (optional): Path to a CNS file (if CNR/CCN is provided).
        cnr_or_cnn_file (optional): Path to a CNR or CNN file (if CNS is provided).
        output_pdf: Path to the generated PDF report.
        extra (optional): Additional parameters forwarded to the cnvkit diagram command.
  
    Returns:
        CompletedProcess: Contains information about the completed Snakemake process.
    """
    inputs = {}
    if cns_file:
        inputs["cns_file"] = cns_file
    if cnr_or_cnn_file:
        inputs["cnr_or_cnn_file"] = cnr_or_cnn_file

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/cnvkit/diagram",
        inputs=inputs,
        outputs={"output_pdf": output_pdf},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def diagram(
    *,
    cns_file: Optional[str] = None,
    cnr_or_cnn_file: Optional[str] = None,
    output_pdf: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Draws copy number (either individual bins or segments) on chromosomes as an ideogram.

    If both the bin-level log2 ratios and segmentation calls are given,
    they are displayed side-by-side on each chromosome (segments on the left side, bins on the right side).

    Args:
        cns_file (optional): Path to a CNS file (if CNR/CCN is provided).
        cnr_or_cnn_file (optional): Path to a CNR or CNN file (if CNS is provided).
        output_pdf: Path to the generated PDF report.
        extra (optional): Additional parameters forwarded to the cnvkit diagram command.
  
    Returns:
        CompletedProcess: Contains information about the completed Snakemake process.
    """
    return run_diagram(
        cns_file=cns_file,
        cnr_or_cnn_file=cnr_or_cnn_file,
        output_pdf=output_pdf,
        extra=extra,
         
    )
