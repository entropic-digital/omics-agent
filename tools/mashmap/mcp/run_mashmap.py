from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_mashmap(
    *,
    ref: str,
    query: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Compute local alignment boundaries between long DNA sequences with MashMap.

    Args:
        ref: Path to the reference file. Can be a FASTA file or a text file containing multiple paths.
        query: Path to the query file. Can be a FASTQ file or a text file containing multiple paths.
        output: Path to the alignment output file.
        extra (optional): Additional parameters to pass to MashMap.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/mashmap",
        inputs=dict(ref=ref, query=query),
        outputs=dict(output=output),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def mashmap(
    *,
    ref: str,
    query: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Compute local alignment boundaries between long DNA sequences with MashMap.

    Args:
        ref: Path to the reference file. Can be a FASTA file or a text file containing multiple paths.
        query: Path to the query file. Can be a FASTQ file or a text file containing multiple paths.
        output: Path to the alignment output file.
        extra (optional): Additional parameters to pass to MashMap.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mashmap(ref=ref, query=query, output=output, extra=extra,      )
