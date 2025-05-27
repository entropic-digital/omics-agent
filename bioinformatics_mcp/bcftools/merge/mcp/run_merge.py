from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_merge(
    *,
    input_files: List[str],
    output: str,
    output_type: str,
    regions: Optional[str] = None,
    region_file: Optional[str] = None,
    include_header: Optional[bool] = None,
    threads: Optional[int] = 1,
    output_uncompressed_bcf: Optional[bool] = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Merge VCF/BCF files using bcftools.

    Args:
        input_files: List of input VCF/BCF files to merge.
        output: Path to the output file.
        output_type: Output type: 'v' for VCF, 'b' for binary BCF, 'u' for uncompressed BCF.
        regions (optional): Comma-separated list of regions to merge (e.g., 'chr1,chr2').
        region_file (optional): File with regions to limit the merge operation.
        include_header (optional): Whether to output the header even before content.
        threads (optional): Number of threads to use (default 1).
        output_uncompressed_bcf (optional): If set, the BCF output will be uncompressed.
        extra (optional): Additional bcftools merge arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/bcftools/merge",
        inputs={"input_files": input_files},
        outputs={"output": output},
        params={
            "output_type": output_type,
            "regions": regions,
            "region_file": region_file,
            "include_header": include_header,
            "threads": threads,
            "output_uncompressed_bcf": output_uncompressed_bcf,
            "extra": extra,
        },
         
    )


@collect_tool()
def merge(
    *,
    input_files: List[str],
    output: str,
    output_type: str,
    regions: Optional[str] = None,
    region_file: Optional[str] = None,
    include_header: Optional[bool] = None,
    threads: Optional[int] = 1,
    output_uncompressed_bcf: Optional[bool] = False,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Merge VCF/BCF files using bcftools.

    Args:
        input_files: List of input VCF/BCF files to merge.
        output: Path to the output file.
        output_type: Output type: 'v' for VCF, 'b' for binary BCF, 'u' for uncompressed BCF.
        regions (optional): Comma-separated list of regions to merge (e.g., 'chr1,chr2').
        region_file (optional): File with regions to limit the merge operation.
        include_header (optional): Whether to output the header even before content.
        threads (optional): Number of threads to use (default 1).
        output_uncompressed_bcf (optional): If set, the BCF output will be uncompressed.
        extra (optional): Additional bcftools merge arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_merge(
        input_files=input_files,
        output=output,
        output_type=output_type,
        regions=regions,
        region_file=region_file,
        include_header=include_header,
        threads=threads,
        output_uncompressed_bcf=output_uncompressed_bcf,
        extra=extra,
         
    )
