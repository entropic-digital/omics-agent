from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_dots(
    *,
    mcool_file: str,
    expected_file: str,
    view_file: Optional[str] = None,
    output_file: str,
    resolution: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate cis eigenvectors for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the input multiresolution cooler file (.mcool).
        expected_file: Path to the expected file.
        view_file (optional): Path to a bed-style file with region coordinates
            and names to use for analysis.
        output_file: Path to the .bedpe file with coordinates of detected dots.
            Can include a {resolution} wildcard.
        resolution (optional): Resolution for the analysis. Optional if provided as a wildcard in the output file.
        extra (optional): Additional arguments to pass to the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/cooltools/dots",
        inputs={
            "mcool_file": mcool_file,
            "expected_file": expected_file,
            **({"view_file": view_file} if view_file else {}),
        },
        outputs={"output_file": output_file},
        params={
            **({"resolution": resolution} if resolution else {}),
            **({"extra": extra} if extra else {}),
        },
         
    )


@collect_tool()
def dots(
    *,
    mcool_file: str,
    expected_file: str,
    view_file: Optional[str] = None,
    output_file: str,
    resolution: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate cis eigenvectors for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the input multiresolution cooler file (.mcool).
        expected_file: Path to the expected file.
        view_file (optional): Path to a bed-style file with region coordinates
            and names to use for analysis.
        output_file: Path to the .bedpe file with coordinates of detected dots.
            Can include a {resolution} wildcard.
        resolution (optional): Resolution for the analysis. Optional if provided as a wildcard in the output file.
        extra (optional): Additional arguments to pass to the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_dots(
        mcool_file=mcool_file,
        expected_file=expected_file,
        view_file=view_file,
        output_file=output_file,
        resolution=resolution,
        extra=extra,
         
    )
