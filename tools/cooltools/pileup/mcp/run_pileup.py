from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_pileup(
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
    Pileup features for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the multiresolution cooler file (.mcool).
        features_file: Path to the file containing features to pileup.
        output_file: Path to save the output file (.npz or .h5). Can include {resolution} wildcard.
        resolution (optional): Resolution for analysis. If not provided, can be inferred from the output wildcard.
        expected_file (optional): Path to the file with expected data.
        view_file (optional): Path to a bed-style file with region coordinates and names to use for analysis.
        extra (optional): Any additional arguments to pass.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {"resolution": resolution, "extra": extra}
    params = {key: value for key, value in params.items() if value is not None}

    return run_snake_wrapper(
        wrapper="file:tools/cooltools/pileup",
        inputs=dict(
            mcool_file=mcool_file,
            features_file=features_file,
            expected_file=expected_file,
            view_file=view_file,
        ),
        outputs=dict(output_file=output_file),
        params=params,
         
    )


@collect_tool()
def pileup(
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
    Pileup features for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the multiresolution cooler file (.mcool).
        features_file: Path to the file containing features to pileup.
        output_file: Path to save the output file (.npz or .h5). Can include {resolution} wildcard.
        resolution (optional): Resolution for analysis. If not provided, can be inferred from the output wildcard.
        expected_file (optional): Path to the file with expected data.
        view_file (optional): Path to a bed-style file with region coordinates and names to use for analysis.
        extra (optional): Any additional arguments to pass.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_pileup(
        mcool_file=mcool_file,
        features_file=features_file,
        output_file=output_file,
        resolution=resolution,
        expected_file=expected_file,
        view_file=view_file,
        extra=extra,
         
    )
