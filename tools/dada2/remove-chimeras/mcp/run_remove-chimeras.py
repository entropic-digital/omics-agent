from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_remove_chimeras(
    *,
    input_rds: str,
    output_rds: str,
    optional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Remove chimera sequences from the sequence table data using the
    DADA2 `removeBimeraDenovo` function.

    Args:
        input_rds: Path to the input RDS file containing the sequence table.
        output_rds: Path to the output RDS file for the chimera-free sequence table.
        optional_params (optional): Optional parameters to pass to `removeBimeraDenovo`
                                    as key=value string pairs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/dada2/remove-chimeras",
        inputs={"input_rds": input_rds},
        outputs={"output_rds": output_rds},
        params={"optional_params": optional_params} if optional_params else {},
         
    )


@collect_tool()
def remove_chimeras(
    *,
    input_rds: str,
    output_rds: str,
    optional_params: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Remove chimera sequences from the sequence table data using the
    DADA2 `removeBimeraDenovo` function.

    Args:
        input_rds: Path to the input RDS file containing the sequence table.
        output_rds: Path to the output RDS file for the chimera-free sequence table.
        optional_params (optional): Optional parameters to pass to `removeBimeraDenovo`
                                    as key=value string pairs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_remove_chimeras(
        input_rds=input_rds,
        output_rds=output_rds,
        optional_params=optional_params,
         
    )
