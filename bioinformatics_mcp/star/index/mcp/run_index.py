from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_index(
    *,
    fasta_file: str,
    output_dir: str,
    sjdbOverhang: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index fasta sequences with STAR.

    Args:
        fasta_file: Path to the input (multi)fasta formatted file.
        output_dir: Path to the output directory for the indexed sequence.
        sjdbOverhang (optional): Length of the donor/acceptor sequence on each side of the junctions.
        extra (optional): Additional program arguments for STAR.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {}
    if sjdbOverhang is not None:
        params["sjdbOverhang"] = sjdbOverhang
    if extra is not None:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/star/index",
        inputs=dict(fasta_file=fasta_file),
        outputs=dict(output_dir=output_dir),
        params=params,
         
    )


@collect_tool()
def star_index(
    *,
    fasta_file: str,
    output_dir: str,
    sjdbOverhang: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index fasta sequences with STAR.

    Args:
        fasta_file: Path to the input (multi)fasta formatted file.
        output_dir: Path to the output directory for the indexed sequence.
        sjdbOverhang (optional): Length of the donor/acceptor sequence on each side of the junctions.
        extra (optional): Additional program arguments for STAR.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_index(
        fasta_file=fasta_file,
        output_dir=output_dir,
        sjdbOverhang=sjdbOverhang,
        extra=extra,
         
    )
