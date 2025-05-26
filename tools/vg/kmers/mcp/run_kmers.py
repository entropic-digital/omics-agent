from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_kmers(
    *,
    input_vg: str,
    output_kmers: str,
    k: int,
    graph_name: str,
    include_reverse: bool = True,
     
) -> subprocess.CompletedProcess:
    """
    Generates kmers from both strands of variation graphs.

    Args:
        input_vg: Path to the input variation graph file.
        output_kmers: Path to the output kmers file.
        k: Length of the kmers to generate.
        graph_name: Name of the graph.
        include_reverse (optional): Whether to include reverse strands. Default is True.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/vg/kmers",
        inputs={"input_vg": input_vg},
        outputs={"output_kmers": output_kmers},
        params={
            "k": k,
            "graph_name": graph_name,
            "include_reverse": include_reverse,
        },
         
    )


@collect_tool()
def kmers(
    *,
    input_vg: str,
    output_kmers: str,
    k: int,
    graph_name: str,
    include_reverse: bool = True,
     
) -> subprocess.CompletedProcess:
    """
    Generates kmers from both strands of variation graphs.

    Args:
        input_vg: Path to the input variation graph file.
        output_kmers: Path to the output kmers file.
        k: Length of the kmers to generate.
        graph_name: Name of the graph.
        include_reverse (optional): Whether to include reverse strands. Default is True.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_kmers(
        input_vg=input_vg,
        output_kmers=output_kmers,
        k=k,
        graph_name=graph_name,
        include_reverse=include_reverse,
         
    )
