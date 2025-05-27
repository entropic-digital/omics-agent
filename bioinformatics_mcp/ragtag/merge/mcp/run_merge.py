from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_merge(
    *,
    ref: str,
    agps: str,
    fasta: str,
    agp: str,
    bam: Optional[str] = None,
    links: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Scaffold merging.

    Args:
        ref: Assembly fasta file (uncompressed or bgzipped).
        agps: Scaffolding AGP files.
        fasta: The merged scaffolds in FASTA format.
        agp: The merged scaffold results in AGP format.
        bam (optional): Hi-C alignments in BAM format.
        links (optional): If Hi-C alignments in BAM format were given.
        extra (optional): Additional parameters. Do not use with '-b'; add the bam file to input instead.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"ref": ref, "agps": agps}
    if bam:
        inputs["bam"] = bam
    outputs = {"fasta": fasta, "agp": agp}
    if links:
        outputs["links"] = links
    params = {"extra": extra} if extra else {}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/ragtag/merge",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def merge(
    *,
    ref: str,
    agps: str,
    fasta: str,
    agp: str,
    bam: Optional[str] = None,
    links: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Scaffold merging.

    Args:
        ref: Assembly fasta file (uncompressed or bgzipped).
        agps: Scaffolding AGP files.
        fasta: The merged scaffolds in FASTA format.
        agp: The merged scaffold results in AGP format.
        bam (optional): Hi-C alignments in BAM format.
        links (optional): If Hi-C alignments in BAM format were given.
        extra (optional): Additional parameters. Do not use with '-b'; add the bam file to input instead.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_merge(
        ref=ref,
        agps=agps,
        fasta=fasta,
        agp=agp,
        bam=bam,
        links=links,
        extra=extra,
         
    )
