from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_ids(
    *,
    graph: str,
    output: str,
    device: Optional[str] = None,
    gfa_output: Optional[bool] = False,
    sort: Optional[bool] = True,
    compact: Optional[bool] = False,
    drop_names: Optional[bool] = False,
     
) -> subprocess.CompletedProcess:
    """
    Manipulate id space of input graphs.

    Args:
        graph: Input graph file (required).
        output: Output graph file (required).
        device (optional): The compute device to use. Default is None.
        gfa_output (optional): If True, output in GFA format. Default is False.
        sort (optional): Sort graph by ID. Default is True.
        compact (optional): Make the ID space compact. Default is False.
        drop_names (optional): Drop node name mappings. Default is False.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/vg/ids",
        inputs=dict(graph=graph),
        outputs=dict(output=output),
        params={
            "device": device,
            "gfa_output": gfa_output,
            "sort": sort,
            "compact": compact,
            "drop_names": drop_names,
        },
         
    )


@collect_tool()
def ids(
    *,
    graph: str,
    output: str,
    device: Optional[str] = None,
    gfa_output: Optional[bool] = False,
    sort: Optional[bool] = True,
    compact: Optional[bool] = False,
    drop_names: Optional[bool] = False,
     
) -> subprocess.CompletedProcess:
    """
    Manipulate id space of input graphs.

    Args:
        graph: Input graph file (required).
        output: Output graph file (required).
        device (optional): The compute device to use. Default is None.
        gfa_output (optional): If True, output in GFA format. Default is False.
        sort (optional): Sort graph by ID. Default is True.
        compact (optional): Make the ID space compact. Default is False.
        drop_names (optional): Drop node name mappings. Default is False.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_ids(
        graph=graph,
        output=output,
        device=device,
        gfa_output=gfa_output,
        sort=sort,
        compact=compact,
        drop_names=drop_names,
         
    )
