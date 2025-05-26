from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_single_cell_bulk(
    *,
    single_cell_bam: str,
    single_cell_bam_index: str,
    bulk_bam: str,
    bulk_bam_index: str,
    reference_genome: str,
    reference_genome_index: str,
    candidate_sites: str,
    output_bcf: str,
     
) -> subprocess.CompletedProcess:
    """
    ProSolo: Call variants or other events in a single cell sample against a bulk background sample.

    Args:
        single_cell_bam: Path to the position-sorted single cell BAM file.
        single_cell_bam_index: Path to the index file for the single cell BAM file.
        bulk_bam: Path to the position-sorted bulk BAM file.
        bulk_bam_index: Path to the index file for the bulk BAM file.
        reference_genome: Path to the reference genome in FASTA format.
        reference_genome_index: Path to the index file for the reference genome.
        candidate_sites: Path to the VCF or BCF file specifying candidate sites for calling.
        output_bcf: Path to the output BCF file with called variants and probabilities.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/prosolo/single-cell-bulk",
        inputs=dict(
            single_cell_bam=single_cell_bam,
            single_cell_bam_index=single_cell_bam_index,
            bulk_bam=bulk_bam,
            bulk_bam_index=bulk_bam_index,
            reference_genome=reference_genome,
            reference_genome_index=reference_genome_index,
            candidate_sites=candidate_sites,
        ),
        outputs=dict(output_bcf=output_bcf),
         
    )


@collect_tool()
def single_cell_bulk(
    *,
    single_cell_bam: str,
    single_cell_bam_index: str,
    bulk_bam: str,
    bulk_bam_index: str,
    reference_genome: str,
    reference_genome_index: str,
    candidate_sites: str,
    output_bcf: str,
     
) -> subprocess.CompletedProcess:
    """
    ProSolo: Call variants or other events in a single cell sample against a bulk background sample.

    Args:
        single_cell_bam: Path to the position-sorted single cell BAM file.
        single_cell_bam_index: Path to the index file for the single cell BAM file.
        bulk_bam: Path to the position-sorted bulk BAM file.
        bulk_bam_index: Path to the index file for the bulk BAM file.
        reference_genome: Path to the reference genome in FASTA format.
        reference_genome_index: Path to the index file for the reference genome.
        candidate_sites: Path to the VCF or BCF file specifying candidate sites for calling.
        output_bcf: Path to the output BCF file with called variants and probabilities.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_single_cell_bulk(
        single_cell_bam=single_cell_bam,
        single_cell_bam_index=single_cell_bam_index,
        bulk_bam=bulk_bam,
        bulk_bam_index=bulk_bam_index,
        reference_genome=reference_genome,
        reference_genome_index=reference_genome_index,
        candidate_sites=candidate_sites,
        output_bcf=output_bcf,
         
    )
