from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_rebaler(
    *,
    reads: str,
    assembly: str,
    output_dir: str,
    sample_name: Optional[str] = None,
    threads: Optional[int] = 1,
     
) -> subprocess.CompletedProcess:
    """
    Rebaler: Reference-based long read assemblies of bacterial genomes.

    Args:
        reads: Path to input reads file.
        assembly: Path to the reference assembly file.
        output_dir: Directory to store output files.
        sample_name (optional): Name of the sample being processed.
        threads (optional): Number of threads to use. Default is 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/rebaler",
        inputs=dict(reads=reads, assembly=assembly),
        outputs={"output_dir": output_dir},
        params={"sample_name": sample_name, "threads": threads},
         
    )


@collect_tool()
def rebaler(
    *,
    reads: str,
    assembly: str,
    output_dir: str,
    sample_name: Optional[str] = None,
    threads: Optional[int] = 1,
     
) -> subprocess.CompletedProcess:
    """
    Rebaler: Reference-based long read assemblies of bacterial genomes.

    Args:
        reads: Path to input reads file.
        assembly: Path to the reference assembly file.
        output_dir: Directory to store output files.
        sample_name (optional): Name of the sample being processed.
        threads (optional): Number of threads to use. Default is 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_rebaler(
        reads=reads,
        assembly=assembly,
        output_dir=output_dir,
        sample_name=sample_name,
        threads=threads,
         
    )
