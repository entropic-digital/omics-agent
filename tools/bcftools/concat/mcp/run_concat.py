from typing import Optional, List
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_concat(
    *,
    vcf_files: List[str],
    output_file: str,
    uncompressed_bcf: Optional[bool] = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Concatenate VCF/BCF files using bcftools concat.

    Args:
        vcf_files: List of VCF/BCF files to concatenate.
        output_file: Path to the concatenated output VCF/BCF file.
        uncompressed_bcf (optional): If True, output BCF will be uncompressed. Defaults to False.
        extra (optional): Additional arguments passed to bcftools concat (excluding `--threads`, `-o/--output`, and `-O/--output-type`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "uncompressed_bcf": uncompressed_bcf,
        "extra": extra,
    }
    return run_snake_wrapper(
        wrapper="file:tools/bcftools/concat",
        inputs={"vcf_files": vcf_files},
        outputs={"output_file": output_file},
        params={key: value for key, value in params.items() if value is not None},
         
    )


@collect_tool()
def concat(
    *,
    vcf_files: List[str],
    output_file: str,
    uncompressed_bcf: Optional[bool] = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Concatenate VCF/BCF files using bcftools concat.

    Args:
        vcf_files: List of VCF/BCF files to concatenate.
        output_file: Path to the concatenated output VCF/BCF file.
        uncompressed_bcf (optional): If True, output BCF will be uncompressed. Defaults to False.
        extra (optional): Additional arguments passed to bcftools concat (excluding `--threads`, `-o/--output`, and `-O/--output-type`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_concat(
        vcf_files=vcf_files,
        output_file=output_file,
        uncompressed_bcf=uncompressed_bcf,
        extra=extra,
         
    )
