from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_makesplicedintronic(
    *,
    gtf: str,
    fasta: str,
    spliced: Optional[str] = None,
    unspliced: Optional[str] = None,
    fasta_output: str,
    gene_id_to_name: str,
    t2g: str,
    read_length: int = 100,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Build splici reference files for Alevin-fry.

    Args:
        gtf: Path to the genome annotation (GTF formatted).
        fasta: Path to the genome sequence (Fasta formatted).
        spliced (optional): Path to additional spliced sequences (Fasta formatted).
        unspliced (optional): Path to unspliced sequences (Fasta formatted).
        fasta_output: Path to spliced+intronic sequences (Fasta formatted).
        gene_id_to_name: Path to a TSV formatted text file containing gene_id <-> gene_name correspondence.
        t2g: Path to a TSV formatted text file containing transcript_id <-> gene_name <-> splicing status correspondence.
        read_length: The read length of the single-cell experiment being processed (determines flank size). Default is 100.
        extra (optional): Additional parameters to be passed to pyroe.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/pyroe/makesplicedintronic",
        inputs=dict(
            gtf=gtf,
            fasta=fasta,
            spliced=spliced,
            unspliced=unspliced,
        ),
        outputs=dict(
            fasta=fasta_output,
            gene_id_to_name=gene_id_to_name,
            t2g=t2g,
        ),
        params={
            "read_length": read_length,
            "extra": extra,
        },
         
    )


@collect_tool()
def makesplicedintronic(
    *,
    gtf: str,
    fasta: str,
    spliced: Optional[str] = None,
    unspliced: Optional[str] = None,
    fasta_output: str,
    gene_id_to_name: str,
    t2g: str,
    read_length: int = 100,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Build splici reference files for Alevin-fry.

    Args:
        gtf: Path to the genome annotation (GTF formatted).
        fasta: Path to the genome sequence (Fasta formatted).
        spliced (optional): Path to additional spliced sequences (Fasta formatted).
        unspliced (optional): Path to unspliced sequences (Fasta formatted).
        fasta_output: Path to spliced+intronic sequences (Fasta formatted).
        gene_id_to_name: Path to a TSV formatted text file containing gene_id <-> gene_name correspondence.
        t2g: Path to a TSV formatted text file containing transcript_id <-> gene_name <-> splicing status correspondence.
        read_length: The read length of the single-cell experiment being processed (determines flank size). Default is 100.
        extra (optional): Additional parameters to be passed to pyroe.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_makesplicedintronic(
        gtf=gtf,
        fasta=fasta,
        spliced=spliced,
        unspliced=unspliced,
        fasta_output=fasta_output,
        gene_id_to_name=gene_id_to_name,
        t2g=t2g,
        read_length=read_length,
        extra=extra,
         
    )
