from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    sequences: str,
    decoys: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index a transcriptome assembly with salmon.

    Args:
        sequences: Path to sequences to index with Salmon. This can be transcriptome sequences or gentrome.
        decoys (optional): Optional path to decoy sequences names, in case the above `sequences` was a gentrome.
        extra (optional): Optional parameters besides `--tmpdir`, `--threads`, and IO.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/salmon/index",
        inputs={"sequences": sequences, "decoys": decoys}
        if decoys
        else {"sequences": sequences},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def salmon_index(
    *,
    sequences: str,
    decoys: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index a transcriptome assembly with salmon.

    Args:
        sequences: Path to sequences to index with Salmon. This can be transcriptome sequences or gentrome.
        decoys (optional): Optional path to decoy sequences names, in case the above `sequences` was a gentrome.
        extra (optional): Optional parameters besides `--tmpdir`, `--threads`, and IO.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        sequences=sequences,
        decoys=decoys,
        extra=extra,
         
    )
