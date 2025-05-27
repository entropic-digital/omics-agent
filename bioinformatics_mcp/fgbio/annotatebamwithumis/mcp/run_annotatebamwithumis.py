from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_annotatebamwithumis(
    *,
    input_bam: str,
    input_fastq: str,
    output_bam: str,
    umi_tag: Optional[str] = "RX",
    discard_tag_failures: Optional[bool] = True,
    max_records_in_ram: Optional[int] = 500000,
    compression_level: Optional[int] = 5,
     
) -> subprocess.CompletedProcess:
    """
    Annotates existing BAM files with UMIs (Unique Molecular Indices) from a separate FASTQ file.

    Args:
        input_bam: Path to the input BAM file.
        input_fastq: Path to the input FASTQ file containing UMIs.
        output_bam: Path to the output BAM file.
        umi_tag (optional): BAM tag name for storing UMIs. Defaults to "RX".
        discard_tag_failures (optional): Whether to discard reads where UMIs cannot be assigned. Defaults to True.
        max_records_in_ram (optional): Maximum number of records to keep in memory before spilling to disk. Defaults to 500000.
        compression_level (optional): Compression level for the output BAM file. Defaults to 5.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/fgbio/annotatebamwithumis",
        inputs=dict(input_bam=input_bam, input_fastq=input_fastq),
        outputs=dict(output_bam=output_bam),
        params={
            "umi_tag": umi_tag,
            "discard_tag_failures": discard_tag_failures,
            "max_records_in_ram": max_records_in_ram,
            "compression_level": compression_level,
        },
         
    )


@collect_tool()
def annotatebamwithumis(
    *,
    input_bam: str,
    input_fastq: str,
    output_bam: str,
    umi_tag: Optional[str] = "RX",
    discard_tag_failures: Optional[bool] = True,
    max_records_in_ram: Optional[int] = 500000,
    compression_level: Optional[int] = 5,
     
) -> subprocess.CompletedProcess:
    """
    Annotates existing BAM files with UMIs (Unique Molecular Indices) from a separate FASTQ file.

    Args:
        input_bam: Path to the input BAM file.
        input_fastq: Path to the input FASTQ file containing UMIs.
        output_bam: Path to the output BAM file.
        umi_tag (optional): BAM tag name for storing UMIs. Defaults to "RX".
        discard_tag_failures (optional): Whether to discard reads where UMIs cannot be assigned. Defaults to True.
        max_records_in_ram (optional): Maximum number of records to keep in memory before spilling to disk. Defaults to 500000.
        compression_level (optional): Compression level for the output BAM file. Defaults to 5.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_annotatebamwithumis(
        input_bam=input_bam,
        input_fastq=input_fastq,
        output_bam=output_bam,
        umi_tag=umi_tag,
        discard_tag_failures=discard_tag_failures,
        max_records_in_ram=max_records_in_ram,
        compression_level=compression_level,
         
    )
