from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_simulator(
    *,
    input_model: str,
    output_reads: str,
    input_reference_genome: Optional[str] = None,
    output_unaligned_reads: Optional[str] = None,
    params_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    NanoSim simulator.

    NanoSim is a simulator of Oxford Nanopore reads that captures the
    technology-specific features of ONT data, and allows for adjustments upon
    improvement of Nanopore sequencing technology.

    Args:
        input_model: Path to the model used for simulation.
        output_reads: Path to save the simulated reads.
        input_reference_genome (optional): Path to the reference genome, required for some modes.
        output_unaligned_reads (optional): Path to save unaligned reads with errors.
        params_extra (optional): Extra parameters passed verbatim to the simulator.
  
    Notes:
        - Wrapper automatically sets flags based on the given input and output types.
        - Ensure the model matches the training data if a reference genome is used for transcriptome simulation.
        - For metagenome mode, multiple samples require separate wrapper executions.
        - Refer to NanoSim documentation for additional details on modes and outputs.

    Returns:
        CompletedProcess instance containing information about the completed simulation process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/nanosim/simulator",
        inputs={
            "model": input_model,
            "reference_genome": input_reference_genome,
        },
        outputs={
            "reads": output_reads,
            "unaligned_reads": output_unaligned_reads,
        },
        params={
            "extra": params_extra,
        },
         
    )


@collect_tool()
def simulator(
    *,
    input_model: str,
    output_reads: str,
    input_reference_genome: Optional[str] = None,
    output_unaligned_reads: Optional[str] = None,
    params_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    NanoSim simulator (decorated function).

    NanoSim is a simulator of Oxford Nanopore reads that captures the
    technology-specific features of ONT data, and allows for adjustments upon
    improvement of Nanopore sequencing technology.

    Args:
        input_model: Path to the model used for simulation.
        output_reads: Path to save the simulated reads.
        input_reference_genome (optional): Path to the reference genome, required for some modes.
        output_unaligned_reads (optional): Path to save unaligned reads with errors.
        params_extra (optional): Extra parameters passed verbatim to the simulator.
  
    Notes:
        - Wrapper automatically sets flags based on the given input and output types.
        - Ensure the model matches the training data if a reference genome is used for transcriptome simulation.
        - For metagenome mode, multiple samples require separate wrapper executions.
        - Refer to NanoSim documentation for additional details on modes and outputs.

    Returns:
        CompletedProcess instance containing information about the completed simulation process.
    """
    return run_simulator(
        input_model=input_model,
        output_reads=output_reads,
        input_reference_genome=input_reference_genome,
        output_unaligned_reads=output_unaligned_reads,
        params_extra=params_extra,
         
    )
