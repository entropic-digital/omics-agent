import subprocess
from typing import Optional

from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper
from bioinformatics_mcp.tool_decorator import collect_tool


def run_barrnap(
    *,
    fasta: str,
    gff: str,
    fasta_output: Optional[str] = None,
    extra: Optional[str] = None,
    kingdom: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    BAsic Rapid Ribosomal RNA Predictor (Barrnap).

    Args:
        fasta: Path to the input query FASTA file.
        gff: Path to the output GFF3 file containing rRNA locations.
        fasta_output (optional): Path to the optional output FASTA file containing hit sequences.
        extra (optional): Additional parameters to pass to Barrnap.
        kingdom (optional): Database to use, either Bacteria (`bac`), Archaea (`arc`), Eukaryota (`euk`),
                            or Metazoan Mitochondria (`mito`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"fasta": fasta}
    outputs = {"gff": gff}
    if fasta_output:
        outputs["fasta"] = fasta_output

    params = {}
    if extra:
        params["extra"] = extra
    if kingdom:
        params["kingdom"] = kingdom

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/barrnap",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def barrnap(
    *,
    fasta: str,
    gff: str,
    fasta_output: Optional[str] = None,
    extra: Optional[str] = None,
    kingdom: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    BAsic Rapid Ribosomal RNA Predictor (Barrnap).

    Args:
        fasta: Path to the input query FASTA file.
        gff: Path to the output GFF3 file containing rRNA locations.
        fasta_output (optional): Path to the optional output FASTA file containing hit sequences.
        extra (optional): Additional parameters to pass to Barrnap.
        kingdom (optional): Database to use, either Bacteria (`bac`), Archaea (`arc`), Eukaryota (`euk`),
                            or Metazoan Mitochondria (`mito`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_barrnap(
        fasta=fasta,
        gff=gff,
        fasta_output=fasta_output,
        extra=extra,
        kingdom=kingdom,
         
    )
