from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_read_gc(
    *,
    input_file: str,
    xls: Optional[str] = None,
    plot_r: Optional[str] = None,
    pdf: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GC content distribution of reads.

    Args:
        input_file: Path to the SAM/BAM file.
        xls (optional): Optional path to the GC percent table.
        plot_r (optional): Optional path to the R script.
        pdf (optional): Optional path to the PDF-formatted graph.
        extra (optional): Optional parameters for `read_gc.py`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/rseqc/read_gc",
        inputs={"input_file": input_file},
        outputs={
            "xls": xls,
            "plot_r": plot_r,
            "pdf": pdf,
        },
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def read_gc(
    *,
    input_file: str,
    xls: Optional[str] = None,
    plot_r: Optional[str] = None,
    pdf: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GC content distribution of reads.

    Args:
        input_file: Path to the SAM/BAM file.
        xls (optional): Optional path to the GC percent table.
        plot_r (optional): Optional path to the R script.
        pdf (optional): Optional path to the PDF-formatted graph.
        extra (optional): Optional parameters for `read_gc.py`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_read_gc(
        input_file=input_file,
        xls=xls,
        plot_r=plot_r,
        pdf=pdf,
        extra=extra,
         
    )
