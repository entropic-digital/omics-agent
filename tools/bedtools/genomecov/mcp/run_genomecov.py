from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_genomecov(
    *,
    input_file: str,
    ref: Optional[str] = None,
    extra: Optional[str] = None,
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Computes genomic coverage of input files and generates histograms, per-base reports, or BEDGRAPH summaries.

    Args:
        input_file: Input file (BED/GFF/VCF/BAM) grouped by chromosome, sorted, and in proper format.
        ref: Path to genome file, required if input_file is BED/GFF/VCF (optional for BAM).
        extra: Additional arguments to pass to genomeCoverageBed (e.g., coverage calculation options).
        output_file: Path to the output genome coverage file (.genomecov).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"input_file": input_file}
    if ref:
        inputs["ref"] = ref

    params = {"extra": extra} if extra else {}

    return run_snake_wrapper(
        wrapper="file:tools/bedtools/genomecov",
        inputs=inputs,
        outputs={"output_file": output_file},
        params=params,
         
    )


@collect_tool()
def genomecov(
    *,
    input_file: str,
    ref: Optional[str] = None,
    extra: Optional[str] = None,
    output_file: str,
     
) -> subprocess.CompletedProcess:
    """
    Computes genomic coverage of input files and generates histograms, per-base reports, or BEDGRAPH summaries.

    Args:
        input_file: Input file (BED/GFF/VCF/BAM) grouped by chromosome, sorted, and in proper format.
        ref: Path to genome file, required if input_file is BED/GFF/VCF (optional for BAM).
        extra: Additional arguments to pass to genomeCoverageBed (e.g., coverage calculation options).
        output_file: Path to the output genome coverage file (.genomecov).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_genomecov(
        input_file=input_file,
        ref=ref,
        extra=extra,
        output_file=output_file,
         
    )
