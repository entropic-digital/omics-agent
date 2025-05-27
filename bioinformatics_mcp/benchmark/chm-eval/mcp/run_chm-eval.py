from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_chm_eval(
    *,
    kit: str,
    vcf: str,
    summary: str,
    bed: str,
    build: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Evaluate a given VCF file with chm-eval for benchmarking variant calling.

    Args:
        kit: Path to annotation directory.
        vcf: Path to VCF to evaluate (can be gzipped).
        summary: Path to write statistics and evaluations.
        bed: Path to write list of errors (BED formatted).
        build: Genome build. Either '37' or '38'.
        extra: Optional parameters besides `-g`.
  
    Returns:
        CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/benchmark/chm-eval",
        inputs={"kit": kit, "vcf": vcf},
        outputs={"summary": summary, "bed": bed},
        params={"build": build, "extra": extra} if extra else {"build": build},
         
    )


@collect_tool()
def chm_eval(
    *,
    kit: str,
    vcf: str,
    summary: str,
    bed: str,
    build: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Evaluate a given VCF file with chm-eval for benchmarking variant calling.

    Args:
        kit: Path to annotation directory.
        vcf: Path to VCF to evaluate (can be gzipped).
        summary: Path to write statistics and evaluations.
        bed: Path to write list of errors (BED formatted).
        build: Genome build. Either '37' or '38'.
        extra: Optional parameters besides `-g`.
  
    Returns:
        CompletedProcess: Instance containing information about the completed Snakemake process.
    """
    return run_chm_eval(
        kit=kit,
        vcf=vcf,
        summary=summary,
        bed=bed,
        build=build,
        extra=extra,
         
    )
