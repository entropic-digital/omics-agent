from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_germline(
    *,
    reference_fasta: str,
    bam: str,
    output_vcf: str,
    output_tbi: str,
    regions_bed: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call germline variants with Strelka.

    Args:
        reference_fasta: Path to the reference FASTA file.
        bam: Path to the BAM file for variant calling.
        output_vcf: Path to the output VCF file.
        output_tbi: Path to the output TBI index file.
        regions_bed (optional): Path to a BED file specifying regions for variant calling.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/strelka/germline",
        inputs={"reference_fasta": reference_fasta, "bam": bam},
        outputs={"output_vcf": output_vcf, "output_tbi": output_tbi},
        params={"regions_bed": regions_bed} if regions_bed else {},
         
    )


@collect_tool()
def germline(
    *,
    reference_fasta: str,
    bam: str,
    output_vcf: str,
    output_tbi: str,
    regions_bed: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Call germline variants with Strelka.

    Args:
        reference_fasta: Path to the reference FASTA file.
        bam: Path to the BAM file for variant calling.
        output_vcf: Path to the output VCF file.
        output_tbi: Path to the output TBI index file.
        regions_bed (optional): Path to a BED file specifying regions for variant calling.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_germline(
        reference_fasta=reference_fasta,
        bam=bam,
        output_vcf=output_vcf,
        output_tbi=output_tbi,
        regions_bed=regions_bed,
         
    )
