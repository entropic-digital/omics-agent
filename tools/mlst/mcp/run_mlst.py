from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_mlst(
    *,
    genomic_assembly: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Scan contig files against traditional PubMLST typing schemes.

    Args:
        genomic_assembly: Path to the genomic assembly file in FASTA format.
        output_file: Path to the output file to store the results.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/mlst",
        inputs=dict(genomic_assembly=genomic_assembly),
        outputs=dict(output_file=output_file),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def mlst(
    *,
    genomic_assembly: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Scan contig files against traditional PubMLST typing schemes.

    Args:
        genomic_assembly: Path to the genomic assembly file in FASTA format.
        output_file: Path to the output file to store the results.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mlst(
        genomic_assembly=genomic_assembly,
        output_file=output_file,
        extra=extra,
         
    )
