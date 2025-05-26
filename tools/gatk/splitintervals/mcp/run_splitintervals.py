from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_splitintervals(
    *,
    intervals: str,
    output: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Runs the GATK SplitIntervals tool.

    This tool takes in a list of intervals and splits them into interval files
    for scattering, producing files with an approximately equal number of bases.

    Args:
        intervals: Path to the input intervals or BED file.
        output: Path to the directory where output files will be written.
        java_opts (optional): Additional options to pass to the Java compiler,
            excluding `-XmX` or `-Djava.io.tmpdir` (handled automatically).
        extra (optional): Additional program arguments not including `--scatter-count`,
            `--output`, `--interval-file-prefix`, `--interval-file-num-digits`, or `--extension`.
            
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/splitintervals",
        inputs=dict(intervals=intervals),
        outputs=dict(output=output),
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def splitintervals(
    *,
    intervals: str,
    output: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Executes the GATK SplitIntervals tool in the MCP server context.

    Args:
        intervals: Path to the input intervals or BED file.
        output: Path to the directory where output files will be written.
        java_opts (optional): Additional options to pass to the Java compiler,
            excluding `-XmX` or `-Djava.io.tmpdir` (handled automatically).
        extra (optional): Additional program arguments not including `--scatter-count`,
            `--output`, `--interval-file-prefix`, `--interval-file-num-digits`, or `--extension`.
            
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_splitintervals(
        intervals=intervals,
        output=output,
        java_opts=java_opts,
        extra=extra,
         
    )
