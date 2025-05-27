from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_graph(
    *,
    bedgraph_file: str,
    pretext_contact_map: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Embeds bedgraph data into Pretext contact maps.

    Args:
        bedgraph_file: Path to the input BEDgraph file.
        pretext_contact_map: Path to the output Pretext contact map.
        extra (optional): Additional arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/pretext/graph",
        inputs=dict(bedgraph_file=bedgraph_file),
        outputs=dict(pretext_contact_map=pretext_contact_map),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def graph(
    *,
    bedgraph_file: str,
    pretext_contact_map: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Embeds bedgraph data into Pretext contact maps.

    Args:
        bedgraph_file: Path to the input BEDgraph file.
        pretext_contact_map: Path to the output Pretext contact map.
        extra (optional): Additional arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_graph(
        bedgraph_file=bedgraph_file,
        pretext_contact_map=pretext_contact_map,
        extra=extra,
         
    )
