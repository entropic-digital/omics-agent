from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_merge_pairs(
    *,
    dadaF: str,
    dadaR: str,
    derepF: str,
    derepR: str,
    output: str,
    optional_params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    DADA2 mergePairs function implementation.

    Merges denoised forward and reverse reads using DADA2's `mergePairs` function.
    Refer to the DADA2 tutorial and manual for a detailed explanation of this process.

    Args:
        dadaF: Path to the RDS file with inferred sample composition from forward reads.
        dadaR: Path to the RDS file with inferred sample composition from reverse reads.
        derepF: Path to the RDS file with dereplicated forward reads.
        derepR: Path to the RDS file with dereplicated reverse reads.
        output: Path to save the resulting merged pairs RDS file.
        optional_params (optional): Dictionary of additional key-value arguments for `mergePairs`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/dada2/merge-pairs",
        inputs=dict(
            dadaF=dadaF,
            dadaR=dadaR,
            derepF=derepF,
            derepR=derepR,
        ),
        outputs=dict(output=output),
        params=optional_params if optional_params else {},
         
    )


@collect_tool()
def merge_pairs(
    *,
    dadaF: str,
    dadaR: str,
    derepF: str,
    derepR: str,
    output: str,
    optional_params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    DADA2 mergePairs function implementation.

    Merges denoised forward and reverse reads using DADA2's `mergePairs` function.
    Refer to the DADA2 tutorial and manual for a detailed explanation of this process.

    Args:
        dadaF: Path to the RDS file with inferred sample composition from forward reads.
        dadaR: Path to the RDS file with inferred sample composition from reverse reads.
        derepF: Path to the RDS file with dereplicated forward reads.
        derepR: Path to the RDS file with dereplicated reverse reads.
        output: Path to save the resulting merged pairs RDS file.
        optional_params (optional): Dictionary of additional key-value arguments for `mergePairs`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_merge_pairs(
        dadaF=dadaF,
        dadaR=dadaR,
        derepF=derepF,
        derepR=derepR,
        output=output,
        optional_params=optional_params,
         
    )
