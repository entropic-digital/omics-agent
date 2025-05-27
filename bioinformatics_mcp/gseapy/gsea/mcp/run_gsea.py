from typing import Optional, Dict
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_gsea(
    *,
    gmt: Optional[str] = None,
    expr: Optional[str] = None,
    cls: Optional[str] = None,
    rank: Optional[str] = None,
    gene_list: Optional[str] = None,
    background: Optional[str] = None,
    outdir: str,
    pkl: str,
    extra: Optional[Dict] = None,
    gene_sets: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GSEApy, a Gene Set Enrichment Analysis tool in Python.

    Args:
        gmt (optional): Path to gene sets (GMT formatted). If None, a `gene_sets` value must be provided.
        expr (optional): Path to expression table, required for `gsea` and `ssgsea` (RNK formatted).
        cls (optional): Path to categorical class file, required for `gsea` (CLS formatted).
        rank (optional): Path to pre-ranked genes, required for `prerank` (TSV/CSV formatted).
        gene_list (optional): Path to gene list file, required for `enrichr` (TXT/TSV/CSV formatted).
        background (optional): Path to background file for `enrichr` (TXT/TSV/CSV formatted).
        outdir: Path to output directory.
        pkl: Path to serialized results (Pickle).
        extra (optional): Dictionary of arguments given to GSEApy's subfunction besides IO and threading options.
        gene_sets (optional): Non-file gene set names from Biomart.
  
    Returns:
        CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gseapy/gsea",
        inputs={
            "gmt": gmt,
            "expr": expr,
            "cls": cls,
            "rank": rank,
            "gene_list": gene_list,
            "background": background,
        },
        outputs={
            "outdir": outdir,
            "pkl": pkl,
        },
        params={
            "extra": extra if extra else {},
            "gene_sets": gene_sets,
        },
         
    )


@collect_tool()
def gsea(
    *,
    gmt: Optional[str] = None,
    expr: Optional[str] = None,
    cls: Optional[str] = None,
    rank: Optional[str] = None,
    gene_list: Optional[str] = None,
    background: Optional[str] = None,
    outdir: str,
    pkl: str,
    extra: Optional[Dict] = None,
    gene_sets: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run GSEApy, a Gene Set Enrichment Analysis tool in Python.

    Args:
        gmt (optional): Path to gene sets (GMT formatted). If None, a `gene_sets` value must be provided.
        expr (optional): Path to expression table, required for `gsea` and `ssgsea` (RNK formatted).
        cls (optional): Path to categorical class file, required for `gsea` (CLS formatted).
        rank (optional): Path to pre-ranked genes, required for `prerank` (TSV/CSV formatted).
        gene_list (optional): Path to gene list file, required for `enrichr` (TXT/TSV/CSV formatted).
        background (optional): Path to background file for `enrichr` (TXT/TSV/CSV formatted).
        outdir: Path to output directory.
        pkl: Path to serialized results (Pickle).
        extra (optional): Dictionary of arguments given to GSEApy's subfunction besides IO and threading options.
        gene_sets (optional): Non-file gene set names from Biomart.
  
    Returns:
        CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_gsea(
        gmt=gmt,
        expr=expr,
        cls=cls,
        rank=rank,
        gene_list=gene_list,
        background=background,
        outdir=outdir,
        pkl=pkl,
        extra=extra,
        gene_sets=gene_sets,
         
    )
