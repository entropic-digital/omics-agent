from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_query(
    *,
    bgzip_file: str,
    tabix_index_file: str,
    region: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Query a file using tabix.

    Args:
        bgzip_file: Path to the bgzip-compressed file (e.g., BED.gz, GFF.gz, or VCF.gz).
        tabix_index_file: Path to the tabix index file corresponding to the bgzip file.
        region: Genomic region of interest to retrieve (e.g., "chr1:1-1000").
        extra (optional): Additional arguments to pass to the tabix tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/tabix/query",
        inputs=dict(
            bgzip_file=bgzip_file,
            tabix_index_file=tabix_index_file,
        ),
        params={
            "region": region,
            **({"extra": extra} if extra else {}),
        },
         
    )


@collect_tool()
def tabix_query(
    *,
    bgzip_file: str,
    tabix_index_file: str,
    region: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Query a file using tabix.

    Args:
        bgzip_file: Path to the bgzip-compressed file (e.g., BED.gz, GFF.gz, or VCF.gz).
        tabix_index_file: Path to the tabix index file corresponding to the bgzip file.
        region: Genomic region of interest to retrieve (e.g., "chr1:1-1000").
        extra (optional): Additional arguments to pass to the tabix tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_query(
        bgzip_file=bgzip_file,
        tabix_index_file=tabix_index_file,
        region=region,
        extra=extra,
         
    )
