from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_seqtk(
    *,
    fastx: str,
    output: str,
    n: Optional[int] = None,
    extra: Optional[str] = None,
    compress_lvl: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Runs seqtk, a toolkit for processing sequences in FASTA/Q formats.

    Args:
        fastx: Path to the input FASTA/Q file(s) (can be gzip compressed).
        output: Path to the output FASTN file(s) (can be gzip compressed).
        n (optional): Number of reads after subsampling (for `sample`).
        extra (optional): Additional program options (e.g., `-s` for `sample` or `-b/-e` for `trimfq`).
        compress_lvl (optional): Compression level (refer to `gzip` manual for details).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "extra": extra,
        "n": n,
        "compress_lvl": compress_lvl,
    }
    # Filter out None values from params
    params = {k: v for k, v in params.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:tools/seqtk",
        inputs={"fastx": fastx},
        outputs={"output": output},
        params=params,
         
    )


@collect_tool()
def seqtk(
    *,
    fastx: str,
    output: str,
    n: Optional[int] = None,
    extra: Optional[str] = None,
    compress_lvl: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Runs seqtk, a toolkit for processing sequences in FASTA/Q formats.

    Args:
        fastx: Path to the input FASTA/Q file(s) (can be gzip compressed).
        output: Path to the output FASTN file(s) (can be gzip compressed).
        n (optional): Number of reads after subsampling (for `sample`).
        extra (optional): Additional program options (e.g., `-s` for `sample` or `-b/-e` for `trimfq`).
        compress_lvl (optional): Compression level (refer to `gzip` manual for details).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_seqtk(
        fastx=fastx,
        output=output,
        n=n,
        extra=extra,
        compress_lvl=compress_lvl,
         
    )
