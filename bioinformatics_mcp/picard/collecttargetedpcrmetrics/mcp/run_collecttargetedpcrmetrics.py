from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_collecttargetedpcrmetrics(
    *,
    input_bam: str,
    reference_sequence: str,
    target_intervals: str,
    output_metrics: str,
    amplicon_intervals: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collect metric information for target PCR metrics runs, with Picard tools.

    Args:
        input_bam: Input BAM file containing aligned reads.
        reference_sequence: Reference sequence corresponding to the reads.
        target_intervals: Target intervals for PCR metrics.
        output_metrics: Output file for metrics in Picard format.
        amplicon_intervals (optional): Amplicon intervals for targeted PCR.
        java_opts (optional): Additional options to configure Java runtime.
        extra (optional): Additional Picard arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/picard/collecttargetedpcrmetrics",
        inputs={
            "input_bam": input_bam,
            "reference_sequence": reference_sequence,
            "target_intervals": target_intervals,
        },
        outputs={
            "output_metrics": output_metrics,
        },
        params={
            "amplicon_intervals": amplicon_intervals,
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def collecttargetedpcrmetrics(
    *,
    input_bam: str,
    reference_sequence: str,
    target_intervals: str,
    output_metrics: str,
    amplicon_intervals: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collect metric information for target PCR metrics runs, with Picard tools.

    Args:
        input_bam: Input BAM file containing aligned reads.
        reference_sequence: Reference sequence corresponding to the reads.
        target_intervals: Target intervals for PCR metrics.
        output_metrics: Output file for metrics in Picard format.
        amplicon_intervals (optional): Amplicon intervals for targeted PCR.
        java_opts (optional): Additional options to configure Java runtime.
        extra (optional): Additional Picard arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collecttargetedpcrmetrics(
        input_bam=input_bam,
        reference_sequence=reference_sequence,
        target_intervals=target_intervals,
        output_metrics=output_metrics,
        amplicon_intervals=amplicon_intervals,
        java_opts=java_opts,
        extra=extra,
         
    )
