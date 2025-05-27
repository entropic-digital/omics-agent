from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_reheader(
    *,
    input_file: str,
    output_file: str,
    header: Optional[str] = None,
    samples: Optional[str] = None,
    uncompressed_bcf: bool = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Change the header or sample names of a VCF/BCF file.

    Args:
        input_file: Path to the input VCF/BCF file.
        output_file: Path to the output VCF/BCF file with the new header.
        header (optional): Path to the new header file (optional if `samples` is provided).
        samples (optional): Path to the new sample names file (optional if `header` is provided).
        uncompressed_bcf: If True, specifies that a BCF output should be uncompressed.
        extra (optional): Additional arguments for the bcftools command.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "uncompressed_bcf": uncompressed_bcf,
        "extra": extra,
    }

    inputs = {
        "vcf_file": input_file,
    }

    if header:
        inputs["header"] = header
    if samples:
        inputs["samples"] = samples

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bcftools/reheader",
        inputs=inputs,
        outputs={"output_file": output_file},
        params={k: v for k, v in params.items() if v is not None},
         
    )


@collect_tool()
def reheader(
    *,
    input_file: str,
    output_file: str,
    header: Optional[str] = None,
    samples: Optional[str] = None,
    uncompressed_bcf: bool = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Change the header or sample names of a VCF/BCF file.

    Args:
        input_file: Path to the input VCF/BCF file.
        output_file: Path to the output VCF/BCF file with the new header.
        header (optional): Path to the new header file (optional if `samples` is provided).
        samples (optional): Path to the new sample names file (optional if `header` is provided).
        uncompressed_bcf: If True, specifies that a BCF output should be uncompressed.
        extra (optional): Additional arguments for the bcftools command.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_reheader(
        input_file=input_file,
        output_file=output_file,
        header=header,
        samples=samples,
        uncompressed_bcf=uncompressed_bcf,
        extra=extra,
         
    )
