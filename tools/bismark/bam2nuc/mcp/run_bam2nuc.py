from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bam2nuc(
    *,
    genome_fa: str,
    bam: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate mono- and di-nucleotide coverage of the reads and compare them with average genomic sequence composition.

    Args:
        genome_fa: Path to genome in FastA format (e.g. *.fa, *.fasta, *.fa.gz, *.fasta.gz).
                   All genomes FastA from its parent folder will be taken.
        bam: Optional BAM or CRAM file (or multiple space-separated files). If this parameter isn't provided,
             the `--genomic_composition_only` option will be used to generate the genomic composition table
             `genomic_nucleotide_frequencies.txt`.
        extra: Any additional arguments to pass to the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {}
    if bam:
        params["bam"] = bam
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:tools/bismark/bam2nuc",
        inputs=dict(genome_fa=genome_fa),
        params=params,
         
    )


@collect_tool()
def bam2nuc(
    *,
    genome_fa: str,
    bam: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate mono- and di-nucleotide coverage of the reads and compare them with average genomic sequence composition.

    Args:
        genome_fa: Path to genome in FastA format (e.g. *.fa, *.fasta, *.fa.gz, *.fasta.gz).
                   All genomes FastA from its parent folder will be taken.
        bam: Optional BAM or CRAM file (or multiple space-separated files). If this parameter isn't provided,
             the `--genomic_composition_only` option will be used to generate the genomic composition table
             `genomic_nucleotide_frequencies.txt`.
        extra: Any additional arguments to pass to the tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bam2nuc(genome_fa=genome_fa, bam=bam, extra=extra,      )
