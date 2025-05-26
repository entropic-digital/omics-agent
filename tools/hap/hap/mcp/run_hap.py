from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_hap(
    *,
    truth_vcf: str,
    query_vcf: str,
    output_dir: str,
    reference: str,
    truth_bed: Optional[str] = None,
    query_bed: Optional[str] = None,
    roc_levels: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Comparison of VCF files and calculation of performance metrics following GA4GH best practices
    for benchmarking small variant call sets (Krusche, P. et al. 2019). Part of the hap.py suite by Illumina.

    Args:
        truth_vcf: Path to the truth VCF file.
        query_vcf: Path to the query VCF file.
        output_dir: Directory where output files will be saved.
        reference: Reference genome FASTA file.
        truth_bed (optional): BED file to limit the evaluation region for the truth VCF.
        query_bed (optional): BED file to limit the evaluation region for the query VCF.
        roc_levels (optional): File specifying ROC levels.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/hap.py",
        inputs=dict(
            truth_vcf=truth_vcf,
            query_vcf=query_vcf,
            reference=reference,
            truth_bed=truth_bed,
            query_bed=query_bed,
            roc_levels=roc_levels,
        ),
        params={},
        outputs=dict(output_dir=output_dir),
         
    )


@collect_tool()
def hap(
    *,
    truth_vcf: str,
    query_vcf: str,
    output_dir: str,
    reference: str,
    truth_bed: Optional[str] = None,
    query_bed: Optional[str] = None,
    roc_levels: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Comparison of VCF files and calculation of performance metrics following GA4GH best practices
    for benchmarking small variant call sets (Krusche, P. et al. 2019). Part of the hap.py suite by Illumina.

    Args:
        truth_vcf: Path to the truth VCF file.
        query_vcf: Path to the query VCF file.
        output_dir: Directory where output files will be saved.
        reference: Reference genome FASTA file.
        truth_bed (optional): BED file to limit the evaluation region for the truth VCF.
        query_bed (optional): BED file to limit the evaluation region for the query VCF.
        roc_levels (optional): File specifying ROC levels.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_hap(
        truth_vcf=truth_vcf,
        query_vcf=query_vcf,
        output_dir=output_dir,
        reference=reference,
        truth_bed=truth_bed,
        query_bed=query_bed,
        roc_levels=roc_levels,
         
    )
