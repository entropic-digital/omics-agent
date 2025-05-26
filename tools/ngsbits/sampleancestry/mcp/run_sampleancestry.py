from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_sampleancestry(
    *,
    input_vcfs: str,
    output_results_tsv: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Estimates the ancestry of a sample based on variants using the NGS-bits SampleAncestry tool.

    Args:
        input_vcfs: Path to one or multiple VCF file(s).
        output_results_tsv: Path to results table (TSV).
        extra (optional): Optional parameters besides IO.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/ngsbits/sampleancestry",
        inputs=dict(input_vcfs=input_vcfs),
        outputs=dict(output_results_tsv=output_results_tsv),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def sampleancestry(
    *,
    input_vcfs: str,
    output_results_tsv: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Estimates the ancestry of a sample based on variants using the NGS-bits SampleAncestry tool.

    Args:
        input_vcfs: Path to one or multiple VCF file(s).
        output_results_tsv: Path to results table (TSV).
        extra (optional): Optional parameters besides IO.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_sampleancestry(
        input_vcfs=input_vcfs,
        output_results_tsv=output_results_tsv,
        extra=extra,
         
    )
