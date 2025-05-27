from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_prune(
    *,
    vg_graph: str,
    output_graph: str,
    threads: Optional[int] = 1,
    mapping_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Prunes the complex regions of the graph for GCSA2 indexing.

    Args:
        vg_graph: Path to the input VG graph file.
        output_graph: Path to the output pruned graph file.
        threads (optional): Number of threads to use (default is 1).
        mapping_file (optional): Path to the mapping file, if any.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/vg/prune",
        inputs=dict(vg_graph=vg_graph),
        outputs=dict(output_graph=output_graph),
        params={
            "threads": threads,
            **({"mapping_file": mapping_file} if mapping_file else {}),
        },
         
    )


@collect_tool()
def prune(
    *,
    vg_graph: str,
    output_graph: str,
    threads: Optional[int] = 1,
    mapping_file: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Prunes the complex regions of the graph for GCSA2 indexing.

    Args:
        vg_graph: Path to the input VG graph file.
        output_graph: Path to the output pruned graph file.
        threads (optional): Number of threads to use (default is 1).
        mapping_file (optional): Path to the mapping file, if any.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_prune(
        vg_graph=vg_graph,
        output_graph=output_graph,
        threads=threads,
        mapping_file=mapping_file,
         
    )
