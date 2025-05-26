from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_collectduplexseqmetrics(
    *,
    input_bam: str,
    output_txt: str,
    output_metrics: str,
    reference: Optional[str] = None,
    min_base_quality: int = 10,
    min_mapping_quality: int = 30,
    collapse_duplex: bool = True,
     
) -> subprocess.CompletedProcess:
    """
    Collects a suite of metrics to QC duplex sequencing data.

    Args:
        input_bam: BAM file containing sequencing data.
        output_txt: Path to save the metrics summary (txt format).
        output_metrics: Path to save detailed metrics.
        reference (optional): Path to the reference genome file.
        min_base_quality: Minimum base quality threshold for analyses. Defaults to 10.
        min_mapping_quality: Minimum mapping quality threshold for reads. Defaults to 30.
        collapse_duplex: Whether to collapse duplex reads into one consistent sequence. Defaults to True.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/fgbio/collectduplexseqmetrics",
        inputs=dict(input_bam=input_bam),
        outputs=dict(output_txt=output_txt, output_metrics=output_metrics),
        params={
            "reference": reference,
            "min_base_quality": min_base_quality,
            "min_mapping_quality": min_mapping_quality,
            "collapse_duplex": collapse_duplex,
        },
         
    )


@collect_tool()
def collect_duplex_seq_metrics(
    *,
    input_bam: str,
    output_txt: str,
    output_metrics: str,
    reference: Optional[str] = None,
    min_base_quality: int = 10,
    min_mapping_quality: int = 30,
    collapse_duplex: bool = True,
     
) -> subprocess.CompletedProcess:
    """
    Collects a suite of metrics to QC duplex sequencing data.

    Args:
        input_bam: BAM file containing sequencing data.
        output_txt: Path to save the metrics summary (txt format).
        output_metrics: Path to save detailed metrics.
        reference (optional): Path to the reference genome file.
        min_base_quality: Minimum base quality threshold for analyses. Defaults to 10.
        min_mapping_quality: Minimum mapping quality threshold for reads. Defaults to 30.
        collapse_duplex: Whether to collapse duplex reads into one consistent sequence. Defaults to True.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collectduplexseqmetrics(
        input_bam=input_bam,
        output_txt=output_txt,
        output_metrics=output_metrics,
        reference=reference,
        min_base_quality=min_base_quality,
        min_mapping_quality=min_mapping_quality,
        collapse_duplex=collapse_duplex,
         
    )
