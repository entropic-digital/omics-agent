from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_extract(
    *,
    ref: str,
    aln: str,
    cpg: str,
    chg: Optional[str] = None,
    chh: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate per-base CpG metrics with MethylDackel.

    Args:
        ref: Path to reference genome (Fasta).
        aln: Path to aligned reads (BAM).
        cpg: Path to CpG metrics (BedGraph).
        chg (optional): Optional path to CHG metrics (BedGraph).
        chh (optional): Optional path to CHH metrics (BedGraph).
        extra (optional): Optional parameters provided to `MethylDackel extract`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    params = {"extra": extra} if extra else {}
    outputs = {"cpg": cpg}
    if chg:
        outputs["chg"] = chg
    if chh:
        outputs["chh"] = chh

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/methyldackel/extract",
        inputs=dict(ref=ref, aln=aln),
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def extract(
    *,
    ref: str,
    aln: str,
    cpg: str,
    chg: Optional[str] = None,
    chh: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Calculate per-base CpG metrics with MethylDackel.

    Args:
        ref: Path to reference genome (Fasta).
        aln: Path to aligned reads (BAM).
        cpg: Path to CpG metrics (BedGraph).
        chg (optional): Optional path to CHG metrics (BedGraph).
        chh (optional): Optional path to CHH metrics (BedGraph).
        extra (optional): Optional parameters provided to `MethylDackel extract`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_extract(
        ref=ref,
        aln=aln,
        cpg=cpg,
        chg=chg,
        chh=chh,
        extra=extra,
         
    )
