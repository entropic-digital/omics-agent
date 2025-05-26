from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_jackhmmer(
    *,
    query: str,
    db: str,
    hits_tbl: Optional[str] = None,
    hits_aln: Optional[str] = None,
    dom_tbl: Optional[str] = None,
    summary: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Search profile(s) against a sequence database using jackhmmer.

    Args:
        query: Query file in FASTA format.
        db: Database file in FASTA format.
        hits_tbl (optional): Table of per-sequence hits.
        hits_aln (optional): Multiple sequence alignment (MSA) in Stockholm format of all significant hits.
        dom_tbl (optional): Table of per-domain hits.
        summary (optional): Human-readable output.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"query": query, "db": db}
    outputs = {
        key: value
        for key, value in {
            "hits_tbl": hits_tbl,
            "hits_aln": hits_aln,
            "dom_tbl": dom_tbl,
            "summary": summary,
        }.items()
        if value is not None
    }
    return run_snake_wrapper(
        wrapper="file:tools/hmmer/jackhmmer",
        inputs=inputs,
        outputs=outputs,
         
    )


@collect_tool()
def jackhmmer(
    *,
    query: str,
    db: str,
    hits_tbl: Optional[str] = None,
    hits_aln: Optional[str] = None,
    dom_tbl: Optional[str] = None,
    summary: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Search profile(s) against a sequence database using jackhmmer.

    Args:
        query: Query file in FASTA format.
        db: Database file in FASTA format.
        hits_tbl (optional): Table of per-sequence hits.
        hits_aln (optional): Multiple sequence alignment (MSA) in Stockholm format of all significant hits.
        dom_tbl (optional): Table of per-domain hits.
        summary (optional): Human-readable output.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_jackhmmer(
        query=query,
        db=db,
        hits_tbl=hits_tbl,
        hits_aln=hits_aln,
        dom_tbl=dom_tbl,
        summary=summary,
         
    )
