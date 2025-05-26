from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_filter(
    *,
    bam_files: str,
    output_bam: str,
    tags: Optional[str] = None,
    min_size: Optional[int] = None,
    max_size: Optional[int] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    additional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Filters BAM files using BamTools.

    Args:
        bam_files: Path to input BAM files, must be the first input.
        output_bam: Path to the filtered output BAM file, must be the first output.
        tags (optional): Filtering tags parameter.
        min_size (optional): Minimum insert size.
        max_size (optional): Maximum insert size.
        min_length (optional): Minimum read length.
        max_length (optional): Maximum read length.
        additional_params (optional): Other filtering and optional parameters.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "tags": tags,
        "min_size": min_size,
        "max_size": max_size,
        "min_length": min_length,
        "max_length": max_length,
        "additional_params": additional_params,
    }
    # Filter out None values from params
    params = {key: value for key, value in params.items() if value is not None}

    return run_snake_wrapper(
        wrapper="file:tools/bamtools/filter",
        inputs={"bam_files": bam_files},
        outputs={"output_bam": output_bam},
        params=params,
         
    )


@collect_tool()
def filter_tool(
    *,
    bam_files: str,
    output_bam: str,
    tags: Optional[str] = None,
    min_size: Optional[int] = None,
    max_size: Optional[int] = None,
    min_length: Optional[int] = None,
    max_length: Optional[int] = None,
    additional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Filters BAM files using BamTools.

    Args:
        bam_files: Path to input BAM files, must be the first input.
        output_bam: Path to the filtered output BAM file, must be the first output.
        tags (optional): Filtering tags parameter.
        min_size (optional): Minimum insert size.
        max_size (optional): Maximum insert size.
        min_length (optional): Minimum read length.
        max_length (optional): Maximum read length.
        additional_params (optional): Other filtering and optional parameters.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_filter(
        bam_files=bam_files,
        output_bam=output_bam,
        tags=tags,
        min_size=min_size,
        max_size=max_size,
        min_length=min_length,
        max_length=max_length,
        additional_params=additional_params,
         
    )
