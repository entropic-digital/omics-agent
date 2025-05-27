from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_intervallisttobed(
    *,
    interval_list: str,
    bed_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk IntervalListToBed.

    Args:
        interval_list: Path to the input interval list.
        bed_file: Path to the output BED file.
        java_opts (optional): Additional arguments for the Java compiler (not for `-XmX` or `-Djava.io.tmpdir`).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/intervallisttobed",
        inputs=dict(interval_list=interval_list),
        outputs=dict(bed_file=bed_file),
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def intervallisttobed(
    *,
    interval_list: str,
    bed_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk IntervalListToBed.

    Args:
        interval_list: Path to the input interval list.
        bed_file: Path to the output BED file.
        java_opts (optional): Additional arguments for the Java compiler (not for `-XmX` or `-Djava.io.tmpdir`).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_intervallisttobed(
        interval_list=interval_list,
        bed_file=bed_file,
        java_opts=java_opts,
        extra=extra,
         
    )
