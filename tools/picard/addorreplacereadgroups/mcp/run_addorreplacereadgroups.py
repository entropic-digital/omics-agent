from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_addorreplacereadgroups(
    *,
    input_bam: str,
    output_bam: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Add or replace read groups with picard tools.

    Args:
        input_bam: The input BAM file.
        output_bam: The output BAM file with added or replaced read groups.
        java_opts (optional): Additional arguments to pass to the Java compiler, e.g., "-XX:ParallelGCThreads=10".
                              Note: `-XmX` or `-Djava.io.tmpdir` are handled automatically.
        extra (optional): Additional program arguments for the Picard tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/picard/addorreplacereadgroups",
        inputs={"bam": input_bam},
        outputs={"bam": output_bam},
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def addorreplacereadgroups(
    *,
    input_bam: str,
    output_bam: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Add or replace read groups with picard tools.

    Args:
        input_bam: The input BAM file.
        output_bam: The output BAM file with added or replaced read groups.
        java_opts (optional): Additional arguments to pass to the Java compiler, e.g., "-XX:ParallelGCThreads=10".
                              Note: `-XmX` or `-Djava.io.tmpdir` are handled automatically.
        extra (optional): Additional program arguments for the Picard tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_addorreplacereadgroups(
        input_bam=input_bam,
        output_bam=output_bam,
        java_opts=java_opts,
        extra=extra,
         
    )
