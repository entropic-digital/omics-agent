from typing import List, Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_trinity(
    *,
    fastq_files: List[str],
    fas: str,
    map: str,
    dir: str,
     
) -> subprocess.CompletedProcess:
    """
    Generate transcriptome assembly with Trinity.

    Args:
        fastq_files: List of FASTQ file paths for the input sequencing reads.
        fas: Output path for the assembled fasta file.
        map: Output path for the gene-transcripts map file.
        dir: Output directory to store intermediate results.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/trinity",
        inputs=dict(fastq_files=fastq_files),
        outputs=dict(fas=fas, map=map, dir=dir),
         
    )


@collect_tool()
def trinity(
    *,
    fastq_files: List[str],
    fas: str,
    map: str,
    dir: str,
     
) -> subprocess.CompletedProcess:
    """
    Generate transcriptome assembly with Trinity.

    Args:
        fastq_files: List of FASTQ file paths for the input sequencing reads.
        fas: Output path for the assembled fasta file.
        map: Output path for the gene-transcripts map file.
        dir: Output directory to store intermediate results.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_trinity(
        fastq_files=fastq_files,
        fas=fas,
        map=map,
        dir=dir,
         
    )
