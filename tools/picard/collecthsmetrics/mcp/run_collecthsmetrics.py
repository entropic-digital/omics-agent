from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_collecthsmetrics(
    *,
    bam: str,
    metrics: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collects hybrid-selection (HS) metrics for a SAM or BAM file using picard.

    Args:
        bam: Path to the input BAM file.
        metrics: Path to the output metrics file.
        java_opts (optional): Additional arguments to be passed to the java compiler (e.g., "-XX:ParallelGCThreads=10").
                              Note: Do not specify `-XmX` or `-Djava.io.tmpdir`, as they are handled automatically.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/picard/collecthsmetrics",
        inputs={"bam": bam},
        outputs={"metrics": metrics},
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def collecthsmetrics(
    *,
    bam: str,
    metrics: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collects hybrid-selection (HS) metrics for a SAM or BAM file using picard.

    Args:
        bam: Path to the input BAM file.
        metrics: Path to the output metrics file.
        java_opts (optional): Additional arguments to be passed to the java compiler (e.g., "-XX:ParallelGCThreads=10").
                              Note: Do not specify `-XmX` or `-Djava.io.tmpdir`, as they are handled automatically.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collecthsmetrics(
        bam=bam,
        metrics=metrics,
        java_opts=java_opts,
        extra=extra,
         
    )
