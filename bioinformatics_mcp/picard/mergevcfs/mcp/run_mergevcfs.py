from typing import List, Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_mergevcfs(
    *,
    vcf_files: List[str],
    merged_vcf_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Merge VCF files using Picard MergeVcfs.

    Args:
        vcf_files: List of input VCF files to merge.
        merged_vcf_file: Path to the output merged VCF file.
        java_opts (optional): Additional arguments for the Java compiler, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments for MergeVcfs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/picard/mergevcfs",
        inputs={"vcf_files": vcf_files},
        outputs={"merged_vcf_file": merged_vcf_file},
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def mergevcfs(
    *,
    vcf_files: List[str],
    merged_vcf_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Merge VCF files using Picard MergeVcfs.

    Args:
        vcf_files: List of input VCF files to merge.
        merged_vcf_file: Path to the output merged VCF file.
        java_opts (optional): Additional arguments for the Java compiler, e.g., "-XX:ParallelGCThreads=10".
        extra (optional): Additional program arguments for MergeVcfs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_mergevcfs(
        vcf_files=vcf_files,
        merged_vcf_file=merged_vcf_file,
        java_opts=java_opts,
        extra=extra,
         
    )
