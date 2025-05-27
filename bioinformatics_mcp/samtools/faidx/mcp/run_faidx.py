from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_faidx(
    *,
    reference_sequence_file: str,
    regions: str,
    fai: Optional[str] = None,
    gzi: Optional[str] = None,
    region: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index reference sequence in FASTA format from a reference sequence.

    Args:
        reference_sequence_file: Path to the input reference sequence file (.fa).
        regions: Path to the file containing regions.
        fai (optional): Path to the index file for the reference sequence.
        gzi (optional): Path to the index for the BGZip'ed reference file.
        region (optional): Specific region to extract from the input file.
        extra (optional): Additional program arguments (excluding `-o`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/samtools/faidx",
        inputs={
            "reference_sequence_file": reference_sequence_file,
            "regions": regions,
            "fai": fai,
            "gzi": gzi,
        },
        params={
            "region": region,
            "extra": extra,
        },
         
    )


@collect_tool()
def faidx(
    *,
    reference_sequence_file: str,
    regions: str,
    fai: Optional[str] = None,
    gzi: Optional[str] = None,
    region: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Index reference sequence in FASTA format from a reference sequence.

    Args:
        reference_sequence_file: Path to the input reference sequence file (.fa).
        regions: Path to the file containing regions.
        fai (optional): Path to the index file for the reference sequence.
        gzi (optional): Path to the index for the BGZip'ed reference file.
        region (optional): Specific region to extract from the input file.
        extra (optional): Additional program arguments (excluding `-o`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_faidx(
        reference_sequence_file=reference_sequence_file,
        regions=regions,
        fai=fai,
        gzi=gzi,
        region=region,
        extra=extra,
         
    )
