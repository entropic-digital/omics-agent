from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_sortsam(
    *,
    input_file: str,
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Sort SAM/BAM files using Picard's SortSam tool.

    Args:
        input_file: Path to the input SAM/BAM file.
        output_file: Path to the output sorted SAM/BAM file.
        java_opts (optional): Additional arguments for the Java compiler,
                              e.g. "-XX:ParallelGCThreads=10". Do not include
                              `-Xmx` or `-Djava.io.tmpdir`, as they are handled automatically.
        extra (optional): Additional program arguments for the SortSam tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/picard/sortsam",
        inputs={"input_file": input_file},
        outputs={"output_file": output_file},
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def sortsam(
    *,
    input_file: str,
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Sort SAM/BAM files using Picard's SortSam tool.

    Args:
        input_file: Path to the input SAM/BAM file.
        output_file: Path to the output sorted SAM/BAM file.
        java_opts (optional): Additional arguments for the Java compiler,
                              e.g. "-XX:ParallelGCThreads=10". Do not include
                              `-Xmx` or `-Djava.io.tmpdir`, as they are handled automatically.
        extra (optional): Additional program arguments for the SortSam tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_sortsam(
        input_file=input_file,
        output_file=output_file,
        java_opts=java_opts,
        extra=extra,
         
    )
