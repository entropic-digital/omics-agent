from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_assembly_stats(
    *,
    assembly: str,
    assembly_stats: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generates a report of summary statistics for a genome assembly.

    Args:
        assembly: Genomic assembly (fasta format).
        assembly_stats: Output file for the assembly statistics (format of your choosing, default = tab-delimited).
        extra (optional): Additional parameters, see `assembly-stats official documentation <https://github.com/sanger-pathogens/assembly-stats#usage>`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/assembly-stats",
        inputs=dict(assembly=assembly),
        outputs=dict(assembly_stats=assembly_stats),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def assembly_stats_tool(
    *,
    assembly: str,
    assembly_stats: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generates a report of summary statistics for a genome assembly.

    Args:
        assembly: Genomic assembly (fasta format).
        assembly_stats: Output file for the assembly statistics (format of your choosing, default = tab-delimited).
        extra (optional): Additional parameters, see `assembly-stats official documentation <https://github.com/sanger-pathogens/assembly-stats#usage>`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_assembly_stats(
        assembly=assembly, assembly_stats=assembly_stats, extra=extra,
    )
