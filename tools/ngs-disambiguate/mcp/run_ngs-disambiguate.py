from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_ngs_disambiguate(
    *,
    species_a_bam: str,
    species_b_bam: str,
    ambiguous_species_a_bam: str,
    ambiguous_species_b_bam: str,
    unambiguous_species_a_bam: str,
    unambiguous_species_b_bam: str,
     
) -> subprocess.CompletedProcess:
    """
    Disambiguation algorithm for reads aligned to two species (e.g., human
    and mouse genomes) from Tophat, Hisat2, STAR, or BWA mem.

    Args:
        species_a_bam: Path to the BAM file for species A (name sorted).
        species_b_bam: Path to the BAM file for species B (name sorted).
        ambiguous_species_a_bam: Path to output BAM file with ambiguous alignments for species A.
        ambiguous_species_b_bam: Path to output BAM file with ambiguous alignments for species B.
        unambiguous_species_a_bam: Path to output BAM file with unambiguous alignments for species A.
        unambiguous_species_b_bam: Path to output BAM file with unambiguous alignments for species B.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/ngs-disambiguate",
        inputs=dict(
            species_a_bam=species_a_bam,
            species_b_bam=species_b_bam,
        ),
        outputs=dict(
            ambiguous_species_a_bam=ambiguous_species_a_bam,
            ambiguous_species_b_bam=ambiguous_species_b_bam,
            unambiguous_species_a_bam=unambiguous_species_a_bam,
            unambiguous_species_b_bam=unambiguous_species_b_bam,
        ),
         
    )


@collect_tool()
def ngs_disambiguate(
    *,
    species_a_bam: str,
    species_b_bam: str,
    ambiguous_species_a_bam: str,
    ambiguous_species_b_bam: str,
    unambiguous_species_a_bam: str,
    unambiguous_species_b_bam: str,
     
) -> subprocess.CompletedProcess:
    """
    Disambiguation algorithm for reads aligned to two species (e.g., human
    and mouse genomes) from Tophat, Hisat2, STAR, or BWA mem.

    Args:
        species_a_bam: Path to the BAM file for species A (name sorted).
        species_b_bam: Path to the BAM file for species B (name sorted).
        ambiguous_species_a_bam: Path to output BAM file with ambiguous alignments for species A.
        ambiguous_species_b_bam: Path to output BAM file with ambiguous alignments for species B.
        unambiguous_species_a_bam: Path to output BAM file with unambiguous alignments for species A.
        unambiguous_species_b_bam: Path to output BAM file with unambiguous alignments for species B.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_ngs_disambiguate(
        species_a_bam=species_a_bam,
        species_b_bam=species_b_bam,
        ambiguous_species_a_bam=ambiguous_species_a_bam,
        ambiguous_species_b_bam=ambiguous_species_b_bam,
        unambiguous_species_a_bam=unambiguous_species_a_bam,
        unambiguous_species_b_bam=unambiguous_species_b_bam,
         
    )
