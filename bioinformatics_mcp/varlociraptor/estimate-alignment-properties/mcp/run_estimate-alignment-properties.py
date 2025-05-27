from typing import List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_estimate_alignment_properties(
    *,
    reference_genome: str,
    read_alignments: List[str],
    alignment_properties: str,
     
) -> subprocess.CompletedProcess:
    """
    Estimate alignment properties for variant calling with varlociraptor.

    Args:
        reference_genome: Path to the reference genome file.
        read_alignments: List of paths to read alignment files (BAMs).
        alignment_properties: Path to save the varlociraptor alignment properties.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/varlociraptor/estimate-alignment-properties",
        inputs=dict(
            reference_genome=reference_genome,
            read_alignments=read_alignments,
        ),
        outputs=dict(
            alignment_properties=alignment_properties,
        ),
         
    )


@collect_tool()
def estimate_alignment_properties(
    *,
    reference_genome: str,
    read_alignments: List[str],
    alignment_properties: str,
     
) -> subprocess.CompletedProcess:
    """
    Estimate alignment properties for variant calling with varlociraptor.

    Args:
        reference_genome: Path to the reference genome file.
        read_alignments: List of paths to read alignment files (BAMs).
        alignment_properties: Path to save the varlociraptor alignment properties.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_estimate_alignment_properties(
        reference_genome=reference_genome,
        read_alignments=read_alignments,
        alignment_properties=alignment_properties,
         
    )
