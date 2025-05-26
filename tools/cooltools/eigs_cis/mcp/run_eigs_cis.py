from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_eigs_cis(
    *,
    mcool_file: str,
    vecs: str,
    lams: str,
    bigwig: str,
    resolution: Optional[int] = None,
    phasing_track: Optional[str] = None,
    view: Optional[str] = None,
    track_col_name: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate cis eigenvectors for a resolution in an .mcool file.

    Args:
        mcool_file: Path to a multiresolution cooler file (.mcool) to analyze.
        vecs: Path to the output .tsv file with cis eigenvector values at each bin.
        lams: Path to the output file containing eigenvalues.
        bigwig: Path to the output .bigwig file for first eigenvector visualization.
        resolution (optional): Resolution for the analysis. Can be specified in the output instead.
        phasing_track (optional): Path to a phasing track file.
        view (optional): Path to a bed-style file with region coordinates and names to use for analysis.
        track_col_name (optional): Column name in the track file to use.
        extra (optional): Additional arguments to pass to the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "mcool_file": mcool_file,
        "phasing_track": phasing_track,
        "view": view,
    }
    inputs = {k: v for k, v in inputs.items() if v is not None}

    params = {
        "resolution": resolution,
        "track_col_name": track_col_name,
        "extra": extra,
    }
    params = {k: v for k, v in params.items() if v is not None}

    outputs = {
        "vecs": vecs,
        "lams": lams,
        "bigwig": bigwig,
    }

    return run_snake_wrapper(
        wrapper="file:tools/cooltools/eigs_cis",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def eigs_cis(
    *,
    mcool_file: str,
    vecs: str,
    lams: str,
    bigwig: str,
    resolution: Optional[int] = None,
    phasing_track: Optional[str] = None,
    view: Optional[str] = None,
    track_col_name: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate cis eigenvectors for a resolution in an .mcool file.

    Args:
        mcool_file: Path to a multiresolution cooler file (.mcool) to analyze.
        vecs: Path to the output .tsv file with cis eigenvector values at each bin.
        lams: Path to the output file containing eigenvalues.
        bigwig: Path to the output .bigwig file for first eigenvector visualization.
        resolution (optional): Resolution for the analysis. Can be specified in the output instead.
        phasing_track (optional): Path to a phasing track file.
        view (optional): Path to a bed-style file with region coordinates and names to use for analysis.
        track_col_name (optional): Column name in the track file to use.
        extra (optional): Additional arguments to pass to the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_eigs_cis(
        mcool_file=mcool_file,
        vecs=vecs,
        lams=lams,
        bigwig=bigwig,
        resolution=resolution,
        phasing_track=phasing_track,
        view=view,
        track_col_name=track_col_name,
        extra=extra,
         
    )
