from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_freebayes(
    *,
    input_files: List[str],
    reference_genome: str,
    output_file: str,
    extra: Optional[str] = None,
    normalize: Optional[str] = None,
    chunksize: int = 100000,
     
) -> subprocess.CompletedProcess:
    """
    Call small genomic variants with freebayes.

    Args:
        input_files: List of SAM/BAM/CRAM file(s) as input.
        reference_genome: Path to the reference genome file.
        output_file: Path to the output VCF/VCF.gz/BCF file.
        extra (optional): Additional arguments for freebayes.
        normalize (optional): Use `bcftools norm` to normalize indels (one of
            `-a`, `-f`, `-m`, `-D`, or `-d` must be used).
        chunksize: Reference genome chunk size for parallelization (default 100000).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "extra": extra,
        "normalize": normalize,
        "chunksize": chunksize,
    }
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/freebayes",
        inputs={"input_files": input_files, "reference_genome": reference_genome},
        outputs={"output_file": output_file},
        params={key: value for key, value in params.items() if value is not None},
         
    )


@collect_tool()
def freebayes(
    *,
    input_files: List[str],
    reference_genome: str,
    output_file: str,
    extra: Optional[str] = None,
    normalize: Optional[str] = None,
    chunksize: int = 100000,
     
) -> subprocess.CompletedProcess:
    """
    Call small genomic variants with freebayes.

    Args:
        input_files: List of SAM/BAM/CRAM file(s) as input.
        reference_genome: Path to the reference genome file.
        output_file: Path to the output VCF/VCF.gz/BCF file.
        extra (optional): Additional arguments for freebayes.
        normalize (optional): Use `bcftools norm` to normalize indels (one of
            `-a`, `-f`, `-m`, `-D`, or `-d` must be used).
        chunksize: Reference genome chunk size for parallelization (default 100000).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_freebayes(
        input_files=input_files,
        reference_genome=reference_genome,
        output_file=output_file,
        extra=extra,
        normalize=normalize,
        chunksize=chunksize,
         
    )
