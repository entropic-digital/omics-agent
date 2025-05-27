from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_sampe(
    *,
    input_aln_sa: str,
    input_aln_sb: str,
    input_reads_a: str,
    input_reads_b: str,
    input_reference: str,
    output_sam: str,
    read_group_str: Optional[str] = None,
    num_threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Map paired-end reads with BWA sampe.

    Args:
        input_aln_sa: Path to the first paired-end alignment file (SA).
        input_aln_sb: Path to the second paired-end alignment file (SB).
        input_reads_a: Path to the first paired-end reads file (read A).
        input_reads_b: Path to the second paired-end reads file (read B).
        input_reference: Path to the reference genome index file.
        output_sam: Path to the output SAM file.
        read_group_str (optional): Read group string to include in the SAM header.
        num_threads (optional): Number of threads to use for processing. Default is 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bwa/sampe",
        inputs={
            "aln_sa": input_aln_sa,
            "aln_sb": input_aln_sb,
            "reads_a": input_reads_a,
            "reads_b": input_reads_b,
            "reference": input_reference,
        },
        outputs={"sam": output_sam},
        params={
            "read_group_str": read_group_str,
            "num_threads": num_threads,
        },
         
    )


@collect_tool()
def sampe(
    *,
    input_aln_sa: str,
    input_aln_sb: str,
    input_reads_a: str,
    input_reads_b: str,
    input_reference: str,
    output_sam: str,
    read_group_str: Optional[str] = None,
    num_threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Map paired-end reads with BWA sampe.

    Args:
        input_aln_sa: Path to the first paired-end alignment file (SA).
        input_aln_sb: Path to the second paired-end alignment file (SB).
        input_reads_a: Path to the first paired-end reads file (read A).
        input_reads_b: Path to the second paired-end reads file (read B).
        input_reference: Path to the reference genome index file.
        output_sam: Path to the output SAM file.
        read_group_str (optional): Read group string to include in the SAM header.
        num_threads (optional): Number of threads to use for processing. Default is 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_sampe(
        input_aln_sa=input_aln_sa,
        input_aln_sb=input_aln_sb,
        input_reads_a=input_reads_a,
        input_reads_b=input_reads_b,
        input_reference=input_reference,
        output_sam=output_sam,
        read_group_str=read_group_str,
        num_threads=num_threads,
         
    )
