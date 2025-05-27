from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_setmateinformation(
    *,
    input_bam: str,
    output_bam: str,
    compression: Optional[int] = None,
    threads: Optional[int] = 1,
    java_opts: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Adds and/or fixes mate information on paired-end reads. Sets the MQ (mate mapping quality), MC (mate cigar string), ensures all mate-related
    flag fields are set correctly, and that the mate reference and mate start position are correct.

    Args:
        input_bam: Path to the input BAM file.
        output_bam: Path to the output BAM file.
        compression (optional): Compression level for the BAM file (0-9). Defaults to None.
        threads (optional): Number of threads to use. Defaults to 1.
        java_opts (optional): Additional Java options to use for the tool. Defaults to None.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "compression": compression,
        "threads": threads,
        "java_opts": java_opts,
    }

    # Filter out None values from parameters
    params = {k: v for k, v in params.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/fgbio/setmateinformation",
        inputs=dict(input_bam=input_bam),
        outputs=dict(output_bam=output_bam),
        params=params,
         
    )


@collect_tool()
def setmateinformation(
    *,
    input_bam: str,
    output_bam: str,
    compression: Optional[int] = None,
    threads: Optional[int] = 1,
    java_opts: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Adds and/or fixes mate information on paired-end reads. Sets the MQ (mate mapping quality), MC (mate cigar string), ensures all mate-related
    flag fields are set correctly, and that the mate reference and mate start position are correct.

    Args:
        input_bam: Path to the input BAM file.
        output_bam: Path to the output BAM file.
        compression (optional): Compression level for the BAM file (0-9). Defaults to None.
        threads (optional): Number of threads to use. Defaults to 1.
        java_opts (optional): Additional Java options to use for the tool. Defaults to None.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_setmateinformation(
        input_bam=input_bam,
        output_bam=output_bam,
        compression=compression,
        threads=threads,
        java_opts=java_opts,
         
    )
