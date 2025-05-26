from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_denoisereadcounts(
    *,
    hdf5: str,
    std_copy_ratio: str,
    denoised_copy_ratio: str,
    pon: Optional[str] = None,
    gc_interval: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Denoises read counts to produce denoised copy ratios.

    Args:
        hdf5: TSV or HDF5 file with counts from CollectReadCounts.
        std_copy_ratio: Path to output file for standardized-copy-ratios.
        denoised_copy_ratio: Path to output file for denoised-copy-ratios.
        pon (optional): Panel-of-normals file from CreateReadCountPanelOfNormals.
        gc_interval (optional): GC-content annotated intervals from AnnotateIntervals.
        java_opts (optional): Additional Java compiler arguments, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/denoisereadcounts",
        inputs=dict(hdf5=hdf5),
        outputs=dict(
            std_copy_ratio=std_copy_ratio, denoised_copy_ratio=denoised_copy_ratio
        ),
        params={
            "pon": pon,
            "gc_interval": gc_interval,
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def denoisereadcounts(
    *,
    hdf5: str,
    std_copy_ratio: str,
    denoised_copy_ratio: str,
    pon: Optional[str] = None,
    gc_interval: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Denoises read counts to produce denoised copy ratios.

    Args:
        hdf5: TSV or HDF5 file with counts from CollectReadCounts.
        std_copy_ratio: Path to output file for standardized-copy-ratios.
        denoised_copy_ratio: Path to output file for denoised-copy-ratios.
        pon (optional): Panel-of-normals file from CreateReadCountPanelOfNormals.
        gc_interval (optional): GC-content annotated intervals from AnnotateIntervals.
        java_opts (optional): Additional Java compiler arguments, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_denoisereadcounts(
        hdf5=hdf5,
        std_copy_ratio=std_copy_ratio,
        denoised_copy_ratio=denoised_copy_ratio,
        pon=pon,
        gc_interval=gc_interval,
        java_opts=java_opts,
        extra=extra,
         
    )
