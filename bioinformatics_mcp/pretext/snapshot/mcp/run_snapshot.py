from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_snapshot(
    *,
    pretext_contact_map: str,
    full_image: str,
    all_images: Optional[str] = None,
    specific_sequences: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Commandline image generator for Pretext contact maps.

    Args:
        pretext_contact_map: Path to the pretext contact map.
        full_image: Path for the generated full image (mandatory output).
        all_images (optional): Path for all generated images (optional output).
        specific_sequences (optional): Path for specific sequence images (optional output).
        extra (optional): Additional arguments for customization.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "full_image": full_image,
    }
    if all_images:
        params["all_images"] = all_images
    if specific_sequences:
        params["specific_sequences"] = specific_sequences
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/pretext/snapshot",
        inputs={"pretext_contact_map": pretext_contact_map},
        params=params,
         
    )


@collect_tool()
def snapshot(
    *,
    pretext_contact_map: str,
    full_image: str,
    all_images: Optional[str] = None,
    specific_sequences: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Commandline image generator for Pretext contact maps.

    Args:
        pretext_contact_map: Path to the pretext contact map.
        full_image: Path for the generated full image (mandatory output).
        all_images (optional): Path for all generated images (optional output).
        specific_sequences (optional): Path for specific sequence images (optional output).
        extra (optional): Additional arguments for customization.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snapshot(
        pretext_contact_map=pretext_contact_map,
        full_image=full_image,
        all_images=all_images,
        specific_sequences=specific_sequences,
        extra=extra,
         
    )
