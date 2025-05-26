from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_prinseq_plus_plus(
    *,
    fastx_files: str,
    r1: str,
    r1_bad: Optional[str] = None,
    r2: Optional[str] = None,
    r1_single: Optional[str] = None,
    r2_single: Optional[str] = None,
    r2_bad: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    C++ implementation of the prinseq-lite.pl program. It can be used to filter, reformat
    or trim genomic and metagenomic sequence data.

    Args:
        fastx_files: Input FASTX file(s).
        r1: Output FASTX file for R1.
        r1_bad (optional): FASTX file for bad sequences in R1.
        r2 (optional): Output FASTX file for R2 (if PE).
        r1_single (optional): FASTX file for single R1 reads (if PE).
        r2_single (optional): FASTX file for single R2 reads (if PE).
        r2_bad (optional): FASTX file for bad sequences in R2.
        extra (optional): Additional program options.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"fastx_files": fastx_files}
    outputs = {
        "r1": r1,
        "r1_bad": r1_bad,
        "r2": r2,
        "r1_single": r1_single,
        "r2_single": r2_single,
        "r2_bad": r2_bad,
    }
    params = {"extra": extra} if extra else {}

    return run_snake_wrapper(
        wrapper="file:tools/prinseq-plus-plus",
        inputs=inputs,
        outputs={k: v for k, v in outputs.items() if v is not None},
        params=params,
         
    )


@collect_tool()
def prinseq_plus_plus(
    *,
    fastx_files: str,
    r1: str,
    r1_bad: Optional[str] = None,
    r2: Optional[str] = None,
    r1_single: Optional[str] = None,
    r2_single: Optional[str] = None,
    r2_bad: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    C++ implementation of the prinseq-lite.pl program. It can be used to filter, reformat
    or trim genomic and metagenomic sequence data.

    Args:
        fastx_files: Input FASTX file(s).
        r1: Output FASTX file for R1.
        r1_bad (optional): FASTX file for bad sequences in R1.
        r2 (optional): Output FASTX file for R2 (if PE).
        r1_single (optional): FASTX file for single R1 reads (if PE).
        r2_single (optional): FASTX file for single R2 reads (if PE).
        r2_bad (optional): FASTX file for bad sequences in R2.
        extra (optional): Additional program options.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_prinseq_plus_plus(
        fastx_files=fastx_files,
        r1=r1,
        r1_bad=r1_bad,
        r2=r2,
        r1_single=r1_single,
        r2_single=r2_single,
        r2_bad=r2_bad,
        extra=extra,
         
    )
