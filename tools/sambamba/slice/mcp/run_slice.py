from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_slice(
    *,
    bam_file: str,
    output_bam: str,
    region: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Fast tool for copying a slice of a BAM file.

    Args:
        bam_file: Path to the coordinate-sorted and indexed BAM file.
        output_bam: Path to the output BAM file with the specified region.
        region (optional): Genomic region to extract (e.g., "chr1:1000-2000").
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/sambamba/slice",
        inputs={"bam_file": bam_file},
        outputs={"output_bam": output_bam},
        params={"region": region} if region else {},
         
    )


@collect_tool()
def slice(
    *,
    bam_file: str,
    output_bam: str,
    region: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Fast tool for copying a slice of a BAM file.

    Args:
        bam_file: Path to the coordinate-sorted and indexed BAM file.
        output_bam: Path to the output BAM file with the specified region.
        region (optional): Genomic region to extract (e.g., "chr1:1000-2000").
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_slice(bam_file=bam_file, output_bam=output_bam, region=region,      )
