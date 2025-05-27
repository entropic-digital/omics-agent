from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_multibigwigsummary(
    *,
    bw: List[str],
    npz: str,
    counts: str,
    blacklist: Optional[str] = None,
    bed: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Compute the average scores for each of the files in every genomic region using multiBigwigSummary.

    Args:
        bw: Path to a bigwig file, or a list of bigwig files.
        npz: Path to the compressed matrix file.
        counts: Path to average scores per region for each bigwig.
        blacklist (optional): Path to a BED file covering regions to exclude.
        bed (optional): Path to a bed file to limit the analysis of regions. This triggers the subcommand 'BED-file'.
                        If left empty, the 'bins' subcommand is triggered.
        extra (optional): Additional arguments for `multiBigwigSummary` besides IO and processor.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "bw": bw,
        "blacklist": blacklist,
        "bed": bed,
    }
    outputs = {
        "npz": npz,
        "counts": counts,
    }
    params = {
        "extra": extra,
    }
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/deeptools/multibigwigsummary",
        inputs={k: v for k, v in inputs.items() if v is not None},
        outputs={k: v for k, v in outputs.items() if v is not None},
        params={k: v for k, v in params.items() if v is not None},
         
    )


@collect_tool()
def multibigwigsummary(
    *,
    bw: List[str],
    npz: str,
    counts: str,
    blacklist: Optional[str] = None,
    bed: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Compute the average scores for each of the files in every genomic region using multiBigwigSummary.

    Args:
        bw: Path to a bigwig file, or a list of bigwig files.
        npz: Path to the compressed matrix file.
        counts: Path to average scores per region for each bigwig.
        blacklist (optional): Path to a BED file covering regions to exclude.
        bed (optional): Path to a bed file to limit the analysis of regions. This triggers the subcommand 'BED-file'.
                        If left empty, the 'bins' subcommand is triggered.
        extra (optional): Additional arguments for `multiBigwigSummary` besides IO and processor.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_multibigwigsummary(
        bw=bw,
        npz=npz,
        counts=counts,
        blacklist=blacklist,
        bed=bed,
        extra=extra,
         
    )
