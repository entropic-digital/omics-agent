from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_getDifferentialPeaks(
    *,
    condition1: str,
    condition2: str,
    output_file: str,
    peak_files_condition1: str,
    peak_files_condition2: str,
    annotation_file: Optional[str] = None,
    size_intersection: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Detect differentially bound ChIP peaks between samples.

    Args:
        condition1: Name/label for the first condition (or sample group).
        condition2: Name/label for the second condition (or sample group).
        output_file: The file where the results will be written.
        peak_files_condition1: Comma-separated list of peak files for condition1.
        peak_files_condition2: Comma-separated list of peak files for condition2.
        annotation_file (optional): Path to an annotation file with gene associations.
        size_intersection (optional): Minimum size of the peak intersection.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/homer/getDifferentialPeaks",
        inputs=dict(
            peak_files_condition1=peak_files_condition1,
            peak_files_condition2=peak_files_condition2,
        ),
        params={
            "condition1": condition1,
            "condition2": condition2,
            "annotation_file": annotation_file,
            "size_intersection": size_intersection,
        },
        outputs=dict(output_file=output_file),
         
    )


@collect_tool()
def getDifferentialPeaks(
    *,
    condition1: str,
    condition2: str,
    output_file: str,
    peak_files_condition1: str,
    peak_files_condition2: str,
    annotation_file: Optional[str] = None,
    size_intersection: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Detect differentially bound ChIP peaks between samples.

    Args:
        condition1: Name/label for the first condition (or sample group).
        condition2: Name/label for the second condition (or sample group).
        output_file: The file where the results will be written.
        peak_files_condition1: Comma-separated list of peak files for condition1.
        peak_files_condition2: Comma-separated list of peak files for condition2.
        annotation_file (optional): Path to an annotation file with gene associations.
        size_intersection (optional): Minimum size of the peak intersection.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_getDifferentialPeaks(
        condition1=condition1,
        condition2=condition2,
        output_file=output_file,
        peak_files_condition1=peak_files_condition1,
        peak_files_condition2=peak_files_condition2,
        annotation_file=annotation_file,
        size_intersection=size_intersection,
         
    )
