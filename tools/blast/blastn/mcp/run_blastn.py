from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_blastn(
    *,
    query: str,
    blastdb: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Blastn performs a sequence similarity search of nucleotide query sequences against a nucleotide database.

    Args:
        query: Path to the query file (FASTA file, bare sequence file or identifiers).
        blastdb: Path to the BLAST database to query against.
        output: Path to the result file depending on the formatting option selected.
        extra (optional): Additional parameters for the BLASTN tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/blast/blastn",
        inputs=dict(query=query, blastdb=blastdb),
        outputs=dict(output=output),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def blastn(
    *,
    query: str,
    blastdb: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Blastn performs a sequence similarity search of nucleotide query sequences against a nucleotide database.

    Args:
        query: Path to the query file (FASTA file, bare sequence file or identifiers).
        blastdb: Path to the BLAST database to query against.
        output: Path to the result file depending on the formatting option selected.
        extra (optional): Additional parameters for the BLASTN tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_blastn(
        query=query, blastdb=blastdb, output=output, extra=extra,      
    )
