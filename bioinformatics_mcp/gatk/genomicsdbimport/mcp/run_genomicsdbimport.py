from typing import Optional, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_genomicsdbimport(
    *,
    gvcf_files: List[str],
    workspace: str,
    intervals: str,
    java_opts: Optional[str] = None,
    db_action: str = "create",
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk GenomicsDBImport.

    Args:
        gvcf_files: List of GVCF file paths for multiple samples.
        workspace: Path to the GenomicsDB workspace directory.
        intervals: Mandatory parameter specifying genomic intervals.
        java_opts (optional): Additional Java options (e.g., -XX:ParallelGCThreads=10).
                              Excludes -XmX or -Djava.io.tmpdir.
        db_action: Action for the database, either 'create' (default) or 'update'.
        extra (optional): Additional program arguments to be passed.
            
    Returns:
        subprocess.CompletedProcess: Information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/genomicsdbimport",
        inputs={"gvcf_files": gvcf_files},
        outputs={"workspace": workspace},
        params={
            "intervals": intervals,
            "java_opts": java_opts,
            "db_action": db_action,
            "extra": extra,
        },
         
    )


@collect_tool()
def genomicsdbimport(
    *,
    gvcf_files: List[str],
    workspace: str,
    intervals: str,
    java_opts: Optional[str] = None,
    db_action: str = "create",
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk GenomicsDBImport.

    Args:
        gvcf_files: List of GVCF file paths for multiple samples.
        workspace: Path to the GenomicsDB workspace directory.
        intervals: Mandatory parameter specifying genomic intervals.
        java_opts (optional): Additional Java options (e.g., -XX:ParallelGCThreads=10).
                              Excludes -XmX or -Djava.io.tmpdir.
        db_action: Action for the database, either 'create' (default) or 'update'.
        extra (optional): Additional program arguments to be passed.
            
    Returns:
        subprocess.CompletedProcess: Information about the completed Snakemake process.
    """
    return run_genomicsdbimport(
        gvcf_files=gvcf_files,
        workspace=workspace,
        intervals=intervals,
        java_opts=java_opts,
        db_action=db_action,
        extra=extra,
         
    )
