from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_scan(
    *,
    input_fasta: str,
    output_txt: str,
     
) -> subprocess.CompletedProcess:
    """
    Scan homopolymers and microsatellites with MSIsensor.

    Args:
        input_fasta: Path to the input (multi)fasta formatted file.
        output_txt: Path to the output text file to store homopolymers and microsatellites.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/msisensor/scan",
        inputs={"input_fasta": input_fasta},
        outputs={"output_txt": output_txt},
         
    )


@collect_tool()
def scan(
    *,
    input_fasta: str,
    output_txt: str,
     
) -> subprocess.CompletedProcess:
    """
    Scan homopolymers and microsatellites with MSIsensor.

    Args:
        input_fasta: Path to the input (multi)fasta formatted file.
        output_txt: Path to the output text file to store homopolymers and microsatellites.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_scan(input_fasta=input_fasta, output_txt=output_txt,      )
