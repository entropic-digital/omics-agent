from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_learnreadorientationmodel(
    *,
    f1r2: List[str],
    output: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GATK LearnReadOrientationModel.

    Get the maximum likelihood estimates of artifact prior probabilities
    in the orientation bias mixture model filter.

    Args:
        f1r2: Path(s) to one or more f1r2 files.
        output: Path to the tar.gz file of artifact prior tables.
        java_opts (optional): Additional arguments to pass to the Java compiler,
            except for `-XmX` or `-Djava.io.tmpdir`, as they are handled automatically.
        extra (optional): Additional custom program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/learnreadorientationmodel",
        inputs={"f1r2": f1r2},
        outputs={"output": output},
        params={
            "java_opts": java_opts,
            "extra": extra,
        },
         
    )


@collect_tool()
def learnreadorientationmodel(
    *,
    f1r2: List[str],
    output: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    GATK LearnReadOrientationModel.

    Get the maximum likelihood estimates of artifact prior probabilities
    in the orientation bias mixture model filter.

    Args:
        f1r2: Path(s) to one or more f1r2 files.
        output: Path to the tar.gz file of artifact prior tables.
        java_opts (optional): Additional arguments to pass to the Java compiler,
            except for `-XmX` or `-Djava.io.tmpdir`, as they are handled automatically.
        extra (optional): Additional custom program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_learnreadorientationmodel(
        f1r2=f1r2,
        output=output,
        java_opts=java_opts,
        extra=extra,
         
    )
