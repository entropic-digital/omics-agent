from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_delly(
    *,
    bam_cram_files: str,
    reference_genome: str,
    output_vcf_bcf: str,
    bed_file: Optional[str] = None,
    uncompressed_bcf: Optional[bool] = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call variants with delly.

    Args:
        bam_cram_files: Input BAM/CRAM file(s).
        reference_genome: Reference genome.
        output_vcf_bcf: Output VCF/BCF file containing SVs.
        bed_file (optional): BED file to restrict calls to specific regions.
        uncompressed_bcf (optional): Flag to set output to uncompressed BCF (ignored if output is `vcf` or `vcf.gz`).
        extra (optional): Additional program arguments passed to delly.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/delly",
        inputs={
            "bam_cram_files": bam_cram_files,
            "reference_genome": reference_genome,
            "bed_file": bed_file,
        },
        outputs={"output_vcf_bcf": output_vcf_bcf},
        params={
            "uncompressed_bcf": uncompressed_bcf,
            "extra": extra,
        },
         
    )


@collect_tool()
def delly(
    *,
    bam_cram_files: str,
    reference_genome: str,
    output_vcf_bcf: str,
    bed_file: Optional[str] = None,
    uncompressed_bcf: Optional[bool] = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call variants with delly.

    Args:
        bam_cram_files: Input BAM/CRAM file(s).
        reference_genome: Reference genome.
        output_vcf_bcf: Output VCF/BCF file containing SVs.
        bed_file (optional): BED file to restrict calls to specific regions.
        uncompressed_bcf (optional): Flag to set output to uncompressed BCF (ignored if output is `vcf` or `vcf.gz`).
        extra (optional): Additional program arguments passed to delly.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_delly(
        bam_cram_files=bam_cram_files,
        reference_genome=reference_genome,
        output_vcf_bcf=output_vcf_bcf,
        bed_file=bed_file,
        uncompressed_bcf=uncompressed_bcf,
        extra=extra,
         
    )
