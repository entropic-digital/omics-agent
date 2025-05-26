from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_blastx(
    *,
    fname_fastq: str,
    fname_db: str,
    fname: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    DIAMOND BLASTX sequence aligner.

    Args:
        fname_fastq: Path to the Fastq query file.
        fname_db: Path to the DIAMOND database.
        fname: Path to the output file with query results.
        extra (optional): Additional parameters for DIAMOND, excluding `--threads`, `--db`, `--query`, and `--out`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/diamond/blastx",
        inputs=dict(query=fname_fastq, db=fname_db),
        outputs=dict(out=fname),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def blastx(
    *,
    fname_fastq: str,
    fname_db: str,
    fname: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    DIAMOND BLASTX sequence aligner.

    Args:
        fname_fastq: Path to the Fastq query file.
        fname_db: Path to the DIAMOND database.
        fname: Path to the output file with query results.
        extra (optional): Additional parameters for DIAMOND, excluding `--threads`, `--db`, `--query`, and `--out`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_blastx(
        fname_fastq=fname_fastq,
        fname_db=fname_db,
        fname=fname,
        extra=extra,
         
    )
