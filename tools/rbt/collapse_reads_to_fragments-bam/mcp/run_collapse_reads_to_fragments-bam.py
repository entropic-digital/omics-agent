from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_collapse_reads_to_fragments_bam(
    *,
    input_bam: str,
    output_bam: str,
    read_group: str,
    filter_mismatching_ids: Optional[bool] = False,
    min_mapq: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate consensus reads from read groups marked by PicardTools MarkDuplicates or UmiAwareMarkDuplicatesWithMateCigar.

    Args:
        input_bam (str): Path to the input BAM file.
        output_bam (str): Path to the output BAM file.
        read_group (str): The read group to base the collapse operation on.
        filter_mismatching_ids (bool, optional): Set to True to filter out mismatching IDs. Defaults to False.
        min_mapq (int, optional): Minimum mapping quality for reads to be processed. Defaults to None.
  
    Returns:
        subprocess.CompletedProcess: CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "read_group": read_group,
        "filter_mismatching_ids": filter_mismatching_ids,
    }
    if min_mapq is not None:
        params["min_mapq"] = min_mapq

    return run_snake_wrapper(
        wrapper="file:tools/rbt/collapse_reads_to_fragments-bam",
        inputs={"input_bam": input_bam},
        outputs={"output_bam": output_bam},
        params=params,
         
    )


@collect_tool()
def collapse_reads_to_fragments_bam(
    *,
    input_bam: str,
    output_bam: str,
    read_group: str,
    filter_mismatching_ids: Optional[bool] = False,
    min_mapq: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate consensus reads from read groups marked by PicardTools MarkDuplicates or UmiAwareMarkDuplicatesWithMateCigar.

    Args:
        input_bam (str): Path to the input BAM file.
        output_bam (str): Path to the output BAM file.
        read_group (str): The read group to base the collapse operation on.
        filter_mismatching_ids (bool, optional): Set to True to filter out mismatching IDs. Defaults to False.
        min_mapq (int, optional): Minimum mapping quality for reads to be processed. Defaults to None.
  
    Returns:
        subprocess.CompletedProcess: CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collapse_reads_to_fragments_bam(
        input_bam=input_bam,
        output_bam=output_bam,
        read_group=read_group,
        filter_mismatching_ids=filter_mismatching_ids,
        min_mapq=min_mapq,
         
    )
