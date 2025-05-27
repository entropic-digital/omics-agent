from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_call(
    *,
    input_bam: str,
    ref: str,
    output_vcf: str,
    sample_name: Optional[str] = None,
    bed: Optional[str] = None,
    threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Call variants using LoFreq.

    Args:
        input_bam: Path to the input BAM file.
        ref: Path to the reference genome file.
        output_vcf: Path to the output VCF file.
        sample_name (optional): Sample name for the analysis.
        bed (optional): BED file for targeted regions.
        threads (optional): Number of threads to use (default is 1).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/lofreq/call",
        inputs=dict(input_bam=input_bam, ref=ref),
        outputs=dict(output_vcf=output_vcf),
        params={
            "sample_name": sample_name,
            "bed": bed,
            "threads": threads,
        },
         
    )


@collect_tool()
def call(
    *,
    input_bam: str,
    ref: str,
    output_vcf: str,
    sample_name: Optional[str] = None,
    bed: Optional[str] = None,
    threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """
    Call variants using LoFreq.

    Args:
        input_bam: Path to the input BAM file.
        ref: Path to the reference genome file.
        output_vcf: Path to the output VCF file.
        sample_name (optional): Sample name for the analysis.
        bed (optional): BED file for targeted regions.
        threads (optional): Number of threads to use (default is 1).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_call(
        input_bam=input_bam,
        ref=ref,
        output_vcf=output_vcf,
        sample_name=sample_name,
        bed=bed,
        threads=threads,
         
    )
