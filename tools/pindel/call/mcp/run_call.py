from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_call(
    *,
    reference: str,
    bam_files: list[str],
    bam_config: str,
    include_bed: Optional[str] = None,
    exclude_bed: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call variants with pindel.

    Args:
        reference: Path to the reference genome fasta file.
        bam_files: List of paths to one or more BAM files.
        bam_config: Path to BAM configuration file (see pindel documentation).
        include_bed (optional): Path to a BED file specifying regions to include.
        exclude_bed (optional): Path to a BED file specifying regions to exclude.
            Note: Include and exclude BED files are incompatible with each other.
            Either provide one or neither.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    if include_bed and exclude_bed:
        raise ValueError(
            "Include and exclude BED files are incompatible. Provide only one or neither."
        )

    input_dict = {
        "reference": reference,
        "bam_files": bam_files,
        "bam_config": bam_config,
    }

    if include_bed:
        input_dict["include_bed"] = include_bed
    if exclude_bed:
        input_dict["exclude_bed"] = exclude_bed

    return run_snake_wrapper(
        wrapper="file:tools/pindel/call",
        inputs=input_dict,
         
    )


@collect_tool()
def call(
    *,
    reference: str,
    bam_files: list[str],
    bam_config: str,
    include_bed: Optional[str] = None,
    exclude_bed: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call variants with pindel.

    Args:
        reference: Path to the reference genome fasta file.
        bam_files: List of paths to one or more BAM files.
        bam_config: Path to BAM configuration file (see pindel documentation).
        include_bed (optional): Path to a BED file specifying regions to include.
        exclude_bed (optional): Path to a BED file specifying regions to exclude.
            Note: Include and exclude BED files are incompatible with each other.
            Either provide one or neither.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_call(
        reference=reference,
        bam_files=bam_files,
        bam_config=bam_config,
        include_bed=include_bed,
        exclude_bed=exclude_bed,
         
    )
