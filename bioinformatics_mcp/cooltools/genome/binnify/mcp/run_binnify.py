from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_binnify(
    *,
    chromsizes: str,
    output: str,
    binsize: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Split chromosomes into equal-sized bins.

    Args:
        chromsizes: Path to the chromsizes file.
        output: Path to the output .bed file with bin coordinates. Can contain a {binsize} wildcard.
        binsize (optional): Size of bins in base pairs, if not specified as a wildcard in the output.
        extra (optional): Any additional arguments to pass.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/cooltools/genome/binnify",
        inputs=dict(chromsizes=chromsizes),
        outputs=dict(output=output),
        params={"binsize": binsize, "extra": extra},
         
    )


@collect_tool()
def binnify(
    *,
    chromsizes: str,
    output: str,
    binsize: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Split chromosomes into equal-sized bins.

    Args:
        chromsizes: Path to the chromsizes file.
        output: Path to the output .bed file with bin coordinates. Can contain a {binsize} wildcard.
        binsize (optional): Size of bins in base pairs, if not specified as a wildcard in the output.
        extra (optional): Any additional arguments to pass.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_binnify(
        chromsizes=chromsizes,
        output=output,
        binsize=binsize,
        extra=extra,
         
    )
