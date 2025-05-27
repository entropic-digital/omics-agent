from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    fasta_file: str,
    output_directory: str,
    prefix: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Creates a bwa-meme index.

    Args:
        fasta_file: Path to the fasta file.
        output_directory: Directory where the output files will be stored.
        prefix (optional): Prefix for the output index files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bwa-meme/index",
        inputs={"fasta_file": fasta_file},
        outputs={"output_directory": output_directory},
        params={"prefix": prefix} if prefix else {},
         
    )


@collect_tool()
def index(
    *,
    fasta_file: str,
    output_directory: str,
    prefix: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Creates a bwa-meme index.

    Args:
        fasta_file: Path to the fasta file.
        output_directory: Directory where the output files will be stored.
        prefix (optional): Prefix for the output index files.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        fasta_file=fasta_file,
        output_directory=output_directory,
        prefix=prefix,
         
    )
