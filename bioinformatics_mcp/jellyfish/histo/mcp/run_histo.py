from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_histo(
    *,
    kmer_count_jf_file: str,
    kmer_histogram_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Export histogram of kmer counts.

    Args:
        kmer_count_jf_file: Path to the kmer count jf file.
        kmer_histogram_file: Path to the output kmer histogram file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/jellyfish/histo",
        inputs={"kmer_count_jf_file": kmer_count_jf_file},
        outputs={"kmer_histogram_file": kmer_histogram_file},
         
    )


@collect_tool()
def jellyfish_histo(
    *,
    kmer_count_jf_file: str,
    kmer_histogram_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Export histogram of kmer counts.

    Args:
        kmer_count_jf_file: Path to the kmer count jf file.
        kmer_histogram_file: Path to the output kmer histogram file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_histo(
        kmer_count_jf_file=kmer_count_jf_file,
        kmer_histogram_file=kmer_histogram_file,
         
    )
