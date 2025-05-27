from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_coolpuppy(
    *,
    mcool_file: str,
    features_file: str,
    output_file: str,
    resolution: Optional[int] = None,
    expected_file: Optional[str] = None,
    view_file: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Executes coolpup.py to perform pileup analysis for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the multiresolution cooler file (.mcool).
        features_file: Path to the file containing features to pileup.
        output_file: Path to the output file (.clpy, HDF5-based format).
        resolution (optional): Analysis resolution, can also be a wildcard in the output file.
        expected_file (optional): Path to the file with expected values.
        view_file (optional): Path to a bed-style file with region coordinates and names for analysis.
        extra (optional): Additional arguments to pass to the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/coolpuppy",
        inputs=dict(
            mcool_file=mcool_file,
            features_file=features_file,
            expected_file=expected_file,
            view_file=view_file,
        ),
        outputs=dict(output_file=output_file),
        params=dict(
            resolution=resolution,
            extra=extra,
        ),
         
    )


@collect_tool()
def coolpuppy(
    *,
    mcool_file: str,
    features_file: str,
    output_file: str,
    resolution: Optional[int] = None,
    expected_file: Optional[str] = None,
    view_file: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Executes coolpup.py to perform pileup analysis for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the multiresolution cooler file (.mcool).
        features_file: Path to the file containing features to pileup.
        output_file: Path to the output file (.clpy, HDF5-based format).
        resolution (optional): Analysis resolution, can also be a wildcard in the output file.
        expected_file (optional): Path to the file with expected values.
        view_file (optional): Path to a bed-style file with region coordinates and names for analysis.
        extra (optional): Additional arguments to pass to the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_coolpuppy(
        mcool_file=mcool_file,
        features_file=features_file,
        output_file=output_file,
        resolution=resolution,
        expected_file=expected_file,
        view_file=view_file,
        extra=extra,
         
    )
