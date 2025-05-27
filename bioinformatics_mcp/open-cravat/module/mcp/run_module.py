from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_module(
    *,
    input_file: str,
    output_dir: str,
    module_name: str,
    reference_genome: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    OpenCRAVAT module for annotating variant calls.

    Args:
        input_file: Path to the input file containing variant calls.
        output_dir: Path to the directory where results will be saved.
        module_name: Name of the OpenCRAVAT module to be used.
        reference_genome (optional): Reference genome to be used for annotation.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/open-cravat",
        inputs=dict(input_file=input_file),
        outputs=dict(output_dir=output_dir),
        params={"module_name": module_name, "reference_genome": reference_genome}
        if reference_genome
        else {"module_name": module_name},
         
    )


@collect_tool()
def module(
    *,
    input_file: str,
    output_dir: str,
    module_name: str,
    reference_genome: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    OpenCRAVAT module for annotating variant calls.

    Args:
        input_file: Path to the input file containing variant calls.
        output_dir: Path to the directory where results will be saved.
        module_name: Name of the OpenCRAVAT module to be used.
        reference_genome (optional): Reference genome to be used for annotation.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_module(
        input_file=input_file,
        output_dir=output_dir,
        module_name=module_name,
        reference_genome=reference_genome,
         
    )
