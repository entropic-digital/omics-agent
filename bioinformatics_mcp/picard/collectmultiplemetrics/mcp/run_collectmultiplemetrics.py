from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_collectmultiplemetrics(
    *,
    bam_file: str,
    reference_fasta: str,
    output_prefix: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Executes the picard CollectMultipleMetrics tool.

    Args:
        bam_file: Path to the input BAM file (.bam).
        reference_fasta: Path to the reference FASTA sequence file (.fasta or .fa).
        output_prefix: Prefix for the output files.
        java_opts (optional): Additional arguments to pass to the Java compiler (e.g., `-XX:ParallelGCThreads=10`).
        extra (optional): Additional program arguments for picard.
  
    Returns:
        subprocess.CompletedProcess: Information about the completed Snakemake process.
    """
    params = {}
    if java_opts:
        params["java_opts"] = java_opts
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/picard/collectmultiplemetrics",
        inputs={"bam_file": bam_file, "reference_fasta": reference_fasta},
        outputs={"output_prefix": output_prefix},
        params=params,
         
    )


@collect_tool()
def collectmultiplemetrics(
    *,
    bam_file: str,
    reference_fasta: str,
    output_prefix: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Executes the picard CollectMultipleMetrics tool.

    Args:
        bam_file: Path to the input BAM file (.bam).
        reference_fasta: Path to the reference FASTA sequence file (.fasta or .fa).
        output_prefix: Prefix for the output files.
        java_opts (optional): Additional arguments to pass to the Java compiler (e.g., `-XX:ParallelGCThreads=10`).
        extra (optional): Additional program arguments for picard.
  
    Returns:
        subprocess.CompletedProcess: Information about the completed Snakemake process.
    """
    return run_collectmultiplemetrics(
        bam_file=bam_file,
        reference_fasta=reference_fasta,
        output_prefix=output_prefix,
        java_opts=java_opts,
        extra=extra,
         
    )
