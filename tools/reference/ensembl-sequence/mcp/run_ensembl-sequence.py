from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_ensembl_sequence(
    *,
    fasta_file: str,
    url: Optional[str] = "ftp://ftp.ensembl.org/pub",
     
) -> subprocess.CompletedProcess:
    """
    Download sequences (e.g., genome) from ENSEMBL FTP servers and store them in a single .fasta file.

    Args:
        fasta_file: Path to the output .fasta file where the downloaded sequences will be stored.
        url (optional): URL from where to download cache data. Defaults to ``ftp://ftp.ensembl.org/pub``.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/reference/ensembl-sequence",
        outputs={"fasta_file": fasta_file},
        params={"url": url} if url else {},
         
    )


@collect_tool()
def ensembl_sequence(
    *,
    fasta_file: str,
    url: Optional[str] = "ftp://ftp.ensembl.org/pub",
     
) -> subprocess.CompletedProcess:
    """
    Download sequences (e.g., genome) from ENSEMBL FTP servers and store them in a single .fasta file.

    Args:
        fasta_file: Path to the output .fasta file where the downloaded sequences will be stored.
        url (optional): URL from where to download cache data. Defaults to ``ftp://ftp.ensembl.org/pub``.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_ensembl_sequence(fasta_file=fasta_file, url=url,      )
