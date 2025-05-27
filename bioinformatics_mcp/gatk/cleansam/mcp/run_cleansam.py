from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_cleansam(
    *,
    input_file: str,
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk CleanSam.

    Args:
        input_file: SAM/BAM/CRAM file to be cleaned.
        output_file: Cleaned and validated SAM/BAM/CRAM file.
        java_opts (optional): Additional arguments passed to the Java compiler, e.g. "-XX:ParallelGCThreads=10". Note: `-XmX` or `-Djava.io.tmpdir` are handled automatically.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/cleansam",
        inputs={"input": input_file},
        outputs={"output": output_file},
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def cleansam(
    *,
    input_file: str,
    output_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk CleanSam.

    Args:
        input_file: SAM/BAM/CRAM file to be cleaned.
        output_file: Cleaned and validated SAM/BAM/CRAM file.
        java_opts (optional): Additional arguments passed to the Java compiler, e.g. "-XX:ParallelGCThreads=10". Note: `-XmX` or `-Djava.io.tmpdir` are handled automatically.
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_cleansam(
        input_file=input_file,
        output_file=output_file,
        java_opts=java_opts,
        extra=extra,
         
    )
