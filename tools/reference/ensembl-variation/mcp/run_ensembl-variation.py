from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_ensembl_variation(
    *,
    url: Optional[str] = "ftp://ftp.ensembl.org/pub",
    output_vcf: str,
     
) -> subprocess.CompletedProcess:
    """
    Download known genomic variants from ENSEMBL FTP servers, and store them in a single .vcf.gz file.

    Args:
        url (optional): URL from where to download cache data. Defaults to ``ftp://ftp.ensembl.org/pub``.
        output_vcf: Path to the output VCF file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/reference/ensembl-variation",
        outputs={"output_vcf": output_vcf},
        params={"url": url} if url else {},
         
    )


@collect_tool()
def ensembl_variation(
    *,
    url: Optional[str] = "ftp://ftp.ensembl.org/pub",
    output_vcf: str,
     
) -> subprocess.CompletedProcess:
    """
    Download known genomic variants from ENSEMBL FTP servers, and store them in a single .vcf.gz file.

    Args:
        url (optional): URL from where to download cache data. Defaults to ``ftp://ftp.ensembl.org/pub``.
        output_vcf: Path to the output VCF file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_ensembl_variation(url=url, output_vcf=output_vcf,      )
