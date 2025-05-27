from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_map(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Paired REad TEXTure Mapper. Converts SAM formatted read pairs into genome contact maps.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path to the output pretext contact map file.
        extra (optional): Additional arguments for the Pretext Map tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/pretext/map",
        inputs=dict(input=input_file),
        outputs=dict(output=output_file),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def map(
    *,
    input_file: str,
    output_file: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Paired REad TEXTure Mapper. Converts SAM formatted read pairs into genome contact maps.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file.
        output_file: Path to the output pretext contact map file.
        extra (optional): Additional arguments for the Pretext Map tool.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_map(
        input_file=input_file, output_file=output_file, extra=extra,      
    )
