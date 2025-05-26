from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_sample_inference(
    *,
    derep: str,
    err: str,
    output: str,
    params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the DADA2 sample inference tool.

    Args:
        derep: Path to the RDS file with the dereplicated sequences.
        err: Path to the RDS file with the error model.
        output: Path to the RDS file to store the inferred sample composition.
        params (optional): Optional arguments for the ``dada()`` function, provided as a dictionary of key=value pairs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/dada2/sample-inference",
        inputs=dict(derep=derep, err=err),
        outputs=dict(output=output),
        params=params or {},
         
    )


@collect_tool()
def sample_inference(
    *,
    derep: str,
    err: str,
    output: str,
    params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Tool for inferring sample composition using DADA2's ``dada`` function.

    Args:
        derep: Path to the RDS file with the dereplicated sequences.
        err: Path to the RDS file with the error model.
        output: Path to the RDS file to store the inferred sample composition.
        params (optional): Optional arguments for the ``dada()`` function, provided as a dictionary of key=value pairs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_sample_inference(
        derep=derep,
        err=err,
        output=output,
        params=params,
         
    )
