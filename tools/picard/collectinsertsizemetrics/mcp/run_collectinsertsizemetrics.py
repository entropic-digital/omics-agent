from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_collectinsertsizemetrics(
    *,
    bam: str,
    txt: str,
    pdf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collect metrics on insert size of paired-end reads with Picard tools.

    Args:
        bam: Path to the input BAM file.
        txt: Path to the output text file containing metrics.
        pdf: Path to the output PDF file containing the insert size histogram.
        java_opts (optional): Additional arguments for the Java compiler.
        extra (optional): Additional program-specific arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/picard/collectinsertsizemetrics",
        inputs=dict(bam=bam),
        outputs=dict(txt=txt, pdf=pdf),
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def collectinsertsizemetrics(
    *,
    bam: str,
    txt: str,
    pdf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collect metrics on insert size of paired-end reads with Picard tools.

    Args:
        bam: Path to the input BAM file.
        txt: Path to the output text file containing metrics.
        pdf: Path to the output PDF file containing the insert size histogram.
        java_opts (optional): Additional arguments for the Java compiler.
        extra (optional): Additional program-specific arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collectinsertsizemetrics(
        bam=bam, txt=txt, pdf=pdf, java_opts=java_opts, extra=extra,      
    )
