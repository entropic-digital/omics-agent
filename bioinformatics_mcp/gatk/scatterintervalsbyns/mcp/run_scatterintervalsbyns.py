from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_scatterintervalsbyns(
    *,
    reference_genome: str,
    interval_list: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk ScatterIntervalsByNs.

    Args:
        reference_genome: Path to the reference genome file.
        interval_list: Path to the interval list output file.
        java_opts (optional): Additional Java compiler options (e.g., "-XX:ParallelGCThreads=10").
                            Note: This does not include `-XmX` or `-Djava.io.tmpdir`.
        extra (optional): Additional program arguments to be passed to ScatterIntervalsByNs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/scatterintervalsbyns",
        inputs={"reference_genome": reference_genome},
        outputs={"interval_list": interval_list},
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def scatterintervalsbyns(
    *,
    reference_genome: str,
    interval_list: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk ScatterIntervalsByNs.

    Args:
        reference_genome: Path to the reference genome file.
        interval_list: Path to the interval list output file.
        java_opts (optional): Additional Java compiler options (e.g., "-XX:ParallelGCThreads=10").
                            Note: This does not include `-XmX` or `-Djava.io.tmpdir`.
        extra (optional): Additional program arguments to be passed to ScatterIntervalsByNs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_scatterintervalsbyns(
        reference_genome=reference_genome,
        interval_list=interval_list,
        java_opts=java_opts,
        extra=extra,
         
    )
