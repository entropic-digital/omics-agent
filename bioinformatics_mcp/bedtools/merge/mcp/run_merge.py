from typing import Union, Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_merge(
    *,
    input: Union[str, List[str]],
    output: str,
    extra: Optional[str] = None,
    threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Merge entries in one or multiple BED/BAM/VCF/GFF files with bedtools.

    Args:
        input: Path or list of paths to interval(s) file(s) (BED/GFF/VCF/BAM).
        output: Path to merged interval(s) file.
        extra (optional): Additional program arguments (except for `-i`).
        threads: Number of threads to use, default is 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bedtools/merge",
        inputs={"input": input},
        outputs={"output": output},
        params={"extra": extra} if extra else {},
        threads=threads,
         
    )


@collect_tool()
def mergeBed(
    *,
    input: Union[str, List[str]],
    output: str,
    extra: Optional[str] = None,
    threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Merge entries in one or multiple BED/BAM/VCF/GFF files with bedtools.

    Args:
        input: Path or list of paths to interval(s) file(s) (BED/GFF/VCF/BAM).
        output: Path to merged interval(s) file.
        extra (optional): Additional program arguments (except for `-i`).
        threads: Number of threads to use, default is 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_merge(
        input=input,
        output=output,
        extra=extra,
        threads=threads,
         
    )
