from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_alignmentsieve(
    *,
    aln: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Filters/shifts alignments in a BAM/CRAM file according to the specified parameters.

    Args:
        aln: Path to BAM/CRAM formatted alignments. BAM files must be indexed.
        output: Path to filtered BAM alignments or BEDPE intervals.
        extra (optional): Optional arguments for `alignmentSieve.py`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/deeptools/alignmentsieve",
        inputs={"aln": aln},
        outputs={"output": output},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def alignmentsieve(
    *,
    aln: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Filters/shifts alignments in a BAM/CRAM file according to the specified parameters.

    Args:
        aln: Path to BAM/CRAM formatted alignments. BAM files must be indexed.
        output: Path to filtered BAM alignments or BEDPE intervals.
        extra (optional): Optional arguments for `alignmentSieve.py`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_alignmentsieve(
        aln=aln,
        output=output,
        extra=extra,
         
    )
