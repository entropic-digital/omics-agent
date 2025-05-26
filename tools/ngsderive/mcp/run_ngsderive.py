from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_ngsderive(
    *,
    ngs: str,
    gene_model: str,
    tsv: str,
    subcommand: str,
    junctions: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Backwards computing information from next-generation sequencing data and annotating splice junctions.

    Args:
        ngs: Path to BAM/SAM/Fastq file. SAM/BAM files should be indexed.
        gene_model: Path to sorted GTF/GFF file. Should be tabix indexed.
        tsv: Path to output file.
        subcommand: Name of the `ngsderive` subcommand.
        junctions (optional): Optional path to junction directory, or list of paths to junction files with a common prefix.
        extra (optional): Additional parameters, besides `-o`, `-g`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/ngsderive",
        inputs=dict(ngs=ngs, gene_model=gene_model),
        outputs=dict(tsv=tsv, junctions=junctions) if junctions else dict(tsv=tsv),
        params={"subcommand": subcommand, "extra": extra}
        if extra
        else {"subcommand": subcommand},
         
    )


@collect_tool()
def ngsderive(
    *,
    ngs: str,
    gene_model: str,
    tsv: str,
    subcommand: str,
    junctions: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Backwards computing information from next-generation sequencing data and annotating splice junctions.

    Args:
        ngs: Path to BAM/SAM/Fastq file. SAM/BAM files should be indexed.
        gene_model: Path to sorted GTF/GFF file. Should be tabix indexed.
        tsv: Path to output file.
        subcommand: Name of the `ngsderive` subcommand.
        junctions (optional): Optional path to junction directory, or list of paths to junction files with a common prefix.
        extra (optional): Additional parameters, besides `-o`, `-g`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_ngsderive(
        ngs=ngs,
        gene_model=gene_model,
        tsv=tsv,
        subcommand=subcommand,
        junctions=junctions,
        extra=extra,
         
    )
