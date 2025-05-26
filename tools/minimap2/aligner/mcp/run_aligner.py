from typing import Optional, List
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_aligner(
    *,
    input_files: List[str],
    reference_genome: str,
    output_file: str,
    extra: Optional[str] = None,
    sort: Optional[str] = "none",
    sort_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    A versatile pairwise aligner for genomic and spliced nucleotide sequences.

    Args:
        input_files: List of FASTQ file(s) or unaligned BAM file to be aligned.
        reference_genome: Path to the reference genome file.
        output_file: Path to the output SAM/BAM/CRAM file.
        extra: Additional arguments for minimap2 (optional).
        sort: Sorting mode, can be 'none', 'queryname', or 'coordinate' (default: 'none').
        sort_extra: Extra arguments for samtools/picard during sorting (optional).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/minimap2/aligner",
        inputs={"input_files": input_files, "reference_genome": reference_genome},
        outputs={"output_file": output_file},
        params={
            "extra": extra,
            "sort": sort,
            "sort_extra": sort_extra,
        },
         
    )


@collect_tool()
def aligner(
    *,
    input_files: List[str],
    reference_genome: str,
    output_file: str,
    extra: Optional[str] = None,
    sort: Optional[str] = "none",
    sort_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    A versatile pairwise aligner for genomic and spliced nucleotide sequences.

    Args:
        input_files: List of FASTQ file(s) or unaligned BAM file to be aligned.
        reference_genome: Path to the reference genome file.
        output_file: Path to the output SAM/BAM/CRAM file.
        extra: Additional arguments for minimap2 (optional).
        sort: Sorting mode, can be 'none', 'queryname', or 'coordinate' (default: 'none').
        sort_extra: Extra arguments for samtools/picard during sorting (optional).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_aligner(
        input_files=input_files,
        reference_genome=reference_genome,
        output_file=output_file,
        extra=extra,
        sort=sort,
        sort_extra=sort_extra,
         
    )
