from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_indexcov(
    *,
    aln: str,
    fai: str,
    html: Optional[str] = None,
    bed: Optional[str] = None,
    ped: Optional[str] = None,
    roc: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Quickly estimate coverage from a whole-genome BAM or CRAM index.

    Args:
        aln: Path to indexed BAM/CRAM file.
        fai: Path to fasta sequence index.
        html (optional): Optional path to HTML report.
        bed (optional): Optional path to coverage BED.
        ped (optional): Optional path to pedigree file.
        roc (optional): Optional path to coverage curves.
        extra (optional): Additional parameters not including `-d` or `-r`.
            
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    outputs = {
        "html": html,
        "bed": bed,
        "ped": ped,
        "roc": roc,
    }
    outputs = {key: value for key, value in outputs.items() if value is not None}

    params = {"extra": extra} if extra else {}

    return run_snake_wrapper(
        wrapper="file:tools/goleft/indexcov",
        inputs=dict(aln=aln, fai=fai),
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def indexcov(
    *,
    aln: str,
    fai: str,
    html: Optional[str] = None,
    bed: Optional[str] = None,
    ped: Optional[str] = None,
    roc: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Quickly estimate coverage from a whole-genome BAM or CRAM index.

    Args:
        aln: Path to indexed BAM/CRAM file.
        fai: Path to fasta sequence index.
        html (optional): Optional path to HTML report.
        bed (optional): Optional path to coverage BED.
        ped (optional): Optional path to pedigree file.
        roc (optional): Optional path to coverage curves.
        extra (optional): Additional parameters not including `-d` or `-r`.
            
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_indexcov(
        aln=aln,
        fai=fai,
        html=html,
        bed=bed,
        ped=ped,
        roc=roc,
        extra=extra,
         
    )
