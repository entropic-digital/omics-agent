from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_gcsa(
    *,
    graph: str,
    gbwt: Optional[str] = None,
    out_gcsa: str,
    out_lcp: Optional[str] = None,
    temp_dir: Optional[str] = None,
    kmer_size: int = 16,
    doubling_steps: int = 2,
     
) -> subprocess.CompletedProcess:
    """
    Build GCSA index for variation graphs.

    Args:
        graph: Input variation graph file (VG format).
        gbwt (optional): Input GBWT file for haplotype-aware indexing.
        out_gcsa: Output GCSA index file.
        out_lcp (optional): Output LCP array file.
        temp_dir (optional): Directory for temporary files.
        kmer_size: K-mer size to use for indexing. Default is 16.
        doubling_steps: Number of times k-mer size doubles. Default is 2.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/vg/index/gcsa",
        inputs=dict(graph=graph, gbwt=gbwt),
        outputs=dict(out_gcsa=out_gcsa, out_lcp=out_lcp),
        params={
            "temp_dir": temp_dir,
            "kmer_size": kmer_size,
            "doubling_steps": doubling_steps,
        },
         
    )


@collect_tool()
def gcsa_tool(
    *,
    graph: str,
    gbwt: Optional[str] = None,
    out_gcsa: str,
    out_lcp: Optional[str] = None,
    temp_dir: Optional[str] = None,
    kmer_size: int = 16,
    doubling_steps: int = 2,
     
) -> subprocess.CompletedProcess:
    """
    Build GCSA index for variation graphs.

    Args:
        graph: Input variation graph file (VG format).
        gbwt (optional): Input GBWT file for haplotype-aware indexing.
        out_gcsa: Output GCSA index file.
        out_lcp (optional): Output LCP array file.
        temp_dir (optional): Directory for temporary files.
        kmer_size: K-mer size to use for indexing. Default is 16.
        doubling_steps: Number of times k-mer size doubles. Default is 2.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_gcsa(
        graph=graph,
        gbwt=gbwt,
        out_gcsa=out_gcsa,
        out_lcp=out_lcp,
        temp_dir=temp_dir,
        kmer_size=kmer_size,
        doubling_steps=doubling_steps,
         
    )
