from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_rubic(
    *,
    seg: str,
    markers: str,
    genefile: Optional[str] = None,
    out_gains: str,
    out_losses: str,
    out_plots: str,
    fdr: Optional[float] = 0.25,
     
) -> subprocess.CompletedProcess:
    """
    RUBIC detects recurrent copy number alterations using copy number breaks.

    Args:
        seg: Segmentation file containing copy number profiles from multiple tumor samples.
        markers: File with marker positions.
        genefile (optional): File path to use custom gene file. If not specified, the default file is used.
        out_gains: File to store recurrent gains.
        out_losses: File to store recurrent losses.
        out_plots: Directory to store plots per chromosome. Potential issues may arise due to timestamped outputs.
        fdr (optional): False discovery rate. Defaults to 0.25 if not provided.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/rubic",
        inputs=dict(seg=seg, markers=markers, genefile=genefile),
        outputs=dict(out_gains=out_gains, out_losses=out_losses, out_plots=out_plots),
        params={"fdr": fdr} if fdr is not None else {},
         
    )


@collect_tool()
def rubic(
    *,
    seg: str,
    markers: str,
    genefile: Optional[str] = None,
    out_gains: str,
    out_losses: str,
    out_plots: str,
    fdr: Optional[float] = 0.25,
     
) -> subprocess.CompletedProcess:
    """
    RUBIC detects recurrent copy number alterations using copy number breaks.

    Args:
        seg: Segmentation file containing copy number profiles from multiple tumor samples.
        markers: File with marker positions.
        genefile (optional): File path to use custom gene file. If not specified, the default file is used.
        out_gains: File to store recurrent gains.
        out_losses: File to store recurrent losses.
        out_plots: Directory to store plots per chromosome. Potential issues may arise due to timestamped outputs.
        fdr (optional): False discovery rate. Defaults to 0.25 if not provided.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_rubic(
        seg=seg,
        markers=markers,
        genefile=genefile,
        out_gains=out_gains,
        out_losses=out_losses,
        out_plots=out_plots,
        fdr=fdr,
         
    )
