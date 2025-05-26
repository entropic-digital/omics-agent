from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_replace_bases(
    *,
    infile: str,
    outfile: str,
    from_base: str,
    to_base: str,
    log_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Replaces all occurrences of one letter with another in a FASTA/FASTQ file.

    Args:
        infile: Input FASTA/FASTQ file path.
        outfile: Output FASTA/FASTQ file path with replaced bases.
        from_base: Base to replace in the input file.
        to_base: Base to replace with in the input file.
        log_file (optional): File to write log messages.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/pyfastaq/replace_bases",
        inputs=dict(infile=infile),
        outputs=dict(outfile=outfile),
        params={
            "from_base": from_base,
            "to_base": to_base,
            "log_file": log_file,
        }
        if log_file
        else {
            "from_base": from_base,
            "to_base": to_base,
        },
         
    )


@collect_tool()
def replace_bases(
    *,
    infile: str,
    outfile: str,
    from_base: str,
    to_base: str,
    log_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Replaces all occurrences of one letter with another in a FASTA/FASTQ file.

    Args:
        infile: Input FASTA/FASTQ file path.
        outfile: Output FASTA/FASTQ file path with replaced bases.
        from_base: Base to replace in the input file.
        to_base: Base to replace with in the input file.
        log_file (optional): File to write log messages.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_replace_bases(
        infile=infile,
        outfile=outfile,
        from_base=from_base,
        to_base=to_base,
        log_file=log_file,
         
    )
