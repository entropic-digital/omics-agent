from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_sim(
    *,
    xg_index: str,
    output_reads: str,
    gam_input: Optional[str] = None,
    gbwt_index: Optional[str] = None,
    seed: Optional[int] = None,
    num_reads: Optional[int] = None,
    max_mem: Optional[str] = None,
    sampling_algorithm: Optional[str] = None,
    sample_name: Optional[str] = None,
    fasta_output: Optional[bool] = False,
     
) -> subprocess.CompletedProcess:
    """
    Samples sequences from the xg-indexed graph.

    Args:
        xg_index: Path to the xg index file.
        output_reads: Path to the output file where sampled reads will be written.
        gam_input (optional): Path to an optional gam file with alignments.
        gbwt_index (optional): Path to the GBWT index file.
        seed (optional): Seed for random sampling.
        num_reads (optional): Number of reads to sample.
        max_mem (optional): Maximum memory for read simulation.
        sampling_algorithm (optional): Sampling algorithm to use.
        sample_name (optional): Name for the sample.
        fasta_output (optional): Whether to output reads in FASTA format.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/vg/sim",
        inputs=dict(
            xg_index=xg_index,
            gam_input=gam_input,
            gbwt_index=gbwt_index,
        ),
        outputs=dict(output_reads=output_reads),
        params={
            "seed": seed,
            "num_reads": num_reads,
            "max_mem": max_mem,
            "sampling_algorithm": sampling_algorithm,
            "sample_name": sample_name,
            "fasta_output": fasta_output,
        },
         
    )


@collect_tool()
def sim(
    *,
    xg_index: str,
    output_reads: str,
    gam_input: Optional[str] = None,
    gbwt_index: Optional[str] = None,
    seed: Optional[int] = None,
    num_reads: Optional[int] = None,
    max_mem: Optional[str] = None,
    sampling_algorithm: Optional[str] = None,
    sample_name: Optional[str] = None,
    fasta_output: Optional[bool] = False,
     
) -> subprocess.CompletedProcess:
    """
    Samples sequences from the xg-indexed graph.

    Args:
        xg_index: Path to the xg index file.
        output_reads: Path to the output file where sampled reads will be written.
        gam_input (optional): Path to an optional gam file with alignments.
        gbwt_index (optional): Path to the GBWT index file.
        seed (optional): Seed for random sampling.
        num_reads (optional): Number of reads to sample.
        max_mem (optional): Maximum memory for read simulation.
        sampling_algorithm (optional): Sampling algorithm to use.
        sample_name (optional): Name for the sample.
        fasta_output (optional): Whether to output reads in FASTA format.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_sim(
        xg_index=xg_index,
        output_reads=output_reads,
        gam_input=gam_input,
        gbwt_index=gbwt_index,
        seed=seed,
        num_reads=num_reads,
        max_mem=max_mem,
        sampling_algorithm=sampling_algorithm,
        sample_name=sample_name,
        fasta_output=fasta_output,
         
    )
