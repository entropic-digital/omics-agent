from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_efetch(
    *,
    db: str,
    id: Optional[str] = None,
    rettype: Optional[str] = None,
    retmode: Optional[str] = None,
    seq_start: Optional[str] = None,
    seq_stop: Optional[str] = None,
    strand: Optional[str] = None,
    complexity: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Obtain data from NCBI and Genbank using Entrez efetch.

    Args:
        db: The database to fetch information from (e.g., nucleotide, protein).
        id (optional): A unique identifier, such as Accession or GI.
        rettype (optional): The format to retrieve data in (e.g., fasta, gb).
        retmode (optional): The mode of the returned data (e.g., text, xml).
        seq_start (optional): Start position for a sequence range.
        seq_stop (optional): Stop position for a sequence range.
        strand (optional): Strand to use (1 for plus, 2 for minus).
        complexity (optional): Level of complexity for the retrieved data.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/entrez/efetch",
        inputs=dict(db=db),
        params={
            "id": id,
            "rettype": rettype,
            "retmode": retmode,
            "seq_start": seq_start,
            "seq_stop": seq_stop,
            "strand": strand,
            "complexity": complexity,
        },
         
    )


@collect_tool()
def efetch(
    *,
    db: str,
    id: Optional[str] = None,
    rettype: Optional[str] = None,
    retmode: Optional[str] = None,
    seq_start: Optional[str] = None,
    seq_stop: Optional[str] = None,
    strand: Optional[str] = None,
    complexity: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Obtain data from NCBI and Genbank using Entrez efetch.

    Args:
        db: The database to fetch information from (e.g., nucleotide, protein).
        id (optional): A unique identifier, such as Accession or GI.
        rettype (optional): The format to retrieve data in (e.g., fasta, gb).
        retmode (optional): The mode of the returned data (e.g., text, xml).
        seq_start (optional): Start position for a sequence range.
        seq_stop (optional): Stop position for a sequence range.
        strand (optional): Strand to use (1 for plus, 2 for minus).
        complexity (optional): Level of complexity for the retrieved data.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_efetch(
        db=db,
        id=id,
        rettype=rettype,
        retmode=retmode,
        seq_start=seq_start,
        seq_stop=seq_stop,
        strand=strand,
        complexity=complexity,
         
    )
