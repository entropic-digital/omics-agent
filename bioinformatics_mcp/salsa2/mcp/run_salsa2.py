from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_salsa2(
    *,
    bed_file: str,
    fasta_file: str,
    fasta_index_file: str,
    polished_assembly_fasta: str,
    polished_assembly_agp: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    A tool to scaffold long read assemblies with Hi-C data.

    Args:
        bed_file: Path to the BED file.
        fasta_file: Path to the FASTA file.
        fasta_index_file: Path to the FASTA index file.
        polished_assembly_fasta: Path to the output polished assembly in FASTA format.
        polished_assembly_agp: Path to the output polished assembly in AGP format.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/salsa2",
        inputs=dict(
            bed_file=bed_file,
            fasta_file=fasta_file,
            fasta_index_file=fasta_index_file,
        ),
        outputs=dict(
            polished_assembly_fasta=polished_assembly_fasta,
            polished_assembly_agp=polished_assembly_agp,
        ),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def salsa2(
    *,
    bed_file: str,
    fasta_file: str,
    fasta_index_file: str,
    polished_assembly_fasta: str,
    polished_assembly_agp: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    A tool to scaffold long read assemblies with Hi-C data.

    Args:
        bed_file: Path to the BED file.
        fasta_file: Path to the FASTA file.
        fasta_index_file: Path to the FASTA index file.
        polished_assembly_fasta: Path to the output polished assembly in FASTA format.
        polished_assembly_agp: Path to the output polished assembly in AGP format.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_salsa2(
        bed_file=bed_file,
        fasta_file=fasta_file,
        fasta_index_file=fasta_index_file,
        polished_assembly_fasta=polished_assembly_fasta,
        polished_assembly_agp=polished_assembly_agp,
        extra=extra,
         
    )
