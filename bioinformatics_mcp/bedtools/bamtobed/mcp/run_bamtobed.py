from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_bamtobed(
    *,
    input_bam: str,
    output_bed: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Conversion utility that converts sequence alignments in BAM format into BED, BED12, and/or BEDPE records.

    Args:
        input_bam: BAM file, this must be the first file in the input file list.
        output_bed: BED file, this must be the first file in the output file list.
        extra (optional): Additional program arguments (except `-i`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bedtools/bamtobed",
        inputs={"input_bam": input_bam},
        outputs={"output_bed": output_bed},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def bamtobed(
    *,
    input_bam: str,
    output_bed: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Conversion utility that converts sequence alignments in BAM format into BED, BED12, and/or BEDPE records.

    Args:
        input_bam: BAM file, this must be the first file in the input file list.
        output_bed: BED file, this must be the first file in the output file list.
        extra (optional): Additional program arguments (except `-i`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bamtobed(
        input_bam=input_bam, output_bed=output_bed, extra=extra,      
    )
