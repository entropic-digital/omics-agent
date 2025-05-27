from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_bedtointervallist(
    *,
    bed: str,
    reference_dict: str,
    interval_list: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert a BED file to Picard Interval List format using `picard BedToIntervalList`.

    Args:
        bed: Path to the input BED file (region file).
        reference_dict: Path to the genome dictionary file (e.g., from samtools dict or 
            picard CreateSequenceDictionary).
        interval_list: Path to the output interval list in Picard format.
        java_opts (optional): Additional Java options, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments for picard BedToIntervalList.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/picard/bedtointervallist",
        inputs=dict(bed=bed, dict=reference_dict),
        outputs=dict(interval_list=interval_list),
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def bedtointervallist(
    *,
    bed: str,
    reference_dict: str,
    interval_list: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert a BED file to Picard Interval List format using `picard BedToIntervalList`.

    Args:
        bed: Path to the input BED file (region file).
        reference_dict: Path to the genome dictionary file (e.g., from samtools dict or 
            picard CreateSequenceDictionary).
        interval_list: Path to the output interval list in Picard format.
        java_opts (optional): Additional Java options, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments for picard BedToIntervalList.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bedtointervallist(
        bed=bed,
        reference_dict=reference_dict,
        interval_list=interval_list,
        java_opts=java_opts,
        extra=extra,
         
    )
