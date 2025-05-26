from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    reference_genome: str,
    output_bed: str,
    threads: Optional[int] = 1,
     
) -> subprocess.CompletedProcess:
    """
    STRling index tool.

    STRling (pronounced like “sterling”) is a method to detect large short tandem repeat (STR) expansions
    from short-read sequencing data. The `index` command creates a BED file of large STR regions
    in the reference genome. This step is more efficient to run once for multiple samples and
    provide the file to the extract step with the `-g` option.

    Args:
        reference_genome: Path to the reference genome file.
        output_bed: Output BED file containing large STR regions.
        threads (optional): Number of threads to use. Default is 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/strling/index",
        inputs=dict(reference_genome=reference_genome),
        outputs=dict(output_bed=output_bed),
        params={"threads": threads},
         
    )


@collect_tool()
def index(
    *,
    reference_genome: str,
    output_bed: str,
    threads: Optional[int] = 1,
     
) -> subprocess.CompletedProcess:
    """
    STRling index tool.

    STRling (pronounced like “sterling”) is a method to detect large short tandem repeat (STR) expansions
    from short-read sequencing data. The `index` command creates a BED file of large STR regions
    in the reference genome. This step is more efficient to run once for multiple samples and
    provide the file to the extract step with the `-g` option.

    Args:
        reference_genome: Path to the reference genome file.
        output_bed: Output BED file containing large STR regions.
        threads (optional): Number of threads to use. Default is 1.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        reference_genome=reference_genome,
        output_bed=output_bed,
        threads=threads,
         
    )
