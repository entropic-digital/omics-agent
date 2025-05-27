from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_read_distribution(
    *,
    aln: str,
    refgene: str,
    output: str,
     
) -> subprocess.CompletedProcess:
    """
    Calculate how mapped reads were distributed over genome features.

    Args:
        aln: Path to SAM/BAM input file.
        refgene: Path to refgene model (BED).
        output: Path to read distribution (txt).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/rseqc/read_distribution",
        inputs={"aln": aln, "refgene": refgene},
        outputs={"output": output},
         
    )


@collect_tool()
def read_distribution(
    *,
    aln: str,
    refgene: str,
    output: str,
     
) -> subprocess.CompletedProcess:
    """
    Calculate how mapped reads were distributed over genome features.

    Args:
        aln: Path to SAM/BAM input file.
        refgene: Path to refgene model (BED).
        output: Path to read distribution (txt).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_read_distribution(aln=aln, refgene=refgene, output=output,      )
