from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_enhancedvolcano(
    *,
    input_path: str,
    output_path: str,
    extra: Optional[str] = None,
    height: Optional[float] = 7.0,
    width: Optional[float] = 7.0,
     
) -> subprocess.CompletedProcess:
    """
    Build Volcano-plots with EnhancedVolcano.

    Args:
        input_path: Path to a TSV/CSV table (separator inferred from file extension)
                    or a RDS formatted object convertible into a `data.frame`.
        output_path: Path to SVG or PNG formatted Volcano plot.
        extra (optional): Additional parameters besides `toptable`.
        height (optional): Plot default height used in `grDevices::svg`. Default is 7.0.
        width (optional): Plot default width used in `grDevices::svg`. Default is 7.0.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/enhancedvolcano",
        inputs=dict(input_path=input_path),
        outputs=dict(output_path=output_path),
        params={
            "extra": extra,
            "height": height,
            "width": width,
        },
         
    )


@collect_tool()
def enhancedvolcano(
    *,
    input_path: str,
    output_path: str,
    extra: Optional[str] = None,
    height: Optional[float] = 7.0,
    width: Optional[float] = 7.0,
     
) -> subprocess.CompletedProcess:
    """
    Build Volcano-plots with EnhancedVolcano.

    Args:
        input_path: Path to a TSV/CSV table (separator inferred from file extension)
                    or a RDS formatted object convertible into a `data.frame`.
        output_path: Path to SVG or PNG formatted Volcano plot.
        extra (optional): Additional parameters besides `toptable`.
        height (optional): Plot default height used in `grDevices::svg`. Default is 7.0.
        width (optional): Plot default width used in `grDevices::svg`. Default is 7.0.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_enhancedvolcano(
        input_path=input_path,
        output_path=output_path,
        extra=extra,
        height=height,
        width=width,
         
    )
