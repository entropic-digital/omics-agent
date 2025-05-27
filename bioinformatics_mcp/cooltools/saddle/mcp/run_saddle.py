from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_saddle(
    *,
    cooler_file: str,
    track_file: str,
    expected_file: str,
    output_prefix: str,
    view_file: Optional[str] = None,
    range: Optional[str] = None,
    resolution: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate a saddle for a resolution in an .mcool file using a track.

    Args:
        cooler_file: A multiresolution cooler file (.mcool).
        track_file: Input track file.
        expected_file: Input expected file.
        output_prefix: Prefix for all output files.
        view_file (optional): A BED-style file with region coordinates and names
                              to use for analysis.
        range (optional): Range of values from the track to use.
                          Example: '--qrange 0.01 0.99' or '--range 0 5'.
        resolution (optional): Resolution for the analysis. This can be omitted
                               if specified as a wildcard in the output_prefix.
        extra (optional): Additional arguments to pass to the tool.
  
    Returns:
        CompletedProcess: Information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/cooltools/saddle",
        inputs=dict(
            cooler_file=cooler_file,
            track_file=track_file,
            expected_file=expected_file,
            view_file=view_file,
        ),
        outputs=dict(
            output_prefix=output_prefix,
        ),
        params=dict(
            range=range,
            resolution=resolution,
            extra=extra,
        ),
         
    )


@collect_tool()
def saddle(
    *,
    cooler_file: str,
    track_file: str,
    expected_file: str,
    output_prefix: str,
    view_file: Optional[str] = None,
    range: Optional[str] = None,
    resolution: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate a saddle for a resolution in an .mcool file using a track.

    Args:
        cooler_file: A multiresolution cooler file (.mcool).
        track_file: Input track file.
        expected_file: Input expected file.
        output_prefix: Prefix for all output files.
        view_file (optional): A BED-style file with region coordinates and names
                              to use for analysis.
        range (optional): Range of values from the track to use.
                          Example: '--qrange 0.01 0.99' or '--range 0 5'.
        resolution (optional): Resolution for the analysis. This can be omitted
                               if specified as a wildcard in the output_prefix.
        extra (optional): Additional arguments to pass to the tool.
  
    Returns:
        CompletedProcess: Information about the completed Snakemake process.
    """
    return run_saddle(
        cooler_file=cooler_file,
        track_file=track_file,
        expected_file=expected_file,
        output_prefix=output_prefix,
        view_file=view_file,
        range=range,
        resolution=resolution,
        extra=extra,
         
    )
