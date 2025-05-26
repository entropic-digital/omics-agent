from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_quality_profile(
    *,
    fastq_file: str,
    output_png: str,
     
) -> subprocess.CompletedProcess:
    """
    DADA2 Quality Profiles.

    This tool generates a quality profile plot for sequencing reads using the
    `plotQualityProfile` function from the DADA2 R package.

    Args:
        fastq_file: Input FASTQ file (can be compressed) without primer sequences.
        output_png: Output PNG file for the quality plot.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/dada2/quality-profile",
        inputs=dict(fastq_file=fastq_file),
        outputs=dict(output_png=output_png),
         
    )


@collect_tool()
def quality_profile(
    *,
    fastq_file: str,
    output_png: str,
     
) -> subprocess.CompletedProcess:
    """
    DADA2 Quality Profiles.

    This tool generates a quality profile plot for sequencing reads using the
    `plotQualityProfile` function from the DADA2 R package.

    Args:
        fastq_file: Input FASTQ file (can be compressed) without primer sequences.
        output_png: Output PNG file for the quality plot.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_quality_profile(fastq_file=fastq_file, output_png=output_png,      )
