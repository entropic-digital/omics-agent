from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_jellyfish_merge(
    *,
    input_files: List[str],
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Merge jellyfish databases.

    Args:
        input_files: List of input jellyfish kmer count files to be merged.
        output_file: File path for the merged jellyfish kmer count file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/jellyfish/merge",
        inputs={"input_files": input_files},
        outputs={"output_file": output_file},
         
    )


@collect_tool()
def jellyfish_merge(
    *,
    input_files: List[str],
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Merge jellyfish databases.

    Args:
        input_files: List of input jellyfish kmer count files to be merged.
        output_file: File path for the merged jellyfish kmer count file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_jellyfish_merge(
        input_files=input_files, output_file=output_file,      
    )
