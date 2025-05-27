from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_mtnucratio(
    *,
    bam_file: str,
    chrom: str,
    json_output: Optional[str] = None,
    txt: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the MTNucRatioCalculator tool.

    Args:
        bam_file: Path to the input BAM file.
        chrom: Name of the mitochondrial chromosome.
        json_output (optional): Optional path to output JSON-formatted results.
        txt (optional): Optional path to output text-formatted results.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/mtnucratio",
        inputs=dict(bam_file=bam_file),
        outputs={"json": json_output, "txt": txt},
        params={"chrom": chrom},
         
    )


@collect_tool()
def mtnucratio(
    *,
    bam_file: str,
    chrom: str,
    json_output: Optional[str] = None,
    txt: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the MTNucRatioCalculator tool.

    Args:
        bam_file: Path to the input BAM file.
        chrom: Name of the mitochondrial chromosome.
        json_output (optional): Optional path to output JSON-formatted results.
        txt (optional): Optional path to output text-formatted results.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mtnucratio(
        bam_file=bam_file,
        chrom=chrom,
        json_output=json_output,
        txt=txt,
         
    )
