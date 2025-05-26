from typing import List, Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_learn_errors(
    *,
    input_files: List[str],
    err: str,
    plot: str,
    optional_params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Learn error rates using DADA2's learnErrors function.

    Args:
        input_files: A list of quality filtered and trimmed forward FASTQ files (potentially compressed).
        err: Output RDS file with the stored error model.
        plot: Output plot file showing observed vs estimated errors rates.
        optional_params (optional): Additional arguments for the learnErrors function provided as key=value pairs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/dada2/learn-errors",
        inputs={"input_files": input_files},
        outputs={"err": err, "plot": plot},
        params=optional_params if optional_params else {},
         
    )


@collect_tool()
def learn_errors(
    *,
    input_files: List[str],
    err: str,
    plot: str,
    optional_params: Optional[dict] = None,
     
) -> subprocess.CompletedProcess:
    """
    Learn error rates using DADA2's learnErrors function.

    Args:
        input_files: A list of quality filtered and trimmed forward FASTQ files (potentially compressed).
        err: Output RDS file with the stored error model.
        plot: Output plot file showing observed vs estimated errors rates.
        optional_params (optional): Additional arguments for the learnErrors function provided as key=value pairs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_learn_errors(
        input_files=input_files,
        err=err,
        plot=plot,
        optional_params=optional_params,
         
    )
