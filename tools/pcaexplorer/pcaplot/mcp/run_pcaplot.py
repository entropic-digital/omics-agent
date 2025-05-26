from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_pcaplot(
    *,
    input_path: str,
    output_path: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Plots the results of PCA on a 2-dimensional space.

    Args:
        input_path: Path to DESeqTransform object, such as rlog or vst transformed data.
        output_path: Path to PCA plot (SVG formatted).
        extra (optional): Optional parameters, besides `x`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/pcaexplorer/pcaplot",
        inputs=dict(input=input_path),
        outputs=dict(output=output_path),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def pcaplot(
    *,
    input_path: str,
    output_path: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Plots the results of PCA on a 2-dimensional space.

    Args:
        input_path: Path to DESeqTransform object, such as rlog or vst transformed data.
        output_path: Path to PCA plot (SVG formatted).
        extra (optional): Optional parameters, besides `x`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_pcaplot(
        input_path=input_path,
        output_path=output_path,
        extra=extra,
         
    )
