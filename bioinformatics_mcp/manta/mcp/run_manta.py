from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_manta(
    *,
    bam_files: List[str],
    reference_genome: str,
    bed_file: Optional[str] = None,
    extra_cfg: Optional[str] = None,
    extra_run: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call structural variants with manta.

    Args:
        bam_files: List of BAM/CRAM file paths to be analyzed.
        reference_genome: Path to the reference genome.
        bed_file (optional): Path to a BED file for targeted analysis.
        extra_cfg (optional): Additional arguments for `configManta.py`.
        extra_run (optional): Additional arguments for `runWorkflow.py`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/manta",
        inputs=dict(
            bam_files=bam_files, reference_genome=reference_genome, bed_file=bed_file
        ),
        params={
            "extra_cfg": extra_cfg,
            "extra_run": extra_run,
        },
         
    )


@collect_tool()
def manta(
    *,
    bam_files: List[str],
    reference_genome: str,
    bed_file: Optional[str] = None,
    extra_cfg: Optional[str] = None,
    extra_run: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call structural variants with manta.

    Args:
        bam_files: List of BAM/CRAM file paths to be analyzed.
        reference_genome: Path to the reference genome.
        bed_file (optional): Path to a BED file for targeted analysis.
        extra_cfg (optional): Additional arguments for `configManta.py`.
        extra_run (optional): Additional arguments for `runWorkflow.py`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_manta(
        bam_files=bam_files,
        reference_genome=reference_genome,
        bed_file=bed_file,
        extra_cfg=extra_cfg,
        extra_run=extra_run,
         
    )
