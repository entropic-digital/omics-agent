from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_calculatecontamination(
    *,
    tumor: str,
    normal: Optional[str] = None,
    output: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate the fraction of reads coming from cross-sample contamination using GATK CalculateContamination.

    Args:
        tumor: Path to pileup table from GATK GetPileupSummaries (required).
        normal (optional): Path to normal pileup table.
        output: Path to contamination table (required).
        java_opts (optional): Additional arguments to pass to the Java compiler,
                              e.g., '-XX:ParallelGCThreads=10'. Excludes `-XmX` or `-Djava.io.tmpdir`.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/calculatecontamination",
        inputs=dict(tumor=tumor, normal=normal) if normal else dict(tumor=tumor),
        outputs=dict(output=output),
        params={
            key: value
            for key, value in [("java_opts", java_opts), ("extra", extra)]
            if value
        },
         
    )


@collect_tool()
def calculatecontamination(
    *,
    tumor: str,
    normal: Optional[str] = None,
    output: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate the fraction of reads coming from cross-sample contamination using GATK CalculateContamination.

    Args:
        tumor: Path to pileup table from GATK GetPileupSummaries (required).
        normal (optional): Path to normal pileup table.
        output: Path to contamination table (required).
        java_opts (optional): Additional arguments to pass to the Java compiler,
                              e.g., '-XX:ParallelGCThreads=10'. Excludes `-XmX` or `-Djava.io.tmpdir`.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_calculatecontamination(
        tumor=tumor,
        normal=normal,
        output=output,
        java_opts=java_opts,
        extra=extra,
         
    )
