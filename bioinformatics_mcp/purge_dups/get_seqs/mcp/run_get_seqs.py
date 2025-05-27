from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_get_seqs(
    *,
    bed_file: str,
    fasta_file: str,
    output_fasta_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Purge haplotigs and overlaps in an assembly based on read depth.

    Args:
        bed_file: Input BED file.
        fasta_file: Input FASTA file.
        output_fasta_file: Output purged FASTA file.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/purge_dups/get_seqs",
        inputs=dict(bed_file=bed_file, fasta_file=fasta_file),
        outputs=dict(output_fasta_file=output_fasta_file),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def get_seqs(
    *,
    bed_file: str,
    fasta_file: str,
    output_fasta_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Purge haplotigs and overlaps in an assembly based on read depth.

    Args:
        bed_file: Input BED file.
        fasta_file: Input FASTA file.
        output_fasta_file: Output purged FASTA file.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_get_seqs(
        bed_file=bed_file,
        fasta_file=fasta_file,
        output_fasta_file=output_fasta_file,
        extra=extra,
         
    )
