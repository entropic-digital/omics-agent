from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_make_table(
    *,
    input_files: List[str],
    output_file: str,
    names: Optional[List[str]] = None,
    params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Build a sequence-sample table from denoised samples using DADA2's `makeSequenceTable` function.

    Args:
        input_files: List of RDS files with denoised samples (se) or denoised and merged samples (pe).
        output_file: Path to the RDS file where the resulting table will be stored.
        names (optional): List of sample names to use instead of paths.
        params (optional): Additional optional arguments for the `makeSequenceTable` function (as Python key=value pairs).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/dada2/make-table",
        inputs=dict(input_files=input_files),
        outputs={"output_file": output_file},
        params={"names": names, **(params if params else {})},
         
    )


@collect_tool()
def make_table(
    *,
    input_files: List[str],
    output_file: str,
    names: Optional[List[str]] = None,
    params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Build a sequence-sample table from denoised samples using DADA2's `makeSequenceTable` function.

    Args:
        input_files: List of RDS files with denoised samples (se) or denoised and merged samples (pe).
        output_file: Path to the RDS file where the resulting table will be stored.
        names (optional): List of sample names to use instead of paths.
        params (optional): Additional optional arguments for the `makeSequenceTable` function (as Python key=value pairs).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_make_table(
        input_files=input_files,
        output_file=output_file,
        names=names,
        params=params,
         
    )
