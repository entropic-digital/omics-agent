from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_metaspades(
    *,
    reads: str,
    output: str,
    pacbio: Optional[str] = None,
    nanopore: Optional[str] = None,
    threads: Optional[int] = 1,
    memory: Optional[int] = 16,
     
) -> subprocess.CompletedProcess:
    """
    Assemble metagenome with metaspades. For more information, see the
    `Spades documentation <https://cab.spbu.ru/software/spades/>`.

    Metagenome assembly uses a lot of computational resources. Spades is told to
    restart from a previous checkpoint if the file `params.txt` exists in the output
    directory. In this way, one can use snakemake with `--restart-times` to automatically
    restart the assembly.

    Args:
        reads: Input reads for metaspades assembly (short reads, typically paired-end).
        output: Directory to store assembly results.
        pacbio (optional): Long-read PacBio input.
        nanopore (optional): Long-read Nanopore input.
        threads (optional): Number of threads available for assembly (default: 1).
        memory (optional): Amount of memory available for assembly in GB (default: 16).
  
    Returns:
        subprocess.CompletedProcess: Instance containing details about the completed Snakemake process.
    """
    params = {
        "threads": threads,
        "memory": memory,
    }
    inputs = {
        "reads": reads,
    }
    if pacbio:
        inputs["pacbio"] = pacbio
    if nanopore:
        inputs["nanopore"] = nanopore

    return run_snake_wrapper(
        wrapper="file:tools/spades/metaspades",
        inputs=inputs,
        outputs={"output": output},
        params=params,
         
    )


@collect_tool()
def metaspades(
    *,
    reads: str,
    output: str,
    pacbio: Optional[str] = None,
    nanopore: Optional[str] = None,
    threads: Optional[int] = 1,
    memory: Optional[int] = 16,
     
) -> subprocess.CompletedProcess:
    """
    Assemble metagenome with metaspades. For more information, see the
    `Spades documentation <https://cab.spbu.ru/software/spades/>`.

    Metagenome assembly uses a lot of computational resources. Spades is told to
    restart from a previous checkpoint if the file `params.txt` exists in the output
    directory. In this way, one can use snakemake with `--restart-times` to automatically
    restart the assembly.

    Args:
        reads: Input reads for metaspades assembly (short reads, typically paired-end).
        output: Directory to store assembly results.
        pacbio (optional): Long-read PacBio input.
        nanopore (optional): Long-read Nanopore input.
        threads (optional): Number of threads available for assembly (default: 1).
        memory (optional): Amount of memory available for assembly in GB (default: 16).
  
    Returns:
        subprocess.CompletedProcess: Instance containing details about the completed Snakemake process.
    """
    return run_metaspades(
        reads=reads,
        output=output,
        pacbio=pacbio,
        nanopore=nanopore,
        threads=threads,
        memory=memory,
         
    )
