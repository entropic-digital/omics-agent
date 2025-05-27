from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_download(
    *,
    manifest_file: str,
    token_file: str,
    client_bin: str = "gdc-client",
    download_dir: Optional[str] = None,
    log_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GDC Data Transfer Tool data download.

    This function uses the GDC Data Transfer Tool (gdc-client) to download data files
    from the GDC repository based on the provided manifest file.

    Args:
        manifest_file: Path to the GDC manifest file specifying the data to download.
        token_file: Path to an authentication token file for accessing the GDC data.
        client_bin (optional): Path to the gdc-client binary (default is "gdc-client").
        download_dir (optional): Directory to store the downloaded files.
        log_file (optional): Path to a log file to capture the gdc-client output.
  
    Returns:
        subprocess.CompletedProcess: Instance containing information about
        the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gdc-client/download",
        inputs=dict(manifest_file=manifest_file, token_file=token_file),
        params={
            "client_bin": client_bin,
            "download_dir": download_dir,
            "log_file": log_file,
        },
         
    )


@collect_tool()
def download(
    *,
    manifest_file: str,
    token_file: str,
    client_bin: str = "gdc-client",
    download_dir: Optional[str] = None,
    log_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GDC Data Transfer Tool data download.

    This function is a decorated entry point that invokes the GDC Data Transfer Tool
    to download data files from GDC based on a manifest file. It uses Snakemake as
    the execution backend.

    Args:
        manifest_file: Path to the GDC manifest file specifying the data to download.
        token_file: Path to an authentication token file for accessing the GDC data.
        client_bin (optional): Path to the gdc-client binary (default is "gdc-client").
        download_dir (optional): Directory to store the downloaded files.
        log_file (optional): Path to a log file to capture the gdc-client output.
  
    Returns:
        subprocess.CompletedProcess: Instance containing information about
        the completed Snakemake process.
    """
    return run_download(
        manifest_file=manifest_file,
        token_file=token_file,
        client_bin=client_bin,
        download_dir=download_dir,
        log_file=log_file,
         
    )
