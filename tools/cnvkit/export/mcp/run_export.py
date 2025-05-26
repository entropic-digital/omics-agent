from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_export(
    *,
    cns: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert copy number ratio tables (.cnr files) or segments (.cns) to another format.

    Args:
        cns: Path to the cns or cnr file(s).
        output: Desired output file format (bed/vcf/vcf.gz/cdt/seq).
        extra (optional): Additional parameters that will be forwarded to cnvkit export.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/cnvkit/export",
        inputs=dict(cns=cns),
        outputs=dict(output=output),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def export_tool(
    *,
    cns: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Convert copy number ratio tables (.cnr files) or segments (.cns) to another format.

    Args:
        cns: Path to the cns or cnr file(s).
        output: Desired output file format (bed/vcf/vcf.gz/cdt/seq).
        extra (optional): Additional parameters that will be forwarded to cnvkit export.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_export(
        cns=cns,
        output=output,
        extra=extra,
         
    )
