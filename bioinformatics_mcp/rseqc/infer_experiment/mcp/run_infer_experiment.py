from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_infer_experiment(
    *,
    aln: str,
    refgene: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Report read strandiness and endeness.

    Args:
        aln: Path to SAM/BAM alignment file.
        refgene: Path to reference gene model in bed format.
        output: Path to text formatted results.
        extra (optional): Optional parameters for `infer_experiment.py` other than `-i` or `-r`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/rseqc/infer_experiment",
        inputs=dict(aln=aln, refgene=refgene),
        outputs=dict(output=output),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def infer_experiment(
    *,
    aln: str,
    refgene: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Report read strandiness and endeness.

    Args:
        aln: Path to SAM/BAM alignment file.
        refgene: Path to reference gene model in bed format.
        output: Path to text formatted results.
        extra (optional): Optional parameters for `infer_experiment.py` other than `-i` or `-r`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_infer_experiment(
        aln=aln,
        refgene=refgene,
        output=output,
        extra=extra,
         
    )
