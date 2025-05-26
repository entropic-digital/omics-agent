from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_modelsegments(
    *,
    denoised_copy_ratios: Optional[str] = None,
    allelic_counts: Optional[str] = None,
    normal_allelic_counts: Optional[str] = None,
    segments: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Models segmented copy ratios from denoised copy ratios and segmented minor-allele fractions from allelic counts.

    Args:
        denoised_copy_ratios (optional): Path to the denoised_copy_ratios file.
        allelic_counts (optional): Path to the allelic_counts file.
        normal_allelic_counts (optional): Path to the matched_normal allelic-counts file.
        segments (optional): Path to the Picard interval-list file containing a multisample segmentation.
        java_opts (optional): Additional arguments to be passed to the Java compiler.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "denoised_copy_ratios": denoised_copy_ratios,
        "allelic_counts": allelic_counts,
        "normal_allelic_counts": normal_allelic_counts,
        "segments": segments,
    }
    params = {
        "java_opts": java_opts,
        "extra": extra,
    }

    return run_snake_wrapper(
        wrapper="file:tools/gatk/modelsegments",
        inputs={key: value for key, value in inputs.items() if value is not None},
        params={key: value for key, value in params.items() if value is not None},
         
    )


@collect_tool()
def modelsegments(
    *,
    denoised_copy_ratios: Optional[str] = None,
    allelic_counts: Optional[str] = None,
    normal_allelic_counts: Optional[str] = None,
    segments: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GATK ModelSegments tool for modeling segmented copy ratios and minor-allele fractions.

    Args:
        denoised_copy_ratios (optional): Path to the denoised_copy_ratios file.
        allelic_counts (optional): Path to the allelic_counts file.
        normal_allelic_counts (optional): Path to the matched_normal allelic-counts file.
        segments (optional): Path to the Picard interval-list file containing a multisample segmentation.
        java_opts (optional): Additional arguments to be passed to the Java compiler.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_modelsegments(
        denoised_copy_ratios=denoised_copy_ratios,
        allelic_counts=allelic_counts,
        normal_allelic_counts=normal_allelic_counts,
        segments=segments,
        java_opts=java_opts,
        extra=extra,
         
    )
