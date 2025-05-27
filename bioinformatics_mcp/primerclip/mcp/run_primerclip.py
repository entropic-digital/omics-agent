from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_primerclip(
    *,
    sam_file: str,
    master_primer_file: str,
    output_sam_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Primer trimming on SAM file.

    Args:
        sam_file: Path to the input SAM file.
        master_primer_file: Path to the master primer file.
        output_sam_file: Path to the output SAM file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/primerclip",
        inputs=dict(sam_file=sam_file, master_primer_file=master_primer_file),
        outputs=dict(output_sam_file=output_sam_file),
         
    )


@collect_tool()
def primerclip(
    *,
    sam_file: str,
    master_primer_file: str,
    output_sam_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Primer trimming on SAM file.

    Args:
        sam_file: Path to the input SAM file.
        master_primer_file: Path to the master primer file.
        output_sam_file: Path to the output SAM file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_primerclip(
        sam_file=sam_file,
        master_primer_file=master_primer_file,
        output_sam_file=output_sam_file,
         
    )
