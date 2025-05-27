from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_genomepy(
    *,
    provider: Optional[str] = "UCSC",
    output_assembly: str,
    optional_output_annotation: Optional[str] = None,
    optional_output_blacklist: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Download genomes the easy way:
    https://github.com/vanheeringen-lab/genomepy

    Args:
        provider (optional): Which provider to download from, defaults to UCSC (choose from UCSC, Ensembl, NCBI).
        output_assembly: The assembly name for the genome files (e.g., hg38, mm10).
        optional_output_annotation (optional): Annotation output path {assembly}/{assembly}.annotation.gtf.
        optional_output_blacklist (optional): Blacklist output path {assembly}/{assembly}.blacklist.bed.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {"provider": provider}
    outputs = {
        "assembly": f"{output_assembly}/{output_assembly}.fa",
        "index": f"{output_assembly}/{output_assembly}.fa.fai",
        "gaps": f"{output_assembly}/{output_assembly}.gaps.bed",
        "sizes": f"{output_assembly}/{output_assembly}.fa.sizes",
    }
    if optional_output_annotation:
        outputs["annotation"] = optional_output_annotation
    if optional_output_blacklist:
        outputs["blacklist"] = optional_output_blacklist

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/genomepy",
        inputs={},
        params=params,
        outputs=outputs,
         
    )


@collect_tool()
def genomepy(
    *,
    provider: Optional[str] = "UCSC",
    output_assembly: str,
    optional_output_annotation: Optional[str] = None,
    optional_output_blacklist: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Download genomes the easy way:
    https://github.com/vanheeringen-lab/genomepy

    Args:
        provider (optional): Which provider to download from, defaults to UCSC (choose from UCSC, Ensembl, NCBI).
        output_assembly: The assembly name for the genome files (e.g., hg38, mm10).
        optional_output_annotation (optional): Annotation output path {assembly}/{assembly}.annotation.gtf.
        optional_output_blacklist (optional): Blacklist output path {assembly}/{assembly}.blacklist.bed.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_genomepy(
        provider=provider,
        output_assembly=output_assembly,
        optional_output_annotation=optional_output_annotation,
        optional_output_blacklist=optional_output_blacklist,
         
    )
