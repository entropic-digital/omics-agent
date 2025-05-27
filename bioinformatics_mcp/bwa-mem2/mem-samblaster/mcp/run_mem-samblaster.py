from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_mem_samblaster(
    *,
    read1: str,
    read2: Optional[str] = None,
    output_bam: str,
    reference: str,
    bwa_params: Optional[str] = None,
    samblaster_params: Optional[str] = None,
    sambamba_sort_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads using bwa-mem2, mark duplicates by samblaster, and sort and index by sambamba.

    Args:
        read1: Path to the first read file (R1).
        read2 (optional): Path to the second read file (R2), if paired-end.
        output_bam: Path to the output BAM file.
        reference: Path to the reference genome.
        bwa_params (optional): Additional parameters for bwa-mem2.
        samblaster_params (optional): Additional parameters for samblaster.
        sambamba_sort_params (optional): Additional parameters for sambamba sort.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "read1": read1,
        "output_bam": output_bam,
        "reference": reference,
    }
    if read2:
        inputs["read2"] = read2

    params = {}
    if bwa_params:
        params["bwa_params"] = bwa_params
    if samblaster_params:
        params["samblaster_params"] = samblaster_params
    if sambamba_sort_params:
        params["sambamba_sort_params"] = sambamba_sort_params

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bwa-mem2/mem-samblaster",
        inputs=inputs,
        params=params,
         
    )


@collect_tool()
def mem_samblaster(
    *,
    read1: str,
    read2: Optional[str] = None,
    output_bam: str,
    reference: str,
    bwa_params: Optional[str] = None,
    samblaster_params: Optional[str] = None,
    sambamba_sort_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads using bwa-mem2, mark duplicates by samblaster, and sort and index by sambamba.

    Args:
        read1: Path to the first read file (R1).
        read2 (optional): Path to the second read file (R2), if paired-end.
        output_bam: Path to the output BAM file.
        reference: Path to the reference genome.
        bwa_params (optional): Additional parameters for bwa-mem2.
        samblaster_params (optional): Additional parameters for samblaster.
        sambamba_sort_params (optional): Additional parameters for sambamba sort.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mem_samblaster(
        read1=read1,
        read2=read2,
        output_bam=output_bam,
        reference=reference,
        bwa_params=bwa_params,
        samblaster_params=samblaster_params,
        sambamba_sort_params=sambamba_sort_params,
         
    )
