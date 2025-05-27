from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_call(
    *,
    input_bam: str,
    reference_fasta: str,
    output_vcf: str,
    log_file: Optional[str] = None,
    temp_dir: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Perform variant calling using GRIDSS.

    Args:
        input_bam: Path to the input BAM file.
        reference_fasta: Path to the reference genome FASTA file.
        output_vcf: Path to the output VCF file.
        log_file (optional): Path to the log file.
        temp_dir (optional): Path to the temporary directory.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gridss/call",
        inputs=dict(
            input_bam=input_bam,
            reference_fasta=reference_fasta,
        ),
        outputs=dict(
            output_vcf=output_vcf,
        ),
        params={
            key: value
            for key, value in [("log_file", log_file), ("temp_dir", temp_dir)]
            if value is not None
        },
         
    )


@collect_tool()
def call(
    *,
    input_bam: str,
    reference_fasta: str,
    output_vcf: str,
    log_file: Optional[str] = None,
    temp_dir: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Perform variant calling using GRIDSS.

    Args:
        input_bam: Path to the input BAM file.
        reference_fasta: Path to the reference genome FASTA file.
        output_vcf: Path to the output VCF file.
        log_file (optional): Path to the log file.
        temp_dir (optional): Path to the temporary directory.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_call(
        input_bam=input_bam,
        reference_fasta=reference_fasta,
        output_vcf=output_vcf,
        log_file=log_file,
        temp_dir=temp_dir,
         
    )
