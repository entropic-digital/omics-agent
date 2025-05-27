from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_giraffe(
    *,
    fastq_files: List[str],
    reference_graph: str,
    output_file: str,
    extra: Optional[str] = None,
    sort_order: Optional[str] = None,
    sorting: str = "none",
    sort_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads using vg giraffe, with optional sorting using samtools or picard.

    Args:
        fastq_files (list of str): List of FASTQ file(s) to map.
        reference_graph (str): The reference graph file for alignment.
        output_file (str): The output BAM/SAM or CRAM file.
        extra (optional, str): Additional arguments for vg giraffe.
        sort_order (optional, str): Sorting order, either 'queryname' or 'coordinate'.
        sorting (optional, str): Sorting tool ('none', 'samtools', 'fgbio', or 'picard'). Default is 'none'.
        sort_extra (optional, str): Extra arguments for the sorting tool.
  
    Returns:
        subprocess.CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    inputs = {
        "fastq": fastq_files,
        "reference_graph": reference_graph,
    }
    outputs = {"output": output_file}
    params = {
        "extra": extra,
        "sorting": sorting,
        "sort_order": sort_order,
        "sort_extra": sort_extra,
    }

    # Filter out None values for optional parameters
    params = {k: v for k, v in params.items() if v is not None}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/vg/giraffe",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def giraffe(
    *,
    fastq_files: List[str],
    reference_graph: str,
    output_file: str,
    extra: Optional[str] = None,
    sort_order: Optional[str] = None,
    sorting: str = "none",
    sort_extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Map reads using vg giraffe, with optional sorting using samtools or picard.

    Args:
        fastq_files (list of str): List of FASTQ file(s) to map.
        reference_graph (str): The reference graph file for alignment.
        output_file (str): The output BAM/SAM or CRAM file.
        extra (optional, str): Additional arguments for vg giraffe.
        sort_order (optional, str): Sorting order, either 'queryname' or 'coordinate'.
        sorting (optional, str): Sorting tool ('none', 'samtools', 'fgbio', or 'picard'). Default is 'none'.
        sort_extra (optional, str): Extra arguments for the sorting tool.
  
    Returns:
        subprocess.CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_giraffe(
        fastq_files=fastq_files,
        reference_graph=reference_graph,
        output_file=output_file,
        extra=extra,
        sort_order=sort_order,
        sorting=sorting,
        sort_extra=sort_extra,
         
    )
