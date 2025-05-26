from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_makesnvpattern(
    *,
    bed: str,
    fasta: str,
    index: List[str],
    output_fasta: str,
    output_pattern_uncompressed: str,
    output_pattern: str,
     
) -> subprocess.CompletedProcess:
    """
    Generate SNP pattern file.

    Args:
        bed: Path to bed intervals.
        fasta: Path to fasta genome sequence.
        index: List of paths to `bowtie` index files.
        output_fasta: Path to fasta-formatted regions extracted from bed intervals.
        output_pattern_uncompressed: Path to uncompressed patterns, used for internal pattern checks only.
        output_pattern: Path to compressed (binary) pattern file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/ngscheckmate/makesnvpattern",
        inputs=dict(bed=bed, fasta=fasta, index=index),
        outputs=dict(
            fasta=output_fasta,
            pattern_uncompressed=output_pattern_uncompressed,
            pattern=output_pattern,
        ),
         
    )


@collect_tool()
def makesnvpattern(
    *,
    bed: str,
    fasta: str,
    index: List[str],
    output_fasta: str,
    output_pattern_uncompressed: str,
    output_pattern: str,
     
) -> subprocess.CompletedProcess:
    """
    Generate SNP pattern file.

    Args:
        bed: Path to bed intervals.
        fasta: Path to fasta genome sequence.
        index: List of paths to `bowtie` index files.
        output_fasta: Path to fasta-formatted regions extracted from bed intervals.
        output_pattern_uncompressed: Path to uncompressed patterns, used for internal pattern checks only.
        output_pattern: Path to compressed (binary) pattern file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_makesnvpattern(
        bed=bed,
        fasta=fasta,
        index=index,
        output_fasta=output_fasta,
        output_pattern_uncompressed=output_pattern_uncompressed,
        output_pattern=output_pattern,
         
    )
