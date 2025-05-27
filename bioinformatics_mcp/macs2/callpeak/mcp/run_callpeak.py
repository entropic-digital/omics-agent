from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_callpeak(
    *,
    input_file: str,
    output_file: str,
    broad: Optional[bool] = False,
    bdg: Optional[bool] = False,
    format: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    MACS2 callpeak tool for peak calling in ChIP-sequencing data.

    Args:
        input_file: Input alignment file (e.g., SAM, BAM, BED, etc.).
        output_file: Base name for all output files.
        broad (optional): Whether to process using broad peak calling mode.
        bdg (optional): Whether to output bedGraph files for pileup/control lambda.
        format (optional): Input file format (e.g., BAM, BED, ELAND, etc.).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {
        "broad": broad,
        "bdg": bdg,
        "format": format,
    }
    # Remove unset parameters (None values) from the params dictionary
    params = {k: v for k, v in params.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/macs2/callpeak",
        inputs=dict(input_file=input_file),
        outputs=dict(output_file=output_file),
        params=params,
         
    )


@collect_tool()
def callpeak(
    *,
    input_file: str,
    output_file: str,
    broad: Optional[bool] = False,
    bdg: Optional[bool] = False,
    format: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    MACS2 callpeak tool for peak calling in ChIP-sequencing data.

    Args:
        input_file: Input alignment file (e.g., SAM, BAM, BED, etc.).
        output_file: Base name for all output files.
        broad (optional): Whether to process using broad peak calling mode.
        bdg (optional): Whether to output bedGraph files for pileup/control lambda.
        format (optional): Input file format (e.g., BAM, BED, ELAND, etc.).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_callpeak(
        input_file=input_file,
        output_file=output_file,
        broad=broad,
        bdg=bdg,
        format=format,
         
    )
