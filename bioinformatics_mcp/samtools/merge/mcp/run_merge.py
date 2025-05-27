from typing import List, Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_merge(
    *,
    input_bam_files: List[str],
    output_bam_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Merge two or more BAM files using samtools.

    Args:
        input_bam_files: List of BAM files to merge.
        output_bam_file: Path to the merged BAM file.
        extra (optional): Additional arguments for samtools that are not '-@/--threads', '--write-index', '-o', or '-O/--output-fmt'.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/samtools/merge",
        inputs={"input_bams": input_bam_files},
        outputs={"output_bam": output_bam_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def merge(
    *,
    input_bam_files: List[str],
    output_bam_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Merge two or more BAM files using samtools.

    Args:
        input_bam_files: List of BAM files to merge.
        output_bam_file: Path to the merged BAM file.
        extra (optional): Additional arguments for samtools that are not '-@/--threads', '--write-index', '-o', or '-O/--output-fmt'.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_merge(
        input_bam_files=input_bam_files,
        output_bam_file=output_bam_file,
        extra=extra,
         
    )
