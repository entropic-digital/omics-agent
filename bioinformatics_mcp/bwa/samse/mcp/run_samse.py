from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_samse(
    *,
    input_alignment_file: str,
    input_reads_file: str,
    reference_sequence_file: str,
    output_file: str,
    read_group_header_line: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map single-end reads with bwa samse. For more information, see BWA documentation.

    Args:
        input_alignment_file: Path to the input alignment file.
        input_reads_file: Path to the single-end read file.
        reference_sequence_file: Path to the indexed reference sequence file.
        output_file: Path to the output file.
        read_group_header_line (optional): Read group header line for BWA, if any.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bwa/samse",
        inputs=dict(
            input_alignment_file=input_alignment_file,
            input_reads_file=input_reads_file,
            reference_sequence_file=reference_sequence_file,
        ),
        outputs=dict(output_file=output_file),
        params={"read_group_header_line": read_group_header_line}
        if read_group_header_line
        else {},
         
    )


@collect_tool()
def samse(
    *,
    input_alignment_file: str,
    input_reads_file: str,
    reference_sequence_file: str,
    output_file: str,
    read_group_header_line: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map single-end reads with bwa samse. For more information, see BWA documentation.

    Args:
        input_alignment_file: Path to the input alignment file.
        input_reads_file: Path to the single-end read file.
        reference_sequence_file: Path to the indexed reference sequence file.
        output_file: Path to the output file.
        read_group_header_line (optional): Read group header line for BWA, if any.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_samse(
        input_alignment_file=input_alignment_file,
        input_reads_file=input_reads_file,
        reference_sequence_file=reference_sequence_file,
        output_file=output_file,
        read_group_header_line=read_group_header_line,
         
    )
