from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_generate_data_matrix(
    *,
    input_files: List[str],
    output_matrix: str,
     
) -> subprocess.CompletedProcess:
    """
    Run rsem-generate-data-matrix to combine a set of single-sample rsem results into a single matrix.

    Args:
        input_files: A list of rsem results files.
        output_matrix: Path to the output file, summarizing quantification results by allele/gene/isoform per sample.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/rsem/generate-data-matrix",
        inputs=dict(input_files=input_files),
        outputs=dict(output_matrix=output_matrix),
         
    )


@collect_tool()
def generate_data_matrix(
    *,
    input_files: List[str],
    output_matrix: str,
     
) -> subprocess.CompletedProcess:
    """
    Run rsem-generate-data-matrix to combine a set of single-sample rsem results into a single matrix.

    Args:
        input_files: A list of rsem results files.
        output_matrix: Path to the output file, summarizing quantification results by allele/gene/isoform per sample.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_generate_data_matrix(
        input_files=input_files, output_matrix=output_matrix,      
    )
