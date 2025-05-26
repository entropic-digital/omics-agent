from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_expected_trans(
    *,
    mcool_file: str,
    output_tsv: str,
    resolution: Optional[str] = None,
    view_file: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate trans expected for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the multiresolution cooler file (.mcool).
        output_tsv: Path to the output .tsv file with mean interaction frequency
                    between chromosomes. Can include a {resolution} wildcard.
        resolution (optional): The resolution to use for the analysis. Optional
                               if specified as a wildcard in the output.
        view_file (optional): Bed-style file with region coordinates and names to
                              use for analysis.
        extra (optional): Any additional arguments to pass.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/cooltools/expected_trans",
        inputs=dict(mcool_file=mcool_file, view_file=view_file)
        if view_file
        else dict(mcool_file=mcool_file),
        outputs={"output_tsv": output_tsv},
        params={"resolution": resolution, "extra": extra}
        if resolution or extra
        else {},
         
    )


@collect_tool()
def expected_trans(
    *,
    mcool_file: str,
    output_tsv: str,
    resolution: Optional[str] = None,
    view_file: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate trans expected for a resolution in an .mcool file as a decorated MCP tool.

    Args:
        mcool_file: Path to the multiresolution cooler file (.mcool).
        output_tsv: Path to the output .tsv file with mean interaction frequency
                    between chromosomes. Can include a {resolution} wildcard.
        resolution (optional): The resolution to use for the analysis. Optional
                               if specified as a wildcard in the output.
        view_file (optional): Bed-style file with region coordinates and names to
                              use for analysis.
        extra (optional): Any additional arguments to pass.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_expected_trans(
        mcool_file=mcool_file,
        output_tsv=output_tsv,
        resolution=resolution,
        view_file=view_file,
        extra=extra,
         
    )
