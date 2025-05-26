from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_combine_outputs(
    *,
    input_tsv_files: List[str],
    abundances: str,
    taxonomy: Optional[str] = None,
    rank: str = "tax_id",
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collapse individual abundance tables TSV into a single TSV at the desired taxonomic rank.

    Args:
        input_tsv_files: List of TSV files obtained with emu abundance.
        abundances: Path to the output TSV file containing the abundance of different taxa.
        taxonomy (optional): Path to the output TSV file containing the taxonomy. If not provided, taxonomy will be included in the abundance table.
        rank: Desired taxonomic rank for agglomeration. Defaults to 'tax_id'. Accepted values are 'tax_id', 'species', 'genus', 'family', 'order', 'class', 'phylum', and 'superkingdom'. If omitted, no agglomeration will be performed.
        extra (optional): Additional arguments (e.g., '--counts').
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/emu/combine-outputs",
        inputs={"tsv": input_tsv_files},
        outputs={
            "abundances": abundances,
            "taxonomy": taxonomy,
        },
        params={
            "rank": rank,
            "extra": extra,
        },
         
    )


@collect_tool()
def combine_outputs(
    *,
    input_tsv_files: List[str],
    abundances: str,
    taxonomy: Optional[str] = None,
    rank: str = "tax_id",
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collapse individual abundance tables TSV into a single TSV at the desired taxonomic rank.

    Args:
        input_tsv_files: List of TSV files obtained with emu abundance.
        abundances: Path to the output TSV file containing the abundance of different taxa.
        taxonomy (optional): Path to the output TSV file containing the taxonomy. If not provided, taxonomy will be included in the abundance table.
        rank: Desired taxonomic rank for agglomeration. Defaults to 'tax_id'. Accepted values are 'tax_id', 'species', 'genus', 'family', 'order', 'class', 'phylum', and 'superkingdom'. If omitted, no agglomeration will be performed.
        extra (optional): Additional arguments (e.g., '--counts').
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_combine_outputs(
        input_tsv_files=input_tsv_files,
        abundances=abundances,
        taxonomy=taxonomy,
        rank=rank,
        extra=extra,
         
    )
