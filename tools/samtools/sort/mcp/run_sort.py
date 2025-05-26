from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_sort(
    *,
    input_file: str,
    output_file: str,
    index_file: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Sort a BAM file using samtools.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path to the output sorted SAM/BAM/CRAM file.
        index_file (optional): Path to the optional output index file.
        extra (optional): Additional program arguments (excluding `-@/--threads`, `--write-index`, `-m`, `-o`, or `-O/--output-fmt`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {"extra": extra} if extra else {}
    return run_snake_wrapper(
        wrapper="file:tools/samtools/sort",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file, "index_file": index_file}
        if index_file
        else {"output_file": output_file},
        params=params,
         
    )


@collect_tool()
def samtools_sort(
    *,
    input_file: str,
    output_file: str,
    index_file: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Sort a BAM file using samtools.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path to the output sorted SAM/BAM/CRAM file.
        index_file (optional): Path to the optional output index file.
        extra (optional): Additional program arguments (excluding `-@/--threads`, `--write-index`, `-m`, `-o`, or `-O/--output-fmt`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_sort(
        input_file=input_file,
        output_file=output_file,
        index_file=index_file,
        extra=extra,
         
    )
