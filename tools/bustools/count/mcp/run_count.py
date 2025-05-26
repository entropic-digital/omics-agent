from typing import Optional, List, Union
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_count(
    *,
    bus: Union[str, List[str]],
    genemap: str,
    txnames: str,
    ecmap: str,
    extra: Optional[str] = None,
    output: str,
     
) -> subprocess.CompletedProcess:
    """
    Convert BUS files into a barcode-feature matrix.

    Args:
        bus: Single bus-file, or a list of bus-files.
        genemap: Transcript to gene mapping file.
        txnames: List of transcripts file.
        ecmap: Equivalence classes file for transcripts.
        extra: Optional additional parameters for bustools count, excluding '--output', '--ecmap', and '--genemap'.
        output: The output file path for barcodes, equivalence classes, and count matrix.
  
    Returns:
        CompletedProcess: Contains information about the completed Snakemake process.
    """
    params = {
        "genemap": genemap,
        "txnames": txnames,
        "ecmap": ecmap,
        "extra": extra,
        "output": output,
    }

    # Automatically handle '--hist' and '--genemap' flags based on output file extensions
    if output.endswith(".hist.txt"):
        params["hist"] = True
    if output.endswith(".genes.txt"):
        params["genemap_flag"] = True

    return run_snake_wrapper(
        wrapper="file:tools/bustools/count",
        inputs={"bus": bus},
        params=params,
         
    )


@collect_tool()
def count(
    *,
    bus: Union[str, List[str]],
    genemap: str,
    txnames: str,
    ecmap: str,
    extra: Optional[str] = None,
    output: str,
     
) -> subprocess.CompletedProcess:
    """
    Convert BUS files into a barcode-feature matrix.

    Args:
        bus: Single bus-file, or a list of bus-files.
        genemap: Transcript to gene mapping file.
        txnames: List of transcripts file.
        ecmap: Equivalence classes file for transcripts.
        extra: Optional additional parameters for bustools count, excluding '--output', '--ecmap', and '--genemap'.
        output: The output file path for barcodes, equivalence classes, and count matrix.
  
    Returns:
        CompletedProcess: Contains information about the completed Snakemake process.
    """
    return run_count(
        bus=bus,
        genemap=genemap,
        txnames=txnames,
        ecmap=ecmap,
        extra=extra,
        output=output,
         
    )
