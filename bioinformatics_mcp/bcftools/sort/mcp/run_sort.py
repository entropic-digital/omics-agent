from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_sort(
    *,
    input_vcf: str,
    output_vcf: str,
    max_mem: str,
    temp_dir: str,
    output_type: Optional[str] = None,
    uncompressed_bcf: Optional[bool] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Sort a VCF/BCF file using bcftools.

    Args:
        input_vcf: Path to the input VCF file.
        output_vcf: Path to the output sorted VCF file.
        max_mem: Maximum memory to use per thread.
        temp_dir: Directory for temporary files.
        output_type (optional): Output type (e.g., 'u', 'b', 'v', 'z').
        uncompressed_bcf (optional): Specify that a BCF output should be uncompressed (ignored otherwise).
        extra (optional): Additional program arguments (not including '--threads', '-o/--output',
                          '-O/--output-type', '-m/--max-mem', or '-T/--temp-dir').
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "max_mem": max_mem,
        "temp_dir": temp_dir,
        "output_type": output_type,
        "uncompressed_bcf": uncompressed_bcf,
        "extra": extra,
    }
    # Filter out None values for params
    params = {key: value for key, value in params.items() if value is not None}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bcftools/sort",
        inputs={"input_vcf": input_vcf},
        outputs={"output_vcf": output_vcf},
        params=params,
         
    )


@collect_tool()
def sort(
    *,
    input_vcf: str,
    output_vcf: str,
    max_mem: str,
    temp_dir: str,
    output_type: Optional[str] = None,
    uncompressed_bcf: Optional[bool] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Sort a VCF/BCF file using bcftools.

    Args:
        input_vcf: Path to the input VCF file.
        output_vcf: Path to the output sorted VCF file.
        max_mem: Maximum memory to use per thread.
        temp_dir: Directory for temporary files.
        output_type (optional): Output type (e.g., 'u', 'b', 'v', 'z').
        uncompressed_bcf (optional): Specify that a BCF output should be uncompressed (ignored otherwise).
        extra (optional): Additional program arguments (not including '--threads', '-o/--output',
                          '-O/--output-type', '-m/--max-mem', or '-T/--temp-dir').
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_sort(
        input_vcf=input_vcf,
        output_vcf=output_vcf,
        max_mem=max_mem,
        temp_dir=temp_dir,
        output_type=output_type,
        uncompressed_bcf=uncompressed_bcf,
        extra=extra,
         
    )
