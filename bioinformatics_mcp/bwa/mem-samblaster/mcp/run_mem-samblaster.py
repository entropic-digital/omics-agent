from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_mem_samblaster(
    *,
    reads: str,
    ref: str,
    out_bam: str,
    read_group: Optional[str] = None,
    genome_name: Optional[str] = None,
    num_cpu: int = 8,
     
) -> subprocess.CompletedProcess:
    """
    Map reads using bwa mem, mark duplicates by samblaster, and sort and index by sambamba.

    Args:
        reads: Path to input reads (FASTQ or similar).
        ref: Path to the reference genome file (FASTA format).
        out_bam: Path to the output BAM file.
        read_group (optional): Read group information in SAM format.
        genome_name (optional): Name of the genome being mapped.
        num_cpu: Number of CPUs to use (default is 8).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bwa/mem-samblaster",
        inputs=dict(reads=reads, ref=ref),
        outputs=dict(out_bam=out_bam),
        params={
            "read_group": read_group,
            "genome_name": genome_name,
            "num_cpu": num_cpu,
        },
         
    )


@collect_tool()
def mem_samblaster(
    *,
    reads: str,
    ref: str,
    out_bam: str,
    read_group: Optional[str] = None,
    genome_name: Optional[str] = None,
    num_cpu: int = 8,
     
) -> subprocess.CompletedProcess:
    """
    Map reads using bwa mem, mark duplicates by samblaster, and sort and index by sambamba.

    Args:
        reads: Path to input reads (FASTQ or similar).
        ref: Path to the reference genome file (FASTA format).
        out_bam: Path to the output BAM file.
        read_group (optional): Read group information in SAM format.
        genome_name (optional): Name of the genome being mapped.
        num_cpu: Number of CPUs to use (default is 8).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mem_samblaster(
        reads=reads,
        ref=ref,
        out_bam=out_bam,
        read_group=read_group,
        genome_name=genome_name,
        num_cpu=num_cpu,
         
    )
