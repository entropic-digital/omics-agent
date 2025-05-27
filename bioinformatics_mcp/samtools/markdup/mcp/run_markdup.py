from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_markdup(
    *,
    input_file: str,
    output_file: str,
    output_index_file: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Mark duplicate alignments in a coordinate sorted file.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path to the output SAM/BAM/CRAM file.
        output_index_file (optional): Path to SAM/BAM/CRAM index file.
        extra (optional): Additional program arguments (not `-@/--threads`,
                          `--write-index`, `-m`, `-T`, `-f`, `-o` or
                          `-O/--output-fmt`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/samtools/markdup",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file, "output_index_file": output_index_file}
        if output_index_file
        else {"output_file": output_file},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def markdup(
    *,
    input_file: str,
    output_file: str,
    output_index_file: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Mark duplicate alignments in a coordinate sorted file.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path to the output SAM/BAM/CRAM file.
        output_index_file (optional): Path to SAM/BAM/CRAM index file.
        extra (optional): Additional program arguments (not `-@/--threads`,
                          `--write-index`, `-m`, `-T`, `-f`, `-o` or
                          `-O/--output-fmt`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_markdup(
        input_file=input_file,
        output_file=output_file,
        output_index_file=output_index_file,
        extra=extra,
         
    )
