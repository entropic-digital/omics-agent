from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_compute(
    *,
    input_file: str,
    output_signature: str,
    ksize: Optional[int] = None,
    scaled: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Build a MinHash signature for a transcriptome, genome, or reads.

    Args:
        input_file: Path to the assembly fasta or reads fastq file.
        output_signature: Path where the sourmash signature will be stored.
        ksize (optional): K-mer size to use (default is 31).
        scaled (optional): Scaling factor to control signature size (default is 2000).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {}
    if ksize is not None:
        params["ksize"] = ksize
    if scaled is not None:
        params["scaled"] = scaled

    return run_snake_wrapper(
        wrapper="file:tools/sourmash/compute",
        inputs={"input_file": input_file},
        outputs={"output_signature": output_signature},
        params=params,
         
    )


@collect_tool()
def sourmash_compute(
    *,
    input_file: str,
    output_signature: str,
    ksize: Optional[int] = None,
    scaled: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Build a MinHash signature for a transcriptome, genome, or reads.

    Args:
        input_file: Path to the assembly fasta or reads fastq file.
        output_signature: Path where the sourmash signature will be stored.
        ksize (optional): K-mer size to use (default is 31).
        scaled (optional): Scaling factor to control signature size (default is 2000).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_compute(
        input_file=input_file,
        output_signature=output_signature,
        ksize=ksize,
        scaled=scaled,
         
    )
