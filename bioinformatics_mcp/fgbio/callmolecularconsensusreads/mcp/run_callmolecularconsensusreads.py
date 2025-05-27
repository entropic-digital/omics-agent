from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_callmolecularconsensusreads(
    *,
    input_bam: str,
    output_bam: str,
    umi_tag: str,
    family_size: Optional[int] = None,
    min_base_quality: Optional[int] = None,
    max_base_error_rate: Optional[float] = None,
    reject_bam: Optional[str] = None,
    output_stats: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calls consensus sequences from reads with the same unique molecular tag.

    Args:
        input_bam: Path to the input BAM file.
        output_bam: Path to the output BAM file with consensus reads.
        umi_tag: The name of the BAM tag that contains the UMI.
        family_size (optional): Minimum family size required to form a consensus.
        min_base_quality (optional): Minimum base quality required to consider base in consensus.
        max_base_error_rate (optional): Maximum base error rate allowed in base consensus calculation.
        reject_bam (optional): Path to an optional BAM file for rejected reads.
        output_stats (optional): Path to an optional stats file for additional output information.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "umi_tag": umi_tag,
        "family_size": family_size,
        "min_base_quality": min_base_quality,
        "max_base_error_rate": max_base_error_rate,
        "reject_bam": reject_bam,
        "output_stats": output_stats,
    }
    # Remove None values from params
    params = {key: value for key, value in params.items() if value is not None}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/fgbio/callmolecularconsensusreads",
        inputs=dict(input_bam=input_bam),
        outputs=dict(output_bam=output_bam),
        params=params,
         
    )


@collect_tool()
def callmolecularconsensusreads(
    *,
    input_bam: str,
    output_bam: str,
    umi_tag: str,
    family_size: Optional[int] = None,
    min_base_quality: Optional[int] = None,
    max_base_error_rate: Optional[float] = None,
    reject_bam: Optional[str] = None,
    output_stats: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calls consensus sequences from reads with the same unique molecular tag.

    Args:
        input_bam: Path to the input BAM file.
        output_bam: Path to the output BAM file with consensus reads.
        umi_tag: The name of the BAM tag that contains the UMI.
        family_size (optional): Minimum family size required to form a consensus.
        min_base_quality (optional): Minimum base quality required to consider base in consensus.
        max_base_error_rate (optional): Maximum base error rate allowed in base consensus calculation.
        reject_bam (optional): Path to an optional BAM file for rejected reads.
        output_stats (optional): Path to an optional stats file for additional output information.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_callmolecularconsensusreads(
        input_bam=input_bam,
        output_bam=output_bam,
        umi_tag=umi_tag,
        family_size=family_size,
        min_base_quality=min_base_quality,
        max_base_error_rate=max_base_error_rate,
        reject_bam=reject_bam,
        output_stats=output_stats,
         
    )
