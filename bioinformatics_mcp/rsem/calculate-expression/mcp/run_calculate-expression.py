from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_calculate_expression(
    *,
    bam: str,
    fq_one: str,
    reference: str,
    reference_bowtie: Optional[str] = None,
    fq_two: Optional[str] = None,
    genes_results: str,
    isoforms_results: str,
     
) -> subprocess.CompletedProcess:
    """
    Run rsem-calculate-expression to estimate gene and isoform expression from RNA-Seq data.

    Args:
        bam: BAM file with reads aligned to transcriptome.
        fq_one: FASTQ file of reads (read_1 for paired-end sequencing).
        reference: Index files created by rsem-prepare-reference.
        reference_bowtie (optional): Additionally needed for FASTQ input; Index files created
            (by bowtie-build) from the reference transcriptome.
        fq_two (optional): Second FASTQ file of reads (read_2 for paired-end sequencing).
        genes_results: Output file containing per-gene quantification data for the sample.
        isoforms_results: Output file containing per-transcript quantification data for the sample.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/rsem/calculate-expression",
        inputs={
            "bam": bam,
            "fq_one": fq_one,
            "fq_two": fq_two,
            "reference": reference,
            "reference_bowtie": reference_bowtie,
        },
        outputs={
            "genes_results": genes_results,
            "isoforms_results": isoforms_results,
        },
         
    )


@collect_tool()
def calculate_expression(
    *,
    bam: str,
    fq_one: str,
    reference: str,
    reference_bowtie: Optional[str] = None,
    fq_two: Optional[str] = None,
    genes_results: str,
    isoforms_results: str,
     
) -> subprocess.CompletedProcess:
    """
    Run rsem-calculate-expression to estimate gene and isoform expression from RNA-Seq data.

    Args:
        bam: BAM file with reads aligned to transcriptome.
        fq_one: FASTQ file of reads (read_1 for paired-end sequencing).
        reference: Index files created by rsem-prepare-reference.
        reference_bowtie (optional): Additionally needed for FASTQ input; Index files created
            (by bowtie-build) from the reference transcriptome.
        fq_two (optional): Second FASTQ file of reads (read_2 for paired-end sequencing).
        genes_results: Output file containing per-gene quantification data for the sample.
        isoforms_results: Output file containing per-transcript quantification data for the sample.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_calculate_expression(
        bam=bam,
        fq_one=fq_one,
        reference=reference,
        reference_bowtie=reference_bowtie,
        fq_two=fq_two,
        genes_results=genes_results,
        isoforms_results=isoforms_results,
         
    )
