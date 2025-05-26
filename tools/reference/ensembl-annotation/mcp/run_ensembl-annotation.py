from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_ensembl_annotation(
    *,
    url: Optional[str] = "ftp://ftp.ensembl.org/pub",
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Download annotation of genomic sites (e.g. transcripts) from ENSEMBL FTP servers and store them in a single .gtf or .gff3 file.

    Args:
        url (optional): URL from where to download cache data. Defaults to "ftp://ftp.ensembl.org/pub".
        output_file: Output file path where the annotation (GTF or GFF3) will be stored.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/reference/ensembl-annotation",
        outputs=dict(output_file=output_file),
        params={"url": url} if url else {},
         
    )


@collect_tool()
def ensembl_annotation(
    *,
    url: Optional[str] = "ftp://ftp.ensembl.org/pub",
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Download annotation of genomic sites (e.g. transcripts) from ENSEMBL FTP servers and store them in a single .gtf or .gff3 file.

    Args:
        url (optional): URL from where to download cache data. Defaults to "ftp://ftp.ensembl.org/pub".
        output_file: Output file path where the annotation (GTF or GFF3) will be stored.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_ensembl_annotation(url=url, output_file=output_file,      )
