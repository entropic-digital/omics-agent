from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_expected_cis(
    *,
    mcool_file: str,
    output_tsv: str,
    view: Optional[str] = None,
    resolution: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate cis expected for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the multiresolution cooler file (.mcool).
        output_tsv: Path to the output .tsv file for storing the mean interaction frequency.
        view (optional): Path to a bed-style file with region coordinates and names to use for analysis.
        resolution (optional): Resolution for the analysis, can be omitted if specified as a wildcard in the output.
        extra (optional): Any additional arguments to pass.
  
    Returns:
        subprocess.CompletedProcess: CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {}
    if resolution is not None:
        params["resolution"] = resolution
    if extra is not None:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/cooltools/expected_cis",
        inputs={"mcool_file": mcool_file, "view": view}
        if view
        else {"mcool_file": mcool_file},
        outputs={"output_tsv": output_tsv},
        params=params,
         
    )


@collect_tool()
def expected_cis(
    *,
    mcool_file: str,
    output_tsv: str,
    view: Optional[str] = None,
    resolution: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate cis expected for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the multiresolution cooler file (.mcool).
        output_tsv: Path to the output .tsv file for storing the mean interaction frequency.
        view (optional): Path to a bed-style file with region coordinates and names to use for analysis.
        resolution (optional): Resolution for the analysis, can be omitted if specified as a wildcard in the output.
        extra (optional): Any additional arguments to pass.
  
    Returns:
        subprocess.CompletedProcess: CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_expected_cis(
        mcool_file=mcool_file,
        output_tsv=output_tsv,
        view=view,
        resolution=resolution,
        extra=extra,
         
    )
