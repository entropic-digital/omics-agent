from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_annotatePeaks(
    *,
    peak_or_bed_file: str,
    optional_input_file: Optional[str] = None,
    annotation_file: str,
    optional_output_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Performing peak annotation to associate peaks with nearby genes.

    Args:
        peak_or_bed_file: Path to the peak or BED file.
        optional_input_file (optional): Path to additional optional input files, e.g., gtf, bedGraph, wiggle.
        annotation_file: Path to the output annotation file (.txt).
        optional_output_file (optional): Path to additional optional output files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/homer/annotatePeaks",
        inputs={
            "peak_or_bed_file": peak_or_bed_file,
            "optional_input_file": optional_input_file if optional_input_file else None,
        },
        outputs={
            "annotation_file": annotation_file,
            "optional_output_file": optional_output_file
            if optional_output_file
            else None,
        },
         
    )


@collect_tool()
def annotatePeaks(
    *,
    peak_or_bed_file: str,
    optional_input_file: Optional[str] = None,
    annotation_file: str,
    optional_output_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Performing peak annotation to associate peaks with nearby genes.

    Args:
        peak_or_bed_file: Path to the peak or BED file.
        optional_input_file (optional): Path to additional optional input files, e.g., gtf, bedGraph, wiggle.
        annotation_file: Path to the output annotation file (.txt).
        optional_output_file (optional): Path to additional optional output files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_annotatePeaks(
        peak_or_bed_file=peak_or_bed_file,
        optional_input_file=optional_input_file,
        annotation_file=annotation_file,
        optional_output_file=optional_output_file,
         
    )
