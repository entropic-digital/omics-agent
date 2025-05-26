from typing import Optional, Union, List
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_sort(
    *,
    input_bus_files: Union[str, List[str]],
    output_bus_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Sort raw BUS output from pseudoalignment programs.

    Args:
        input_bus_files: Path to a BUS file, or a list of BUS files to sort.
        output_bus_file: Path to the output BUS file.
        extra (optional): Additional parameters to pass to the sorting tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    # Ensure input_bus_files is consistently a list
    if isinstance(input_bus_files, str):
        input_bus_files = [input_bus_files]

    return run_snake_wrapper(
        wrapper="file:tools/bustools/sort",
        inputs={"bus_files": input_bus_files},
        outputs={"sorted_bus_file": output_bus_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def sort_tool(
    *,
    input_bus_files: Union[str, List[str]],
    output_bus_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Sort raw BUS output from pseudoalignment programs.

    Args:
        input_bus_files: Path to a BUS file, or a list of BUS files to sort.
        output_bus_file: Path to the output BUS file.
        extra (optional): Additional parameters to pass to the sorting tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_sort(
        input_bus_files=input_bus_files,
        output_bus_file=output_bus_file,
        extra=extra,
         
    )
