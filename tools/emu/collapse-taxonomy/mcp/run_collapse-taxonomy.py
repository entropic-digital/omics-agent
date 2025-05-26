from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_collapse_taxonomy(
    *,
    input_file: str,
    output_file: str,
    rank: Optional[str] = "species",
     
) -> subprocess.CompletedProcess:
    """
    Collapse a TSV output file generated with emu at the desired taxonomic rank.

    Args:
        input_file: A TSV output file generated with emu.
        output_file: A TSV output file collapsed at the desired taxonomic rank.
        rank (optional): Accepted ranks are 'species', 'genus', 'family', 'order',
                         'class', 'phylum', and 'superkingdom'. Defaults to 'species'.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/emu/collapse-taxonomy",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file},
        params={"rank": rank} if rank else {},
         
    )


@collect_tool()
def collapse_taxonomy(
    *,
    input_file: str,
    output_file: str,
    rank: Optional[str] = "species",
     
) -> subprocess.CompletedProcess:
    """
    Collapse a TSV output file generated with emu at the desired taxonomic rank.

    Args:
        input_file: A TSV output file generated with emu.
        output_file: A TSV output file collapsed at the desired taxonomic rank.
        rank (optional): Accepted ranks are 'species', 'genus', 'family', 'order',
                         'class', 'phylum', and 'superkingdom'. Defaults to 'species'.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collapse_taxonomy(
        input_file=input_file, output_file=output_file, rank=rank,      
    )
