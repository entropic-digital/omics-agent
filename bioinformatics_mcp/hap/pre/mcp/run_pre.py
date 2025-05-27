from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_pre(
    *,
    input_vcf: str,
    output_vcf: str,
    ref_file: str,
    ref_index: Optional[str] = None,
    normalization: bool = True,
    compression_level: int = 5,
     
) -> subprocess.CompletedProcess:
    """
    Preprocessing/normalisation of VCF/BCF files using hap.py suite.

    Args:
        input_vcf: Path to the input VCF/BCF file.
        output_vcf: Path to the normalized/processed output VCF/BCF file.
        ref_file: Path to the reference genome file (FASTA).
        ref_index (optional): Path to the index file for the reference genome (default: None).
        normalization: Whether to perform normalization or not (default: True).
        compression_level: Compression level for the output VCF/BCF file (default: 5).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "ref_file": ref_file,
        "normalization": normalization,
        "compression_level": compression_level,
    }
    if ref_index:
        params["ref_index"] = ref_index

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/hap.py/pre.py/",
        inputs=dict(input_vcf=input_vcf),
        outputs=dict(output_vcf=output_vcf),
        params=params,
         
    )


@collect_tool()
def pre(
    *,
    input_vcf: str,
    output_vcf: str,
    ref_file: str,
    ref_index: Optional[str] = None,
    normalization: bool = True,
    compression_level: int = 5,
     
) -> subprocess.CompletedProcess:
    """
    Preprocessing/normalisation of VCF/BCF files using hap.py suite.

    Args:
        input_vcf: Path to the input VCF/BCF file.
        output_vcf: Path to the normalized/processed output VCF/BCF file.
        ref_file: Path to the reference genome file (FASTA).
        ref_index (optional): Path to the index file for the reference genome (default: None).
        normalization: Whether to perform normalization or not (default: True).
        compression_level: Compression level for the output VCF/BCF file (default: 5).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_pre(
        input_vcf=input_vcf,
        output_vcf=output_vcf,
        ref_file=ref_file,
        ref_index=ref_index,
        normalization=normalization,
        compression_level=compression_level,
         
    )
