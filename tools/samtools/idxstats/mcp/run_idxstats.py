from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_idxstats(
    *,
    input_file: str,
    index_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Use samtools to retrieve and print stats from indexed BAM, SAM, or CRAM files.

    Args:
        input_file: Path to the indexed SAM, BAM, or CRAM file (.SAM, .BAM, .CRAM).
        index_file: Path to the corresponding index file.
        output_file: Path to the idxstat output file (.idxstats).
        extra (optional): Additional program arguments (not `-@/--threads`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/samtools/idxstats",
        inputs={"input_file": input_file, "index_file": index_file},
        params={"extra": extra} if extra else {},
        outputs={"output_file": output_file},
         
    )


@collect_tool()
def idxstats(
    *,
    input_file: str,
    index_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Use samtools to retrieve and print stats from indexed BAM, SAM, or CRAM files.

    Args:
        input_file: Path to the indexed SAM, BAM, or CRAM file (.SAM, .BAM, .CRAM).
        index_file: Path to the corresponding index file.
        output_file: Path to the idxstat output file (.idxstats).
        extra (optional): Additional program arguments (not `-@/--threads`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_idxstats(
        input_file=input_file,
        index_file=index_file,
        output_file=output_file,
        extra=extra,
         
    )
