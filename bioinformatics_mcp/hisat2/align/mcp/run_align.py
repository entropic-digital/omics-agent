from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_align(
    *,
    reads: List[str],
    idx: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads with hisat2.

    Args:
        reads: Either 1 or 2 FASTQ files with reads.
        idx: Path to the index files.
        output: BAM file with mapped reads.
        extra (optional): Additional parameters for hisat2.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/hisat2/align",
        inputs={"reads": reads, "idx": idx},
        outputs={"output": output},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def align(
    *,
    reads: List[str],
    idx: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads with hisat2.

    Args:
        reads: Either 1 or 2 FASTQ files with reads.
        idx: Path to the index files.
        output: BAM file with mapped reads.
        extra (optional): Additional parameters for hisat2.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_align(reads=reads, idx=idx, output=output, extra=extra,      )
