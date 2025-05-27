from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_inner_distance(
    *,
    aln: str,
    refgene: str,
    reads_inner_distance: Optional[str] = None,
    pdf: Optional[str] = None,
    plot_r: Optional[str] = None,
    freq: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate inner distance between read pairs.

    Args:
        aln: Path to SAM/BAM input file.
        refgene: Path to refgene model file.
        reads_inner_distance (optional): Path to per-read inner distance table.
        pdf (optional): Path to PDF graph output.
        plot_r (optional): Path to R script output.
        freq (optional): Path to inner distance frequency output.
        extra (optional): Additional parameters for 'inner_distance.py', excluding '-i', '-r', and '-o'.
  
    Returns:
        A subprocess.CompletedProcess instance containing information about the completed Snakemake process.
    """
    outputs = {
        "reads_inner_distance": reads_inner_distance,
        "pdf": pdf,
        "plot_r": plot_r,
        "freq": freq,
    }

    outputs = {key: value for key, value in outputs.items() if value}

    params = {}
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/rseqc/inner_distance",
        inputs=dict(aln=aln, refgene=refgene),
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def inner_distance(
    *,
    aln: str,
    refgene: str,
    reads_inner_distance: Optional[str] = None,
    pdf: Optional[str] = None,
    plot_r: Optional[str] = None,
    freq: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate inner distance between read pairs.

    Args:
        aln: Path to SAM/BAM input file.
        refgene: Path to refgene model file.
        reads_inner_distance (optional): Path to per-read inner distance table.
        pdf (optional): Path to PDF graph output.
        plot_r (optional): Path to R script output.
        freq (optional): Path to inner distance frequency output.
        extra (optional): Additional parameters for 'inner_distance.py', excluding '-i', '-r', and '-o'.
  
    Returns:
        A subprocess.CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_inner_distance(
        aln=aln,
        refgene=refgene,
        reads_inner_distance=reads_inner_distance,
        pdf=pdf,
        plot_r=plot_r,
        freq=freq,
        extra=extra,
         
    )
