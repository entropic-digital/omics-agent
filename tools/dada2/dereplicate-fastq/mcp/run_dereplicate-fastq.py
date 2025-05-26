from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_dereplicate_fastq(
    *,
    input_fastq: str,
    output_rds: str,
    optional_params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    DADA2 Dereplication of FASTQ files.

    Args:
        input_fastq: Path to the input FASTQ file.
        output_rds: Path to the output RDS file containing a `derep-class` object.
        optional_params (optional): Optional arguments for the `derepFastq` function as key-value pairs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/dada2/dereplicate-fastq",
        inputs={"input_fastq": input_fastq},
        outputs={"output_rds": output_rds},
        params=optional_params if optional_params else {},
         
    )


@collect_tool()
def dada2_dereplicate_fastq(
    *,
    input_fastq: str,
    output_rds: str,
    optional_params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Decorated function for DADA2 Dereplication of FASTQ files.

    Args:
        input_fastq: Path to the input FASTQ file.
        output_rds: Path to the output RDS file containing a `derep-class` object.
        optional_params (optional): Optional arguments for the `derepFastq` function as key-value pairs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_dereplicate_fastq(
        input_fastq=input_fastq,
        output_rds=output_rds,
        optional_params=optional_params,
         
    )
