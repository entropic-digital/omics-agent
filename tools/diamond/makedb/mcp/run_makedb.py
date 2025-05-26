from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_makedb(
    *,
    input_fname: str,
    output_fname: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the DIAMOND makedb tool to create a DIAMOND database from a reference genome.

    Args:
        input_fname: Path to the reference genome sequence file (Fasta formatted).
        output_fname: Path where the generated DIAMOND database will be saved.
        extra (optional): Additional command-line parameters to pass to DIAMOND makedb.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/diamond/makedb",
        inputs={"input_fname": input_fname},
        outputs={"output_fname": output_fname},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def makedb(
    *,
    input_fname: str,
    output_fname: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the DIAMOND makedb tool to create a DIAMOND database from a reference genome.

    Args:
        input_fname: Path to the reference genome sequence file (Fasta formatted).
        output_fname: Path where the generated DIAMOND database will be saved.
        extra (optional): Additional command-line parameters to pass to DIAMOND makedb.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_makedb(
        input_fname=input_fname, output_fname=output_fname, extra=extra,      
    )
