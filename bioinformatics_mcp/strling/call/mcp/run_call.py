from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_call(
    *,
    input_bam: str,
    index_file: str,
    output_file: str,
    reference_genome: str,
    min_repeat_size: Optional[int] = None,
    threads: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    STRling 'call' subcommand to detect large short tandem repeat (STR) expansions from sequencing data.

    Args:
        input_bam: Path to the input BAM file.
        index_file: Path to the STRling index file.
        output_file: Path to the output genotype call file.
        reference_genome: Path to the reference genome file.
        min_repeat_size (optional): Minimum repeat size to consider (default: None).
        threads (optional): Number of threads to use (default: None).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/strling/call",
        inputs=dict(
            input_bam=input_bam,
            index_file=index_file,
        ),
        outputs=dict(
            output_file=output_file,
        ),
        params={
            "reference_genome": reference_genome,
            "min_repeat_size": min_repeat_size,
            "threads": threads,
        },
         
    )


@collect_tool()
def call(
    *,
    input_bam: str,
    index_file: str,
    output_file: str,
    reference_genome: str,
    min_repeat_size: Optional[int] = None,
    threads: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    STRling 'call' subcommand MCP tool to detect large STR expansions.

    Args:
        input_bam: Path to the input BAM file.
        index_file: Path to the STRling index file.
        output_file: Path to the output genotype call file.
        reference_genome: Path to the reference genome file.
        min_repeat_size (optional): Minimum repeat size to consider (default: None).
        threads (optional): Number of threads to use (default: None).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_call(
        input_bam=input_bam,
        index_file=index_file,
        output_file=output_file,
        reference_genome=reference_genome,
        min_repeat_size=min_repeat_size,
        threads=threads,
         
    )
