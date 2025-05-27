from typing import Optional, Dict, Any
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_fastq_screen(
    *,
    input_fastq: str,
    output_txt: str,
    output_png: str,
    fastq_screen_config: Optional[Dict[str, Any]] = None,
    aligner: str = "bowtie2",
    subset: int = 100000,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Runs the `fastq_screen` tool to screen a library of FASTQ sequences against sequence databases.

    Args:
        input_fastq: Path to the input FASTQ file (gzipped or not).
        output_txt: Path to the output text file containing the fraction of reads mapped.
        output_png: Path to the output PNG bar plot.
        fastq_screen_config (optional): Configuration as a dictionary or filename.
        aligner (optional): Alignment tool to use (default is "bowtie2").
        subset (optional): Number of reads to subset for screening (default is 100000).
        extra (optional): Additional arguments to pass to `fastq_screen`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/fastq_screen",
        inputs={"input_fastq": input_fastq},
        outputs={"output_txt": output_txt, "output_png": output_png},
        params={
            "fastq_screen_config": fastq_screen_config,
            "aligner": aligner,
            "subset": subset,
            "extra": extra,
        },
         
    )


@collect_tool()
def fastq_screen(
    *,
    input_fastq: str,
    output_txt: str,
    output_png: str,
    fastq_screen_config: Optional[Dict[str, Any]] = None,
    aligner: str = "bowtie2",
    subset: int = 100000,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Wrapper function for the `fastq_screen` tool to screen a FASTQ sequence library.

    Args:
        input_fastq: Path to the input FASTQ file (gzipped or not).
        output_txt: Path to the output text file containing the fraction of reads mapped.
        output_png: Path to the output PNG bar plot.
        fastq_screen_config (optional): Configuration as a dictionary or filename.
        aligner (optional): Alignment tool to use (default is "bowtie2").
        subset (optional): Number of reads to subset for screening (default is 100000).
        extra (optional): Additional arguments to pass to `fastq_screen`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_fastq_screen(
        input_fastq=input_fastq,
        output_txt=output_txt,
        output_png=output_png,
        fastq_screen_config=fastq_screen_config,
        aligner=aligner,
        subset=subset,
        extra=extra,
         
    )
