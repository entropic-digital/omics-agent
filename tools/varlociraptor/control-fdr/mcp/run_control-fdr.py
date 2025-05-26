from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_control_fdr(
    *,
    input_file: str,
    output_file: str,
    fdr: Optional[float] = None,
     
) -> subprocess.CompletedProcess:
    """
    Control false discovery rate of Varlociraptor calls.

    Args:
        input_file: The BCF/VCF file with Varlociraptor calls.
        output_file: The filtered BCF/VCF file with Varlociraptor calls such that the given FDR is not exceeded.
        fdr (optional): The desired false discovery rate to control.
  
    Returns:
        CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/varlociraptor/control-fdr",
        inputs=dict(input_file=input_file),
        outputs=dict(output_file=output_file),
        params={"fdr": fdr} if fdr is not None else {},
         
    )


@collect_tool()
def control_fdr(
    *,
    input_file: str,
    output_file: str,
    fdr: Optional[float] = None,
     
) -> subprocess.CompletedProcess:
    """
    Control false discovery rate of Varlociraptor calls.

    Args:
        input_file: The BCF/VCF file with Varlociraptor calls.
        output_file: The filtered BCF/VCF file with Varlociraptor calls such that the given FDR is not exceeded.
        fdr (optional): The desired false discovery rate to control.
  
    Returns:
        CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_control_fdr(
        input_file=input_file,
        output_file=output_file,
        fdr=fdr,
         
    )
