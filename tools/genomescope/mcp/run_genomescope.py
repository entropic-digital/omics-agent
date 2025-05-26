from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_genomescope(
    *,
    kmer_histogram: str,
    inferred_genome_characteristics_and_plots: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Reference-free profiling of polyploid genomes using GenomeScope.

    Args:
        kmer_histogram: Path to the k-mer histogram input file.
        inferred_genome_characteristics_and_plots: Path to the directory where outputs (genome characteristics and plots) will be saved.
        extra (optional): Additional program arguments (e.g., mandatory kmer length `-k`/`--kmer_length`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/genomescope",
        inputs={"kmer_histogram": kmer_histogram},
        outputs={
            "inferred_genome_characteristics_and_plots": inferred_genome_characteristics_and_plots
        },
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def genomescope(
    *,
    kmer_histogram: str,
    inferred_genome_characteristics_and_plots: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Reference-free profiling of polyploid genomes using GenomeScope.

    Args:
        kmer_histogram: Path to the k-mer histogram input file.
        inferred_genome_characteristics_and_plots: Path to the directory where outputs (genome characteristics and plots) will be saved.
        extra (optional): Additional program arguments (e.g., mandatory kmer length `-k`/`--kmer_length`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_genomescope(
        kmer_histogram=kmer_histogram,
        inferred_genome_characteristics_and_plots=inferred_genome_characteristics_and_plots,
        extra=extra,
         
    )
