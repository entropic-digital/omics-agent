from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_razers3(
    *,
    reads: str,
    reference: str,
    output: str,
    aligner: Optional[str] = None,
    format: Optional[str] = None,
    indels: Optional[int] = None,
    percent_identity: Optional[float] = None,
    error_rate: Optional[float] = None,
     
) -> subprocess.CompletedProcess:
    """
    Mapping (short) reads against a reference sequence. Can have multiple output formats.

    Args:
        reads: Input file containing the reads.
        reference: Reference sequence for mapping.
        output: Path to the output file.
        aligner (optional): Specifies the aligner to use.
        format (optional): Output format of the mapping.
        indels (optional): Maximum number of indels allowed.
        percent_identity (optional): Minimum percent identity required.
        error_rate (optional): Error rate for mapping.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/razers3",
        inputs={"reads": reads, "reference": reference},
        outputs={"output": output},
        params={
            "aligner": aligner,
            "format": format,
            "indels": indels,
            "percent_identity": percent_identity,
            "error_rate": error_rate,
        },
         
    )


@collect_tool()
def razers3(
    *,
    reads: str,
    reference: str,
    output: str,
    aligner: Optional[str] = None,
    format: Optional[str] = None,
    indels: Optional[int] = None,
    percent_identity: Optional[float] = None,
    error_rate: Optional[float] = None,
     
) -> subprocess.CompletedProcess:
    """
    Mapping (short) reads against a reference sequence. Can have multiple output formats.

    Args:
        reads: Input file containing the reads.
        reference: Reference sequence for mapping.
        output: Path to the output file.
        aligner (optional): Specifies the aligner to use.
        format (optional): Output format of the mapping.
        indels (optional): Maximum number of indels allowed.
        percent_identity (optional): Minimum percent identity required.
        error_rate (optional): Error rate for mapping.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_razers3(
        reads=reads,
        reference=reference,
        output=output,
        aligner=aligner,
        format=format,
        indels=indels,
        percent_identity=percent_identity,
        error_rate=error_rate,
         
    )
