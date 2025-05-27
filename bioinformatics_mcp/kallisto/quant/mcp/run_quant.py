from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_quant(
    *,
    fastq: List[str],
    index: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Pseudoalign reads and quantify transcripts using kallisto.

    Args:
        fastq: List of FASTQ file(s).
        index: Indexed file for kallisto.
        output: Directory to store the results.
        extra (optional): Additional parameters for kallisto.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/kallisto/quant",
        inputs=dict(fastq=fastq, index=index),
        outputs=dict(output=output),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def quant(
    *,
    fastq: List[str],
    index: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Pseudoalign reads and quantify transcripts using kallisto.

    Args:
        fastq: List of FASTQ file(s).
        index: Indexed file for kallisto.
        output: Directory to store the results.
        extra (optional): Additional parameters for kallisto.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_quant(
        fastq=fastq,
        index=index,
        output=output,
        extra=extra,
         
    )
