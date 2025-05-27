from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_peaks(
    *,
    treatment: str,
    background: str,
    enriched_regions: str,
    bed: Optional[str] = None,
    matrix: Optional[str] = None,
    extra: Optional[str] = None,
    log: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Find broad enriched domains in ChIP-Seq data with epic.

    Args:
        treatment: Path to the treatment ChIP .bed(.gz/.bz) files.
        background: Path to the background input .bed(.gz/.bz) files.
        enriched_regions: Path to the output file with enriched peaks.
        bed (optional): Path to the optional output file in a bed format.
        matrix (optional): Path to the optional gzipped matrix of read counts.
        extra (optional): Additional parameters for the tool.
        log (optional): Path to the optional file to write the log output to.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = dict(
        treatment=treatment,
        background=background,
    )
    outputs = dict(
        enriched_regions=enriched_regions,
        bed=bed,
        matrix=matrix,
    )
    params = dict(
        extra=extra,
        log=log,
    )

    # Remove keys with None values from outputs and params
    outputs = {k: v for k, v in outputs.items() if v is not None}
    params = {k: v for k, v in params.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/epic/peaks",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def peaks(
    *,
    treatment: str,
    background: str,
    enriched_regions: str,
    bed: Optional[str] = None,
    matrix: Optional[str] = None,
    extra: Optional[str] = None,
    log: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Find broad enriched domains in ChIP-Seq data with epic.

    Args:
        treatment: Path to the treatment ChIP .bed(.gz/.bz) files.
        background: Path to the background input .bed(.gz/.bz) files.
        enriched_regions: Path to the output file with enriched peaks.
        bed (optional): Path to the optional output file in a bed format.
        matrix (optional): Path to the optional gzipped matrix of read counts.
        extra (optional): Additional parameters for the tool.
        log (optional): Path to the optional file to write the log output to.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_peaks(
        treatment=treatment,
        background=background,
        enriched_regions=enriched_regions,
        bed=bed,
        matrix=matrix,
        extra=extra,
        log=log,
         
    )
