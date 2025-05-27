from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_snp_mutator(
    *,
    reference_genome: str,
    output_directory: str,
    mutation_rate: float,
    snp_seed: Optional[int] = None,
    log_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate mutated sequence files from a reference genome.

    Args:
        reference_genome: Path to the reference genome file.
        output_directory: Directory where the mutated sequence files will be written.
        mutation_rate: Mutation rate to apply to the reference genome.
        snp_seed (optional): Seed value for reproducibility of mutations (default: None).
        log_file (optional): Path to the log file to capture output (default: None).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "mutation_rate": mutation_rate,
        "snp_seed": snp_seed,
        "log_file": log_file,
    }
    filtered_params = {k: v for k, v in params.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/snp-mutator",
        inputs={"reference_genome": reference_genome},
        outputs={"output_directory": output_directory},
        params=filtered_params,
         
    )


@collect_tool()
def snp_mutator(
    *,
    reference_genome: str,
    output_directory: str,
    mutation_rate: float,
    snp_seed: Optional[int] = None,
    log_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Generate mutated sequence files from a reference genome.

    Args:
        reference_genome: Path to the reference genome file.
        output_directory: Directory where the mutated sequence files will be written.
        mutation_rate: Mutation rate to apply to the reference genome.
        snp_seed (optional): Seed value for reproducibility of mutations (default: None).
        log_file (optional): Path to the log file to capture output (default: None).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snp_mutator(
        reference_genome=reference_genome,
        output_directory=output_directory,
        mutation_rate=mutation_rate,
        snp_seed=snp_seed,
        log_file=log_file,
         
    )
