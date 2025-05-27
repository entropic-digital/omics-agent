from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_stats(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate VCF stats using bcftools stats.

    Args:
        input_file: Path to the input BCF, VCF, or VCF.gz file.
        output_file: Path to the output stats text file.
        extra (optional): Additional program arguments excluding '--threads', '-f/--fasta-ref', or '-o/--output'.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bcftools/stats",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def stats(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate VCF stats using bcftools stats.

    Args:
        input_file: Path to the input BCF, VCF, or VCF.gz file.
        output_file: Path to the output stats text file.
        extra (optional): Additional program arguments excluding '--threads', '-f/--fasta-ref', or '-o/--output'.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_stats(
        input_file=input_file,
        output_file=output_file,
        extra=extra,
         
    )
