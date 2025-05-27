from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_bedGraphToBigWig(
    *,
    bedGraph: str,
    chromsizes: str,
    output: str,
     
) -> subprocess.CompletedProcess:
    """
    Convert a *.bedGraph file to a *.bw file using UCSC bedGraphToBigWig.

    Args:
        bedGraph: Path to the *.bedGraph input file.
        chromsizes: Path to the chrom sizes file, could be generated using twoBitInfo or downloaded from UCSC.
        output: Path to the resulting *.bw output file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/ucsc/bedGraphToBigWig",
        inputs=dict(bedGraph=bedGraph, chromsizes=chromsizes),
        outputs=dict(output=output),
         
    )


@collect_tool()
def bedGraphToBigWig(
    *,
    bedGraph: str,
    chromsizes: str,
    output: str,
     
) -> subprocess.CompletedProcess:
    """
    Convert a *.bedGraph file to a *.bw file using UCSC bedGraphToBigWig.

    Args:
        bedGraph: Path to the *.bedGraph input file.
        chromsizes: Path to the chrom sizes file, could be generated using twoBitInfo or downloaded from UCSC.
        output: Path to the resulting *.bw output file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bedGraphToBigWig(
        bedGraph=bedGraph,
        chromsizes=chromsizes,
        output=output,
         
    )
