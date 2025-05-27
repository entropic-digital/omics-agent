from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_align(
    *,
    input_reads: str,
    reference_genome: str,
    output_bam: str,
    preset: Optional[str] = None,
    sort: bool = True,
     
) -> subprocess.CompletedProcess:
    """
    Align reads using pbmm2, a minimap2 SMRT wrapper for PacBio data.

    Args:
        input_reads: Path to input reads file.
        reference_genome: Path to reference genome file.
        output_bam: Path to output BAM file.
        preset (optional): Preset options for pbmm2 alignment. Valid presets are map-pb, map-hifi, map-hifi-no_trim.
        sort (optional): Whether or not to sort the output BAM file. Defaults to True.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {"preset": preset, "sort": sort} if preset else {"sort": sort}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/pbmm2/align",
        inputs={
            "input_reads": input_reads,
            "reference_genome": reference_genome,
        },
        outputs={
            "output_bam": output_bam,
        },
        params=params,
         
    )


@collect_tool()
def align(
    *,
    input_reads: str,
    reference_genome: str,
    output_bam: str,
    preset: Optional[str] = None,
    sort: bool = True,
     
) -> subprocess.CompletedProcess:
    """
    Align reads using pbmm2, a minimap2 SMRT wrapper for PacBio data.

    Args:
        input_reads: Path to input reads file.
        reference_genome: Path to reference genome file.
        output_bam: Path to output BAM file.
        preset (optional): Preset options for pbmm2 alignment. Valid presets are map-pb, map-hifi, map-hifi-no_trim.
        sort (optional): Whether or not to sort the output BAM file. Defaults to True.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_align(
        input_reads=input_reads,
        reference_genome=reference_genome,
        output_bam=output_bam,
        preset=preset,
        sort=sort,
         
    )
