from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_depth(
    *,
    input_bam: str,
    output_file: str,
    regions_file: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Compute the read depth at each position or region using samtools.

    Args:
        input_bam: BAM file containing the mapped reads.
        output_file: Path to the output file for depth data.
        regions_file (optional): File containing regions of interest.
        extra (optional): Additional arguments to pass to samtools depth, excluding `-@/--threads` and `-o`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/samtools/depth",
        inputs={"input_bam": input_bam},
        outputs={"output_file": output_file},
        params={"regions_file": regions_file, "extra": extra},
         
    )


@collect_tool()
def depth(
    *,
    input_bam: str,
    output_file: str,
    regions_file: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Compute the read depth at each position or region using samtools.

    Args:
        input_bam: BAM file containing the mapped reads.
        output_file: Path to the output file for depth data.
        regions_file (optional): File containing regions of interest.
        extra (optional): Additional arguments to pass to samtools depth, excluding `-@/--threads` and `-o`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_depth(
        input_bam=input_bam,
        output_file=output_file,
        regions_file=regions_file,
        extra=extra,
         
    )
