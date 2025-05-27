from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_twoBitInfo(
    *,
    input_2bit: str,
    output_chrom_sizes: str,
     
) -> subprocess.CompletedProcess:
    """
    Generate *.chrom.sizes file from a *.2bit genome file.

    Args:
        input_2bit: Path to the input genome *.2bit file.
        output_chrom_sizes: Path to the output *.chrom.sizes file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/ucsc/twoBitInfo",
        inputs={"input_2bit": input_2bit},
        outputs={"output_chrom_sizes": output_chrom_sizes},
         
    )


@collect_tool()
def twoBitInfo(
    *,
    input_2bit: str,
    output_chrom_sizes: str,
     
) -> subprocess.CompletedProcess:
    """
    Generate *.chrom.sizes file from a *.2bit genome file.

    Args:
        input_2bit: Path to the input genome *.2bit file.
        output_chrom_sizes: Path to the output *.chrom.sizes file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_twoBitInfo(
        input_2bit=input_2bit,
        output_chrom_sizes=output_chrom_sizes,
         
    )
