from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    prg_file: str,
    index: str,
    kmer_prgs: str,
    options: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index population reference graph (PRG) sequences.

    Args:
        prg_file: Path to the PRG file to index (made by `make_prg`).
        index: Path to the output pandora index file.
        kmer_prgs: Directory for the index kmer PRGs in GFA format.
        options (optional): Any additional options for the tool, excluding threads.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/pandora/index",
        inputs=dict(prg_file=prg_file),
        outputs=dict(index=index, kmer_prgs=kmer_prgs),
        params={"options": options} if options else {},
         
    )


@collect_tool()
def index(
    *,
    prg_file: str,
    index: str,
    kmer_prgs: str,
    options: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index population reference graph (PRG) sequences.

    Args:
        prg_file: Path to the PRG file to index (made by `make_prg`).
        index: Path to the output pandora index file.
        kmer_prgs: Directory for the index kmer PRGs in GFA format.
        options (optional): Any additional options for the tool, excluding threads.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        prg_file=prg_file,
        index=index,
        kmer_prgs=kmer_prgs,
        options=options,
         
    )
