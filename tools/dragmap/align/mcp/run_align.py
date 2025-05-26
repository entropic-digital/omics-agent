from typing import Optional, Union, List
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_align(
    *,
    reads: Union[str, List[str]],
    idx: str,
    output: str,
    extra: Optional[str] = None,
    sorting: Optional[str] = "none",
    sort_order: Optional[str] = None,
    sort_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads with Dragmap.

    Args:
        reads: Path to input FASTQ file(s).
        idx: Path to reference hash table.
        output: Path to output SAM/BAM/CRAM file.
        extra (optional): Additional parameters for Dragmap, excluding `--num-threads` and `-r`.
        sorting (optional): Sorting method, either `none`, `samtools`, or `picard`. Default is `none`.
        sort_order (optional): Sorting order, either `queryname` or `coordinate`. Ignored if sorting is `none`.
        sort_extra (optional): Additional parameters for samtools or picard.
  
    Returns:
        subprocess.CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/dragmap/align",
        inputs={"reads": reads, "idx": idx},
        outputs={"output": output},
        params={
            "extra": extra,
            "sorting": sorting,
            "sort_order": sort_order,
            "sort_extra": sort_extra,
        },
         
    )


@collect_tool()
def align(
    *,
    reads: Union[str, List[str]],
    idx: str,
    output: str,
    extra: Optional[str] = None,
    sorting: Optional[str] = "none",
    sort_order: Optional[str] = None,
    sort_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads with Dragmap.

    Args:
        reads: Path to input FASTQ file(s).
        idx: Path to reference hash table.
        output: Path to output SAM/BAM/CRAM file.
        extra (optional): Additional parameters for Dragmap, excluding `--num-threads` and `-r`.
        sorting (optional): Sorting method, either `none`, `samtools`, or `picard`. Default is `none`.
        sort_order (optional): Sorting order, either `queryname` or `coordinate`. Ignored if sorting is `none`.
        sort_extra (optional): Additional parameters for samtools or picard.
  
    Returns:
        subprocess.CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_align(
        reads=reads,
        idx=idx,
        output=output,
        extra=extra,
        sorting=sorting,
        sort_order=sort_order,
        sort_extra=sort_extra,
         
    )
