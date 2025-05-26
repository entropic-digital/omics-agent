from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_preprocess_variants(
    *,
    reference_genome: str,
    read_alignments: str,
    varlociraptor_alignment_properties: str,
    candidate_variants: str,
    preprocessed_variants: str,
     
) -> subprocess.CompletedProcess:
    """
    Preprocess candidate variants for variant calling with Varlociraptor.

    Args:
        reference_genome: Path to the reference genome file.
        read_alignments: Path to the read alignments file.
        varlociraptor_alignment_properties: Path to the Varlociraptor alignment properties file.
        candidate_variants: Path to the candidate variants file.
        preprocessed_variants: Path to the output preprocessed variants file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/varlociraptor/preprocess-variants",
        inputs=dict(
            reference_genome=reference_genome,
            read_alignments=read_alignments,
            varlociraptor_alignment_properties=varlociraptor_alignment_properties,
            candidate_variants=candidate_variants,
        ),
        outputs=dict(preprocessed_variants=preprocessed_variants),
         
    )


@collect_tool()
def preprocess_variants(
    *,
    reference_genome: str,
    read_alignments: str,
    varlociraptor_alignment_properties: str,
    candidate_variants: str,
    preprocessed_variants: str,
     
) -> subprocess.CompletedProcess:
    """
    Preprocess candidate variants for variant calling with Varlociraptor.

    Args:
        reference_genome: Path to the reference genome file.
        read_alignments: Path to the read alignments file.
        varlociraptor_alignment_properties: Path to the Varlociraptor alignment properties file.
        candidate_variants: Path to the candidate variants file.
        preprocessed_variants: Path to the output preprocessed variants file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_preprocess_variants(
        reference_genome=reference_genome,
        read_alignments=read_alignments,
        varlociraptor_alignment_properties=varlociraptor_alignment_properties,
        candidate_variants=candidate_variants,
        preprocessed_variants=preprocessed_variants,
         
    )
