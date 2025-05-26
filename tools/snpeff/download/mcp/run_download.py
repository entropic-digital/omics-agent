from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_download(
    *,
    species: str,
    version: Optional[str] = None,
    out_db_dir: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Download `snpeff <https://pcingola.github.io/SnpEff/se_introduction/>`_ DB for a given species.

    Args:
        species: Name of the species for which to download the SnpEff database.
        version (optional): Version of the SnpEff database to download.
        out_db_dir (optional): Directory to store the downloaded database files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/snpeff/download",
        inputs=dict(species=species),
        params={"version": version, "out_db_dir": out_db_dir},
         
    )


@collect_tool()
def download(
    *,
    species: str,
    version: Optional[str] = None,
    out_db_dir: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Download `snpeff <https://pcingola.github.io/SnpEff/se_introduction/>`_ DB for a given species.

    Args:
        species: Name of the species for which to download the SnpEff database.
        version (optional): Version of the SnpEff database to download.
        out_db_dir (optional): Directory to store the downloaded database files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_download(
        species=species, version=version, out_db_dir=out_db_dir,      
    )
