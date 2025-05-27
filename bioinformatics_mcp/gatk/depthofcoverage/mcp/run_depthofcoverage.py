from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_depthofcoverage(
    *,
    bam_file: str,
    intervals: List[str],
    reference_genome: str,
    output_base: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk DepthOfCoverage (BETA).

    Args:
        bam_file: Path to the BAM file to be analyzed for coverage statistics.
        intervals: One or more genomic intervals over which to operate.
        reference_genome: Path to the reference genome.
        output_base: Base file location to which to write coverage summary information.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/depthofcoverage",
        inputs=dict(
            bam_file=bam_file,
            intervals=intervals,
            reference_genome=reference_genome,
        ),
        outputs=dict(output_base=output_base),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def depthofcoverage(
    *,
    bam_file: str,
    intervals: List[str],
    reference_genome: str,
    output_base: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk DepthOfCoverage (BETA).

    Args:
        bam_file: Path to the BAM file to be analyzed for coverage statistics.
        intervals: One or more genomic intervals over which to operate.
        reference_genome: Path to the reference genome.
        output_base: Base file location to which to write coverage summary information.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_depthofcoverage(
        bam_file=bam_file,
        intervals=intervals,
        reference_genome=reference_genome,
        output_base=output_base,
        extra=extra,
         
    )
