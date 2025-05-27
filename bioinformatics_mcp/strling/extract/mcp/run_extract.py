from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_extract(
    *,
    input_bam: str,
    reference_fasta: str,
    region_bed: Optional[str] = None,
    output_bin: str,
     
) -> subprocess.CompletedProcess:
    """
    STRling extract tool.

    STRling (pronounced “sterling”) is a method to detect large short tandem repeat (STR)
    expansions from short-read sequencing data. The `extract` method retrieves informative
    read pairs to a binary format for a single sample.

    Args:
        input_bam: The path to the input BAM file.
        reference_fasta: The path to the reference FASTA file.
        region_bed (optional): The path to a BED file defining regions of interest.
        output_bin: The path to the output binary file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/strling/extract",
        inputs=dict(
            input_bam=input_bam,
            reference_fasta=reference_fasta,
            region_bed=region_bed,
        ),
        outputs=dict(output_bin=output_bin),
        params={},
         
    )


@collect_tool()
def extract(
    *,
    input_bam: str,
    reference_fasta: str,
    region_bed: Optional[str] = None,
    output_bin: str,
     
) -> subprocess.CompletedProcess:
    """
    STRling extract tool.

    STRling (pronounced “sterling”) is a method to detect large short tandem repeat (STR)
    expansions from short-read sequencing data. The `extract` method retrieves informative
    read pairs to a binary format for a single sample.

    Args:
        input_bam: The path to the input BAM file.
        reference_fasta: The path to the reference FASTA file.
        region_bed (optional): The path to a BED file defining regions of interest.
        output_bin: The path to the output binary file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_extract(
        input_bam=input_bam,
        reference_fasta=reference_fasta,
        region_bed=region_bed,
        output_bin=output_bin,
         
    )
