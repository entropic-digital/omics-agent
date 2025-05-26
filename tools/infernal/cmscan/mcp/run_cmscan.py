from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_cmscan(
    *,
    sequence_file: str,
    covariance_models: str,
    rna_alignments: str,
    tblout: Optional[str] = None,
    main_output: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the Infernal cmscan tool to search sequences against RNA covariance models.

    Args:
        sequence_file: Input file containing the sequences to analyze.
        covariance_models: Input file with RNA covariance models (CMs).
        rna_alignments: Output file to store the result of RNA alignments.
        tblout (optional): File to save additional concise tabular results.
        main_output (optional): File to redirect main output; set to '/dev/null' to discard.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {}
    if tblout:
        params["tblout"] = tblout
    if main_output:
        params["main_output"] = main_output

    return run_snake_wrapper(
        wrapper="file:tools/infernal/cmscan",
        inputs=dict(sequence_file=sequence_file, covariance_models=covariance_models),
        outputs=dict(rna_alignments=rna_alignments),
        params=params,
         
    )


@collect_tool()
def cmscan(
    *,
    sequence_file: str,
    covariance_models: str,
    rna_alignments: str,
    tblout: Optional[str] = None,
    main_output: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the Infernal cmscan tool to search sequences against RNA covariance models.

    Args:
        sequence_file: Input file containing the sequences to analyze.
        covariance_models: Input file with RNA covariance models (CMs).
        rna_alignments: Output file to store the result of RNA alignments.
        tblout (optional): File to save additional concise tabular results.
        main_output (optional): File to redirect main output; set to '/dev/null' to discard.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_cmscan(
        sequence_file=sequence_file,
        covariance_models=covariance_models,
        rna_alignments=rna_alignments,
        tblout=tblout,
        main_output=main_output,
         
    )
