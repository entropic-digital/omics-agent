from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_norm(
    *,
    input_vcf: str,
    fasta_ref: str,
    output_vcf: str,
    output_type: str,
    uncompressed_bcf: bool = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Left-align and normalize indels, check REF alleles, split multiallelics into rows,
    and recover multiallelics from rows using bcftools norm.

    Args:
        input_vcf: Input VCF/BCF file.
        fasta_ref: Reference genome in FASTA format.
        output_vcf: Path to the output VCF/BCF file.
        output_type: Type of the output file (e.g., 'v', 'b', 'u', etc.).
        uncompressed_bcf (optional): Whether to produce an uncompressed BCF output. Defaults to False.
        extra (optional): Additional arguments for bcftools norm, excluding threads, reference, and output options.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bcftools/norm",
        inputs=dict(input_vcf=input_vcf, fasta_ref=fasta_ref),
        outputs=dict(output_vcf=output_vcf),
        params={
            "output_type": output_type,
            "uncompressed_bcf": uncompressed_bcf,
            "extra": extra,
        },
         
    )


@collect_tool()
def norm(
    *,
    input_vcf: str,
    fasta_ref: str,
    output_vcf: str,
    output_type: str,
    uncompressed_bcf: bool = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Left-align and normalize indels, check REF alleles, split multiallelics into rows,
    and recover multiallelics from rows using bcftools norm.

    Args:
        input_vcf: Input VCF/BCF file.
        fasta_ref: Reference genome in FASTA format.
        output_vcf: Path to the output VCF/BCF file.
        output_type: Type of the output file (e.g., 'v', 'b', 'u', etc.).
        uncompressed_bcf (optional): Whether to produce an uncompressed BCF output. Defaults to False.
        extra (optional): Additional arguments for bcftools norm, excluding threads, reference, and output options.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_norm(
        input_vcf=input_vcf,
        fasta_ref=fasta_ref,
        output_vcf=output_vcf,
        output_type=output_type,
        uncompressed_bcf=uncompressed_bcf,
        extra=extra,
         
    )
