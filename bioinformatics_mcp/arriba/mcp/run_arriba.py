from typing import Optional
import subprocess

from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_arriba(
    *,
    bam: str,
    genome: str,
    annotation: str,
    fusions: str,
    known_fusions: Optional[str] = None,
    blacklist: Optional[str] = None,
    sv_file: Optional[str] = None,
    extra: str = "",
    threads: int = 1,
     
) -> subprocess.CompletedProcess:
    """Run the Snakemake Arriba wrapper with the given arguments."""
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/arriba",
        inputs=dict(bam=bam, genome=genome, annotation=annotation),
        outputs=dict(fusions=fusions),
        params={
            **({"known_fusions": known_fusions} if known_fusions else {}),
            **({"blacklist": blacklist} if blacklist else {}),
            **({"sv_file": sv_file} if sv_file else {}),
            "extra": extra,
        },
        threads=threads,
         
    )


@collect_tool()
def arriba(
    *,
    bam: str,
    genome: str,
    annotation: str,
    fusions: str,
    known_fusions: Optional[str] = None,
    blacklist: Optional[str] = None,
    sv_file: Optional[str] = None,
    extra: str = "",
     
) -> subprocess.CompletedProcess:
    """
    Detect gene fusions from chimeric STAR output using Arriba.

    Args:
        bam: Path to bam formatted alignment file from STAR
        genome: Path to fasta formatted genome sequence
        annotation: Path to GTF formatted genome annotation
        fusions: Path to output fusion file
        known_fusions (optional): Path to known fusions file. See Arriba documentation for more information
        blacklist (optional): Path to blacklist file. See Arriba documentation for more information
        sv_file (optional): Path to structural variations calls from WGS. See Arriba documentation for more information
        extra (optional): Additional optional parameters for Arriba. Defaults to ""
           
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process
    """
    return run_arriba(
        bam=bam,
        genome=genome,
        annotation=annotation,
        fusions=fusions,
        known_fusions=known_fusions,
        blacklist=blacklist,
        sv_file=sv_file,
        extra=extra,
         
    )
