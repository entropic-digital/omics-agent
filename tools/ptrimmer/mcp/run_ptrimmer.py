from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_ptrimmer(
    *,
    input_sequences: str,
    primer_sequences: str,
    output_trimmed_sequences: str,
    additional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Tool to trim off the primer sequence from multiplex amplicon sequencing.

    Args:
        input_sequences: Path to the input sequencing file.
        primer_sequences: Path to the primer sequences file.
        output_trimmed_sequences: Path to the output trimmed sequences file.
        additional_params (optional): Additional parameters for ptrimmer.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/ptrimmer",
        inputs={
            "input_sequences": input_sequences,
            "primer_sequences": primer_sequences,
        },
        outputs={"output_trimmed_sequences": output_trimmed_sequences},
        params={"additional_params": additional_params} if additional_params else {},
         
    )


@collect_tool()
def ptrimmer(
    *,
    input_sequences: str,
    primer_sequences: str,
    output_trimmed_sequences: str,
    additional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Tool to trim off the primer sequence from multiplex amplicon sequencing.

    Args:
        input_sequences: Path to the input sequencing file.
        primer_sequences: Path to the primer sequences file.
        output_trimmed_sequences: Path to the output trimmed sequences file.
        additional_params (optional): Additional parameters for ptrimmer.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_ptrimmer(
        input_sequences=input_sequences,
        primer_sequences=primer_sequences,
        output_trimmed_sequences=output_trimmed_sequences,
        additional_params=additional_params,
         
    )
