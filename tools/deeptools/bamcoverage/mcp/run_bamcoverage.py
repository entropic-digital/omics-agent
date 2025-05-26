from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bamcoverage(
    *,
    bam: str,
    output: str,
    blacklist: Optional[str] = None,
    effective_genome_size: Optional[str] = None,
    genome: Optional[str] = None,
    read_length: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the deepTools bamCoverage tool to generate a coverage track from a BAM file.

    Args:
        bam: Path to alignment (BAM) file.
        output: Path to the output coverage file (bigWig or bedGraph).
        blacklist (optional): Path to an optional blacklist region file (BED).
        effective_genome_size (optional): Effective genome size value.
        genome (optional): Pre-computed genome parameter for effective genome size.
            Options: `GRCm37`, `GRCm38`, `GRCm39`, `GRCh37`, `GRCh38`, `dm3`, `dm6`, `WBcel235`, `GRCz10`.
        read_length (optional): Pre-computed read length.
            Options: `50`, `75`, `100`, `150`, `200`, `250`.
        extra (optional): Additional parameters to be passed to bamCoverage.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    input_files = {"bam": bam}
    if blacklist:
        input_files["blacklist"] = blacklist

    params = {"output": output}
    if effective_genome_size:
        params["effective_genome_size"] = effective_genome_size
    if genome:
        params["genome"] = genome
    if read_length:
        params["read_length"] = read_length
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:tools/deeptools/bamcoverage",
        inputs=input_files,
        params=params,
         
    )


@collect_tool()
def bamcoverage(
    *,
    bam: str,
    output: str,
    blacklist: Optional[str] = None,
    effective_genome_size: Optional[str] = None,
    genome: Optional[str] = None,
    read_length: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the deepTools bamCoverage tool to generate a coverage track from a BAM file.

    Args:
        bam: Path to alignment (BAM) file.
        output: Path to the output coverage file (bigWig or bedGraph).
        blacklist (optional): Path to an optional blacklist region file (BED).
        effective_genome_size (optional): Effective genome size value.
        genome (optional): Pre-computed genome parameter for effective genome size.
            Options: `GRCm37`, `GRCm38`, `GRCm39`, `GRCh37`, `GRCh38`, `dm3`, `dm6`, `WBcel235`, `GRCz10`.
        read_length (optional): Pre-computed read length.
            Options: `50`, `75`, `100`, `150`, `200`, `250`.
        extra (optional): Additional parameters to be passed to bamCoverage.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bamcoverage(
        bam=bam,
        output=output,
        blacklist=blacklist,
        effective_genome_size=effective_genome_size,
        genome=genome,
        read_length=read_length,
        extra=extra,
         
    )
