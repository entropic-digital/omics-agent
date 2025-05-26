from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_pe(
    *,
    input_1: str,
    input_2: str,
    output_1: str,
    output_2: str,
    output_single: str,
    qual_type: str,
    min_len: Optional[int] = None,
    qual_thresh: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim paired-end reads with sickle.

    Args:
        input_1: Path to the first paired-end input file.
        input_2: Path to the second paired-end input file.
        output_1: Path to the first output file for trimmed reads.
        output_2: Path to the second output file for trimmed reads.
        output_single: Path to the output file for single reads.
        qual_type: Quality type (e.g., illumina, sanger, or solexa).
        min_len (optional): Minimum read length after trimming.
        qual_thresh (optional): Quality threshold for trimming.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {"qual_type": qual_type}
    if min_len is not None:
        params["min_len"] = min_len
    if qual_thresh is not None:
        params["qual_thresh"] = qual_thresh

    return run_snake_wrapper(
        wrapper="file:tools/sickle/pe",
        inputs={"input_1": input_1, "input_2": input_2},
        outputs={
            "output_1": output_1,
            "output_2": output_2,
            "output_single": output_single,
        },
        params=params,
         
    )


@collect_tool()
def sickle_pe(
    *,
    input_1: str,
    input_2: str,
    output_1: str,
    output_2: str,
    output_single: str,
    qual_type: str,
    min_len: Optional[int] = None,
    qual_thresh: Optional[int] = None,
     
) -> subprocess.CompletedProcess:
    """
    Trim paired-end reads with sickle.

    Args:
        input_1: Path to the first paired-end input file.
        input_2: Path to the second paired-end input file.
        output_1: Path to the first output file for trimmed reads.
        output_2: Path to the second output file for trimmed reads.
        output_single: Path to the output file for single reads.
        qual_type: Quality type (e.g., illumina, sanger, or solexa).
        min_len (optional): Minimum read length after trimming.
        qual_thresh (optional): Quality threshold for trimming.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_pe(
        input_1=input_1,
        input_2=input_2,
        output_1=output_1,
        output_2=output_2,
        output_single=output_single,
        qual_type=qual_type,
        min_len=min_len,
        qual_thresh=qual_thresh,
         
    )
