from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_combinegvcfs(
    *,
    gvcf_files: List[str],
    combined_gvcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk CombineGVCFs.

    Args:
        gvcf_files: List of GVCF file paths for multiple samples.
        combined_gvcf: Path to the output combined GVCF file.
        java_opts (optional): Additional arguments to pass to the Java compiler
            (excluding -XmX and -Djava.io.tmpdir, handled automatically).
        extra (optional): Additional program arguments for CombineGVCFs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/combinegvcfs",
        inputs={"gvcf_files": gvcf_files},
        outputs={"combined_gvcf": combined_gvcf},
        params={k: v for k, v in {"java_opts": java_opts, "extra": extra}.items() if v},
         
    )


@collect_tool()
def combine_gvcfs(
    *,
    gvcf_files: List[str],
    combined_gvcf: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk CombineGVCFs.

    Args:
        gvcf_files: List of GVCF file paths for multiple samples.
        combined_gvcf: Path to the output combined GVCF file.
        java_opts (optional): Additional arguments to pass to the Java compiler
            (excluding -XmX and -Djava.io.tmpdir, handled automatically).
        extra (optional): Additional program arguments for CombineGVCFs.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_combinegvcfs(
        gvcf_files=gvcf_files,
        combined_gvcf=combined_gvcf,
        java_opts=java_opts,
        extra=extra,
         
    )
