from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_filter_json(
    *,
    bam_file: str,
    output_bam: str,
    filter_json_file: str,
    region: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Filters BAM files using JSON-script for filtering parameters and rules.

    Args:
        bam_file: Path to the input BAM file.
        output_bam: Path to the output BAM file.
        filter_json_file: Path to the JSON-formatted filter file.
        region (optional): Region string; formats documented in bamtools.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {"json": filter_json_file}
    if region:
        params["region"] = region

    return run_snake_wrapper(
        wrapper="file:tools/bamtools/filter_json",
        inputs={"bam_file": bam_file},
        outputs={"output_bam": output_bam},
        params=params,
         
    )


@collect_tool()
def filter_json(
    *,
    bam_file: str,
    output_bam: str,
    filter_json_file: str,
    region: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Filters BAM files using JSON-script for filtering parameters and rules.

    Args:
        bam_file: Path to the input BAM file.
        output_bam: Path to the output BAM file.
        filter_json_file: Path to the JSON-formatted filter file.
        region (optional): Region string; formats documented in bamtools.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_filter_json(
        bam_file=bam_file,
        output_bam=output_bam,
        filter_json_file=filter_json_file,
        region=region,
         
    )
