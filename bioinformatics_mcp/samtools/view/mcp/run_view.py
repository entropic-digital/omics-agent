from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_view(
    *,
    input_file: str,
    output_file: str,
    region: Optional[str] = None,
    extra: Optional[str] = None,
    write_index: bool = False,
     
) -> subprocess.CompletedProcess:
    """
    Convert or filter SAM/BAM/CRAM files using samtools view.

    Args:
        input_file: Input SAM/BAM/CRAM file.
        output_file: Output SAM/BAM/CRAM file.
        region (optional): The region to extract (e.g., 'chr1', 'chr2:1000-2000', '*').
        extra (optional): Additional program arguments (not including `-@/--threads`,
                          `--write-index`, `-o`, or `-O/--output-fmt`).
        write_index: Whether to write an index for the output file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/samtools/view",
        inputs=dict(input_file=input_file),
        outputs=dict(output_file=output_file),
        params={
            "region": region,
            "extra": extra,
            "write_index": write_index,
        },
         
    )


@collect_tool()
def view(
    *,
    input_file: str,
    output_file: str,
    region: Optional[str] = None,
    extra: Optional[str] = None,
    write_index: bool = False,
     
) -> subprocess.CompletedProcess:
    """
    Convert or filter SAM/BAM/CRAM files using samtools view.

    Args:
        input_file: Input SAM/BAM/CRAM file.
        output_file: Output SAM/BAM/CRAM file.
        region (optional): The region to extract (e.g., 'chr1', 'chr2:1000-2000', '*').
        extra (optional): Additional program arguments (not including `-@/--threads`,
                          `--write-index`, `-o`, or `-O/--output-fmt`).
        write_index: Whether to write an index for the output file.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_view(
        input_file=input_file,
        output_file=output_file,
        region=region,
        extra=extra,
        write_index=write_index,
         
    )
