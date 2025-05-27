from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_call_variants(
    *,
    preprocessed_observations: str,
    scenario: str,
    variant_calls: str,
     
) -> subprocess.CompletedProcess:
    """
    Call variants with Varlociraptor using a given scenario.

    Args:
        preprocessed_observations: Path to the preprocessed observations for the samples in the scenario.
                                   If a sample is omitted, it will be treated as if there are no observations available.
        scenario: Path to the scenario file.
        variant_calls: Path where the variant call results should be stored.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/varlociraptor/call-variants",
        inputs=dict(
            preprocessed_observations=preprocessed_observations,
            scenario=scenario,
        ),
        outputs=dict(variant_calls=variant_calls),
        params={},
         
    )


@collect_tool()
def call_variants(
    *,
    preprocessed_observations: str,
    scenario: str,
    variant_calls: str,
     
) -> subprocess.CompletedProcess:
    """
    Call variants with Varlociraptor using a given scenario.

    Args:
        preprocessed_observations: Path to the preprocessed observations for the samples in the scenario.
                                   If a sample is omitted, it will be treated as if there are no observations available.
        scenario: Path to the scenario file.
        variant_calls: Path where the variant call results should be stored.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_call_variants(
        preprocessed_observations=preprocessed_observations,
        scenario=scenario,
        variant_calls=variant_calls,
         
    )
