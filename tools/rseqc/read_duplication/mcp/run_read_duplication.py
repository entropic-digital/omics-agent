from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_read_duplication(
    *,
    input_file: str,
    pos: Optional[str] = None,
    seq: Optional[str] = None,
    plot_r: Optional[str] = None,
    pdf: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Estimate read duplication rate using RSeQC's read_duplication.py.

    Args:
        input_file: Path to the SAM/BAM input file.
        pos (optional): Path to output file for read duplication determined from mapping position of reads.
        seq (optional): Path to output file for read duplication determined from the sequence of reads.
        plot_r (optional): Path to output R script file for generating graphs.
        pdf (optional): Path to output PDF file for formatted graphs.
        extra (optional): Additional command-line parameters to provide to `read_duplication.py`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/rseqc/read_duplication",
        inputs={"input_file": input_file},
        outputs={"pos": pos, "seq": seq, "plot_r": plot_r, "pdf": pdf},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def read_duplication(
    *,
    input_file: str,
    pos: Optional[str] = None,
    seq: Optional[str] = None,
    plot_r: Optional[str] = None,
    pdf: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Estimate read duplication rate using RSeQC's read_duplication.py.

    Args:
        input_file: Path to the SAM/BAM input file.
        pos (optional): Path to output file for read duplication determined from mapping position of reads.
        seq (optional): Path to output file for read duplication determined from the sequence of reads.
        plot_r (optional): Path to output R script file for generating graphs.
        pdf (optional): Path to output PDF file for formatted graphs.
        extra (optional): Additional command-line parameters to provide to `read_duplication.py`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_read_duplication(
        input_file=input_file,
        pos=pos,
        seq=seq,
        plot_r=plot_r,
        pdf=pdf,
        extra=extra,
         
    )
