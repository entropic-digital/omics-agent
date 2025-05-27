from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_mosdepth(
    *,
    bam_or_cram: str,
    output_prefix: str,
    reference_genome: Optional[str] = None,
    bed_file: Optional[str] = None,
    by: Optional[int] = None,
    threshold: Optional[str] = None,
    precision: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Runs the mosdepth tool for fast BAM/CRAM depth calculation.

    Args:
        bam_or_cram: Path to the input BAM or CRAM file.
        output_prefix: Prefix for the output coverage summary files.
        reference_genome (optional): Path to the reference genome.
        bed_file (optional): Path to the BED file.
        by (optional): Window size for intervals (incompatible with input BED).
        threshold (optional): Comma-separated integers for threshold coverage values.
        precision (optional): Precision for floating-point outputs.
        extra (optional): Additional command-line arguments for mosdepth.
  
    Returns:
        subprocess.CompletedProcess: Result of the completed Snakemake process.
    """
    inputs = {
        "bam_or_cram": bam_or_cram,
    }
    if reference_genome:
        inputs["reference_genome"] = reference_genome
    if bed_file:
        inputs["bed_file"] = bed_file

    params = {}
    if by:
        params["by"] = by
    if threshold:
        params["threshold"] = threshold
    if precision:
        params["precision"] = precision
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/mosdepth",
        inputs=inputs,
        params=params,
        outputs={"output_prefix": output_prefix},
         
    )


@collect_tool()
def mosdepth(
    *,
    bam_or_cram: str,
    output_prefix: str,
    reference_genome: Optional[str] = None,
    bed_file: Optional[str] = None,
    by: Optional[int] = None,
    threshold: Optional[str] = None,
    precision: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Executes the mosdepth tool for BAM/CRAM depth calculation.

    Args:
        bam_or_cram: Path to the input BAM or CRAM file.
        output_prefix: Prefix for the output coverage summary files.
        reference_genome (optional): Path to the reference genome.
        bed_file (optional): Path to the BED file.
        by (optional): Window size for intervals (incompatible with input BED).
        threshold (optional): Comma-separated integers for threshold coverage values.
        precision (optional): Precision for floating-point outputs.
        extra (optional): Additional command-line arguments for mosdepth.
  
    Returns:
        subprocess.CompletedProcess: Result of the completed Snakemake process.
    """
    return run_mosdepth(
        bam_or_cram=bam_or_cram,
        output_prefix=output_prefix,
        reference_genome=reference_genome,
        bed_file=bed_file,
        by=by,
        threshold=threshold,
        precision=precision,
        extra=extra,
         
    )
