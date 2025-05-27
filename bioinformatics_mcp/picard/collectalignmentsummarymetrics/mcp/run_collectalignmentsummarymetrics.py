from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_collectalignmentsummarymetrics(
    *,
    input: str,
    output: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collect metrics on aligned reads with Picard tools.

    Args:
        input: Path to the input BAM file.
        output: Path to the output metrics file.
        java_opts (optional): Additional arguments for the Java VM, excluding -XmX and -Djava.io.tmpdir.
        extra (optional): Additional Picard arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/picard/collectalignmentsummarymetrics",
        inputs={"input": input},
        outputs={"output": output},
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def collectalignmentsummarymetrics(
    *,
    input: str,
    output: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Collect metrics on aligned reads with Picard tools.

    Args:
        input: Path to the input BAM file.
        output: Path to the output metrics file.
        java_opts (optional): Additional arguments for the Java VM, excluding -XmX and -Djava.io.tmpdir.
        extra (optional): Additional Picard arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_collectalignmentsummarymetrics(
        input=input, output=output, java_opts=java_opts, extra=extra,      
    )
