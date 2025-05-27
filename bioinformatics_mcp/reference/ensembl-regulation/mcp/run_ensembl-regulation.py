from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_ensembl_regulation(
    *,
    url: Optional[str] = "ftp://ftp.ensembl.org/pub",
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Download annotation of regulatory features (e.g. promotors) for genomes from ENSEMBL FTP servers
    and store them in a single .gff or .gff3 file.

    Args:
        url (optional): Base URL from where to download cache data. Defaults to 'ftp://ftp.ensembl.org/pub'.
        output_file: Ensembl GFF annotation file for regulatory features.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/reference/ensembl-regulation",
        outputs={"output_file": output_file},
        params={"url": url},
         
    )


@collect_tool()
def ensembl_regulation(
    *,
    url: Optional[str] = "ftp://ftp.ensembl.org/pub",
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Download annotation of regulatory features (e.g. promotors) for genomes from ENSEMBL FTP servers
    and store them in a single .gff or .gff3 file.

    Args:
        url (optional): Base URL from where to download cache data. Defaults to 'ftp://ftp.ensembl.org/pub'.
        output_file: Ensembl GFF annotation file for regulatory features.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_ensembl_regulation(url=url, output_file=output_file,      )
