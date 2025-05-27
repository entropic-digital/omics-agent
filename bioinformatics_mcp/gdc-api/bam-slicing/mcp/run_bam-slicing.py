from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_bam_slicing(
    *,
    bam_uuid: str,
    gdc_token: str,
    output: str,
    region: Optional[str] = None,
    gencode: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GDC API-based data download of BAM slices.

    Downloads regions or gene-specific slices from BAM files hosted by the GDC API.

    Args:
        bam_uuid: UUID of the BAM file to be downloaded.
        gdc_token: Path to the GDC access token file.
        output: Path to the output file where the BAM slice will be saved.
        region (optional): Specifies regions to slice (e.g., 'chr20:3000-4000').
        gencode (optional): Specifies gene name(s) to slice (e.g., 'BRCA2').
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gdc-api/bam-slicing",
        inputs=dict(bam_uuid=bam_uuid),
        outputs=dict(output=output),
        params={
            "gdc_token": gdc_token,
            "region": region,
            "gencode": gencode,
        },
         
    )


@collect_tool()
def bam_slicing(
    *,
    bam_uuid: str,
    gdc_token: str,
    output: str,
    region: Optional[str] = None,
    gencode: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GDC API-based data download of BAM slices.

    Downloads regions or gene-specific slices from BAM files hosted by the GDC API.

    Args:
        bam_uuid: UUID of the BAM file to be downloaded.
        gdc_token: Path to the GDC access token file.
        output: Path to the output file where the BAM slice will be saved.
        region (optional): Specifies regions to slice (e.g., 'chr20:3000-4000').
        gencode (optional): Specifies gene name(s) to slice (e.g., 'BRCA2').
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bam_slicing(
        bam_uuid=bam_uuid,
        gdc_token=gdc_token,
        output=output,
        region=region,
        gencode=gencode,
         
    )
