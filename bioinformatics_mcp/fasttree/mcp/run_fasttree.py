from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_fasttree(
    *,
    input_file: str,
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Build phylogenetic trees using FastTree.

    Args:
        input_file: Path to the input FASTA or interleaved Phylip alignment file.
        output_file: Path to the output Newick formatted tree file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/fasttree",
        inputs=dict(input=input_file),
        outputs=dict(output=output_file),
         
    )


@collect_tool()
def fasttree(
    *,
    input_file: str,
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Build phylogenetic trees using FastTree.

    Args:
        input_file: Path to the input FASTA or interleaved Phylip alignment file.
        output_file: Path to the output Newick formatted tree file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_fasttree(input_file=input_file, output_file=output_file,      )
