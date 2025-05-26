from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_eigs_trans(
    *,
    mcool_file: str,
    vecs: str,
    lams: str,
    bigwig: str,
    resolution: Optional[int] = None,
    phasing_track: Optional[str] = None,
    track_col_name: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate trans eigenvectors for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the multiresolution cooler file (.mcool).
        vecs: Path to save the .tsv file with values of trans eigenvectors at each bin.
        lams: Path to save the file with eigenvalues.
        bigwig: Path to save the .bigwig file for visualization of the first eigenvector.
        resolution (optional): Resolution for the analysis. May also be specified via wildcard in the output.
        phasing_track (optional): Path to the phasing track file.
        track_col_name (optional): Column name in the track file to use.
        extra (optional): Additional arguments to pass.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/cooltools/eigs_trans",
        inputs=dict(mcool_file=mcool_file, phasing_track=phasing_track),
        outputs=dict(vecs=vecs, lams=lams, bigwig=bigwig),
        params={
            "resolution": resolution,
            "track_col_name": track_col_name,
            "extra": extra,
        },
         
    )


@collect_tool()
def eigs_trans(
    *,
    mcool_file: str,
    vecs: str,
    lams: str,
    bigwig: str,
    resolution: Optional[int] = None,
    phasing_track: Optional[str] = None,
    track_col_name: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate trans eigenvectors for a resolution in an .mcool file.

    Args:
        mcool_file: Path to the multiresolution cooler file (.mcool).
        vecs: Path to save the .tsv file with values of trans eigenvectors at each bin.
        lams: Path to save the file with eigenvalues.
        bigwig: Path to save the .bigwig file for visualization of the first eigenvector.
        resolution (optional): Resolution for the analysis. May also be specified via wildcard in the output.
        phasing_track (optional): Path to the phasing track file.
        track_col_name (optional): Column name in the track file to use.
        extra (optional): Additional arguments to pass.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_eigs_trans(
        mcool_file=mcool_file,
        vecs=vecs,
        lams=lams,
        bigwig=bigwig,
        resolution=resolution,
        phasing_track=phasing_track,
        track_col_name=track_col_name,
        extra=extra,
         
    )
