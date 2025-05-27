from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_insulation(
    *,
    mcool_file: str,
    output_tsv: str,
    window: List[int],
    view: Optional[str] = None,
    resolution: Optional[int] = None,
    chunksize: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate insulation score for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the input multiresolution cooler file (.mcool).
        output_tsv: Path to the output .tsv file with insulation scores and boundaries.
        window: List of window sizes for insulation score calculation, in bp.
        view (optional): Path to a bed-style file with region coordinates and names for analysis.
        resolution (optional): Resolution for the analysis (can also be specified as a wildcard in output_tsv).
        chunksize (optional): Number of pixels to process in each chunk.
        extra (optional): Additional arguments to pass to the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/cooltools/insulation",
        inputs=dict(mcool_file=mcool_file, view=view),
        outputs=dict(output_tsv=output_tsv),
        params=dict(
            window=window,
            resolution=resolution,
            chunksize=chunksize,
            extra=extra,
        ),
         
    )


@collect_tool()
def insulation(
    *,
    mcool_file: str,
    output_tsv: str,
    window: List[int],
    view: Optional[str] = None,
    resolution: Optional[int] = None,
    chunksize: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate insulation score for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the input multiresolution cooler file (.mcool).
        output_tsv: Path to the output .tsv file with insulation scores and boundaries.
        window: List of window sizes for insulation score calculation, in bp.
        view (optional): Path to a bed-style file with region coordinates and names for analysis.
        resolution (optional): Resolution for the analysis (can also be specified as a wildcard in output_tsv).
        chunksize (optional): Number of pixels to process in each chunk.
        extra (optional): Additional arguments to pass to the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_insulation(
        mcool_file=mcool_file,
        output_tsv=output_tsv,
        window=window,
        view=view,
        resolution=resolution,
        chunksize=chunksize,
        extra=extra,
         
    )
