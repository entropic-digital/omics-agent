from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_collapse_nomismatch(
    *,
    input_rds: str,
    output_rds: str,
    optional_params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Combine sequences that are identical up to shifts and/or indels using DADA2's collapseNoMismatch function.

    Args:
        input_rds: Path to the input RDS file containing the chimera-free sequence table.
        output_rds: Path to the output RDS file where the collapsed sequence table will be saved.
        optional_params (optional): Optional arguments for collapseNoMismatch as a dictionary of key-value pairs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/dada2/collapse-nomismatch",
        inputs={"input_rds": input_rds},
        outputs={"output_rds": output_rds},
        params=optional_params if optional_params else {},
         
    )


@collect_tool()
def collapse_nomismatch(
    *,
    input_rds: str,
    output_rds: str,
    optional_params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Combine sequences that are identical up to shifts and/or indels using DADA2's collapseNoMismatch function.

    Args:
        input_rds: Path to the input RDS file containing the chimera-free sequence table.
        output_rds: Path to the output RDS file where the collapsed sequence table will be saved.
        optional_params (optional): Optional arguments for collapseNoMismatch as a dictionary of key-value pairs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collapse_nomismatch(
        input_rds=input_rds,
        output_rds=output_rds,
        optional_params=optional_params,
         
    )
