from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_annotate(
    *,
    input_vcf: str,
    output_vcf: str,
    cache_dir: str,
    species: str,
    assembly: str,
    offline: bool = False,
    custom_annotations: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Annotate variant calls with VEP.

    Args:
        input_vcf: Path to the input VCF file.
        output_vcf: Path to the output VCF file.
        cache_dir: Directory containing VEP cache.
        species: Species name, e.g., 'homo_sapiens'.
        assembly: Genome assembly version, e.g., 'GRCh38'.
        offline (optional): Whether to run VEP in offline mode. Default is False.
        custom_annotations (optional): Path to custom annotation files. Default is None.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "input_vcf": input_vcf,
    }
    outputs = {
        "output_vcf": output_vcf,
    }
    params = {
        "cache_dir": cache_dir,
        "species": species,
        "assembly": assembly,
        "offline": offline,
    }
    if custom_annotations:
        params["custom_annotations"] = custom_annotations

    return run_snake_wrapper(
        wrapper="file:tools/vep/annotate",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def annotate(
    *,
    input_vcf: str,
    output_vcf: str,
    cache_dir: str,
    species: str,
    assembly: str,
    offline: bool = False,
    custom_annotations: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Annotate variant calls with VEP.

    Args:
        input_vcf: Path to the input VCF file.
        output_vcf: Path to the output VCF file.
        cache_dir: Directory containing VEP cache.
        species: Species name, e.g., 'homo_sapiens'.
        assembly: Genome assembly version, e.g., 'GRCh38'.
        offline (optional): Whether to run VEP in offline mode. Default is False.
        custom_annotations (optional): Path to custom annotation files. Default is None.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_annotate(
        input_vcf=input_vcf,
        output_vcf=output_vcf,
        cache_dir=cache_dir,
        species=species,
        assembly=assembly,
        offline=offline,
        custom_annotations=custom_annotations,
         
    )
