from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_mem(
    *,
    bwa: str,
    reads: str,
    index: str,
    output_bam: str,
    threads: int = 1,
    read_group: Optional[str] = None,
    extra_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the bwa-memx tool for sequence alignment.

    Args:
        bwa: Specify which alignment to use: 'bwa-mem', 'bwa-mem2', or 'bwa-meme'.
        reads: Input reads in FASTQ or BAM format for alignment.
        index: Input index corresponding to the selected alignment tool.
        output_bam: Output BAM file path for alignment results.
        threads (optional): Number of threads to use for alignment. Default is 1.
        read_group (optional): Read group information to include in the alignment.
        extra_params (optional): Additional parameters to pass to the alignment tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bwa-memx/mem",
        inputs=dict(reads=reads, index=index),
        outputs=dict(output_bam=output_bam),
        params={
            "bwa": bwa,
            "threads": threads,
            "read_group": read_group,
            "extra_params": extra_params,
        },
         
    )


@collect_tool()
def mem(
    *,
    bwa: str,
    reads: str,
    index: str,
    output_bam: str,
    threads: int = 1,
    read_group: Optional[str] = None,
    extra_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Perform sequence alignment using bwa-mem, bwa-mem2, or bwa-meme.

    Args:
        bwa: Specify which alignment to use: 'bwa-mem', 'bwa-mem2', or 'bwa-meme'.
        reads: Input reads in FASTQ or BAM format for alignment.
        index: Input index corresponding to the selected alignment tool.
        output_bam: Output BAM file path for alignment results.
        threads (optional): Number of threads to use for alignment. Default is 1.
        read_group (optional): Read group information to include in the alignment.
        extra_params (optional): Additional parameters to pass to the alignment tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mem(
        bwa=bwa,
        reads=reads,
        index=index,
        output_bam=output_bam,
        threads=threads,
        read_group=read_group,
        extra_params=extra_params,
         
    )
