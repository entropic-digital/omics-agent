from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_sort(
    *,
    in_file: str,
    output: str,
    genome: Optional[str] = None,
    faidx: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Sorts BED, VCF, or GFF files by chromosome and other criteria using the sortBed tool.

    Args:
        in_file: Path to interval file (BED/GFF/VCF formatted).
        output: Path to the sorted interval file (BED/GFF/VCF formatted).
        genome (optional): A tab-separated file determining sorting order with chromosome names in the first column.
        faidx (optional): A FASTA index file.
        extra (optional): Additional program arguments (excluding `-i`, `-g`, or `--faidx`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {"extra": extra} if extra else {}
    return run_snake_wrapper(
        wrapper="file:tools/bedtools/sort",
        inputs=dict(in_file=in_file),
        outputs=dict(output=output),
        params=params,
        resources={"genome": genome, "faidx": faidx},
         
    )


@collect_tool()
def sortBed(
    *,
    in_file: str,
    output: str,
    genome: Optional[str] = None,
    faidx: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Sorts BED, VCF, or GFF files by chromosome and other criteria using the sortBed tool.

    Args:
        in_file: Path to interval file (BED/GFF/VCF formatted).
        output: Path to the sorted interval file (BED/GFF/VCF formatted).
        genome (optional): A tab-separated file determining sorting order with chromosome names in the first column.
        faidx (optional): A FASTA index file.
        extra (optional): Additional program arguments (excluding `-i`, `-g`, or `--faidx`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_sort(
        in_file=in_file,
        output=output,
        genome=genome,
        faidx=faidx,
        extra=extra,
         
    )
