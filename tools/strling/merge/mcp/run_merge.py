from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_merge(
    *,
    input_files: str,
    output_file: str,
    min_evidence: int,
    sample_names: Optional[str] = None,
    regions_bed: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    STRling merge tool to prepare joint calling of STR loci across all given samples.

    Args:
        input_files: Path to input files (STRling output).
        output_file: Path to the output file to write results.
        min_evidence: Minimum read evidence required from at least one sample.
        sample_names (optional): Path to file containing sample names.
        regions_bed (optional): BED file specifying regions of interest for STR calling.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/strling/merge",
        inputs=dict(
            input_files=input_files, sample_names=sample_names, regions_bed=regions_bed
        ),
        outputs=dict(output_file=output_file),
        params=dict(min_evidence=min_evidence),
         
    )


@collect_tool()
def merge(
    *,
    input_files: str,
    output_file: str,
    min_evidence: int,
    sample_names: Optional[str] = None,
    regions_bed: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    STRling merge tool to prepare joint calling of STR loci across all given samples.

    Args:
        input_files: Path to input files (STRling output).
        output_file: Path to the output file to write results.
        min_evidence: Minimum read evidence required from at least one sample.
        sample_names (optional): Path to file containing sample names.
        regions_bed (optional): BED file specifying regions of interest for STR calling.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_merge(
        input_files=input_files,
        output_file=output_file,
        min_evidence=min_evidence,
        sample_names=sample_names,
        regions_bed=regions_bed,
         
    )
