from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_genefuse(
    *,
    fastq_files: str,
    gene_fuse_settings: str,
    reference_genome: str,
    txt_fusions: str,
    html_report: str,
    json_report: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    A tool to detect and visualize target gene fusions by scanning FASTQ files directly.

    Args:
        fastq_files: Input FASTQ files to be scanned for gene fusions.
        gene_fuse_settings: Path to the gene fuse settings file.
        reference_genome: Reference genome file.
        txt_fusions: Output file to save gene fusion results in text format.
        html_report: Output file to save the HTML report of the analysis.
        json_report: Output file to save the JSON report of the analysis.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/genefuse",
        inputs={
            "fastq_files": fastq_files,
            "gene_fuse_settings": gene_fuse_settings,
            "reference_genome": reference_genome,
        },
        outputs={
            "txt_fusions": txt_fusions,
            "html_report": html_report,
            "json_report": json_report,
        },
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def genefuse(
    *,
    fastq_files: str,
    gene_fuse_settings: str,
    reference_genome: str,
    txt_fusions: str,
    html_report: str,
    json_report: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    A tool to detect and visualize target gene fusions by scanning FASTQ files directly.

    Args:
        fastq_files: Input FASTQ files to be scanned for gene fusions.
        gene_fuse_settings: Path to the gene fuse settings file.
        reference_genome: Reference genome file.
        txt_fusions: Output file to save gene fusion results in text format.
        html_report: Output file to save the HTML report of the analysis.
        json_report: Output file to save the JSON report of the analysis.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_genefuse(
        fastq_files=fastq_files,
        gene_fuse_settings=gene_fuse_settings,
        reference_genome=reference_genome,
        txt_fusions=txt_fusions,
        html_report=html_report,
        json_report=json_report,
        extra=extra,
         
    )
