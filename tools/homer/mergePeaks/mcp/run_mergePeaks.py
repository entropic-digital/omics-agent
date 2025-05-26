from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_mergePeaks(
    *,
    input_files: str,
    output_file: str,
    min_overlap: Optional[int] = None,
    delimiter: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Merge ChIP-Seq peaks from multiple peak files using HOMER mergePeaks.

    Args:
        input_files: Paths to the input peak files, separated by spaces.
        output_file: Path to the output file where the merged peaks will be saved.
        min_overlap (optional): Minimum overlap required to merge peaks (default: None).
        delimiter (optional): Delimiter to use in the output file (default: None).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {}
    if min_overlap is not None:
        params["min_overlap"] = min_overlap
    if delimiter is not None:
        params["delimiter"] = delimiter

    return run_snake_wrapper(
        wrapper="file:tools/homer/mergePeaks",
        inputs={"input_files": input_files},
        outputs={"output_file": output_file},
        params=params,
         
    )


@collect_tool()
def mergePeaks(
    *,
    input_files: str,
    output_file: str,
    min_overlap: Optional[int] = None,
    delimiter: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Merge ChIP-Seq peaks from multiple peak files using HOMER mergePeaks.

    Args:
        input_files: Paths to the input peak files, separated by spaces.
        output_file: Path to the output file where the merged peaks will be saved.
        min_overlap (optional): Minimum overlap required to merge peaks (default: None).
        delimiter (optional): Delimiter to use in the output file (default: None).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mergePeaks(
        input_files=input_files,
        output_file=output_file,
        min_overlap=min_overlap,
        delimiter=delimiter,
         
    )
