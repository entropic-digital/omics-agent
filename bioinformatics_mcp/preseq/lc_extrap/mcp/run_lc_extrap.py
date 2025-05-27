from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_lc_extrap(
    *,
    input_file: str,
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Runs the preseq lc_extrap tool to estimate library complexity of sequencing data.

    Args:
        input_file: Path to the input file, either a sorted BED or BAM file containing duplicates.
        output_file: Path to the output file where the .lc_extrap result should be stored.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/preseq/lc_extrap",
        inputs=dict(input_file=input_file),
        outputs=dict(output_file=output_file),
         
    )


@collect_tool()
def lc_extrap(
    *,
    input_file: str,
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Executes the preseq lc_extrap tool for library complexity estimation.

    Args:
        input_file: Path to the input file, either a sorted BED or BAM file containing duplicates.
        output_file: Path to the output file where the .lc_extrap result should be stored.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_lc_extrap(input_file=input_file, output_file=output_file,      )
