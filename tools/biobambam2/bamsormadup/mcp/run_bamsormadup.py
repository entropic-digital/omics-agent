from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bamsormadup(
    *,
    input_file: str,
    reference: Optional[str] = None,
    output_file: str,
    index: Optional[str] = None,
    metrics: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Mark PCR and optical duplicates, followed by sorting, with BioBamBam2 tools.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file. This must be the first file.
        reference (optional): Path to the reference file (required for CRAM output).
        output_file: Path to the output SAM/BAM/CRAM file with marked duplicates.
        index (optional): Path to the BAM index file.
        metrics (optional): Path to the metrics file.
        extra (optional): Additional program arguments (excluding `inputformat`, `outputformat`, or `tmpfile`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/biobambam2/bamsormadup",
        inputs={"input_file": input_file, "reference": reference},
        outputs={"output_file": output_file, "index": index, "metrics": metrics},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def bamsormadup(
    *,
    input_file: str,
    reference: Optional[str] = None,
    output_file: str,
    index: Optional[str] = None,
    metrics: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Mark PCR and optical duplicates, followed by sorting, with BioBamBam2 tools.

    Args:
        input_file: Path to the input SAM/BAM/CRAM file. This must be the first file.
        reference (optional): Path to the reference file (required for CRAM output).
        output_file: Path to the output SAM/BAM/CRAM file with marked duplicates.
        index (optional): Path to the BAM index file.
        metrics (optional): Path to the metrics file.
        extra (optional): Additional program arguments (excluding `inputformat`, `outputformat`, or `tmpfile`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bamsormadup(
        input_file=input_file,
        reference=reference,
        output_file=output_file,
        index=index,
        metrics=metrics,
        extra=extra,
         
    )
