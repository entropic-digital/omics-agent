from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_cache(
    *,
    url: Optional[str] = "ftp://ftp.ensembl.org/pub",
    species: str,
    build: str,
    release: str,
    indexed: bool,
    output_directory: str,
     
) -> subprocess.CompletedProcess:
    """
    Download VEP cache for a given species, build, and release.

    Args:
        url (optional): URL from where to download cache data. Defaults to `ftp://ftp.ensembl.org/pub`.
        species: Species for which to download the cache data.
        build: Build version for which to download the cache data.
        release: Release version for which to download the cache data.
        indexed: Whether to download an already indexed cache.
        output_directory: Directory to store the VEP cache.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/vep/cache",
        inputs={},
        params={
            "url": url,
            "species": species,
            "build": build,
            "release": release,
            "indexed": indexed,
        },
        outputs={"output_directory": output_directory},
         
    )


@collect_tool()
def cache(
    *,
    url: Optional[str] = "ftp://ftp.ensembl.org/pub",
    species: str,
    build: str,
    release: str,
    indexed: bool,
    output_directory: str,
     
) -> subprocess.CompletedProcess:
    """
    Download VEP cache for a given species, build, and release.

    Args:
        url (optional): URL from where to download cache data. Defaults to `ftp://ftp.ensembl.org/pub`.
        species: Species for which to download the cache data.
        build: Build version for which to download the cache data.
        release: Release version for which to download the cache data.
        indexed: Whether to download an already indexed cache.
        output_directory: Directory to store the VEP cache.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_cache(
        url=url,
        species=species,
        build=build,
        release=release,
        indexed=indexed,
        output_directory=output_directory,
         
    )
