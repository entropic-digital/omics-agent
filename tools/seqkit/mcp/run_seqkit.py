from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_seqkit(
    *,
    input_files: str,
    output_files: str,
    command: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run SeqKit.

    Args:
        input_files: Input file(s) for SeqKit.
        output_files: Output file(s) for SeqKit.
        command: SeqKit command to use.
        extra (optional): Optional additional parameters for SeqKit.
  
    Notes:
        - First `input` and `output` file is considered to be the main one
          (except for commands `concat`, `common`, and `stats` that take all input files).
        - Keys for extra `input` and `output` files need to match `seqkit` arguments
          without the `-file` suffix (if present).

    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/seqkit",
        inputs={"input_files": input_files},
        outputs={"output_files": output_files},
        params={"command": command, "extra": extra} if extra else {"command": command},
         
    )


@collect_tool()
def seqkit(
    *,
    input_files: str,
    output_files: str,
    command: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run SeqKit.

    Args:
        input_files: Input file(s) for SeqKit.
        output_files: Output file(s) for SeqKit.
        command: SeqKit command to use.
        extra (optional): Optional additional parameters for SeqKit.
  
    Notes:
        - First `input` and `output` file is considered to be the main one
          (except for commands `concat`, `common`, and `stats` that take all input files).
        - Keys for extra `input` and `output` files need to match `seqkit` arguments
          without the `-file` suffix (if present).

    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_seqkit(
        input_files=input_files,
        output_files=output_files,
        command=command,
        extra=extra,
         
    )
