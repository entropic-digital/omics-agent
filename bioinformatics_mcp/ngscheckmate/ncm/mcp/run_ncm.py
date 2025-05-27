from typing import Optional, Union, List
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_ncm(
    *,
    samples: Union[str, List[str]],
    bed: Optional[str] = None,
    pt: Optional[str] = None,
    pdf: str,
    matched: str,
    txt: str,
    matrix: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    NGS-Checkmate: Identify BAM/VCF/Fastq files that belong to the same individuals.

    Args:
        samples: Either a path to a list-file, or list of paths to alignment (BAM/SAM) files,
                 list of paths to variants files (VCF/BCF), or list of paths to FastQ files.
        bed: Path to an interval (BED) file, required for VCF/BAM input.
        pt: Path to a pattern file, required for FastQ input.
        pdf: Path to plot file (PDF formatted).
        matched: Path to matched samples table.
        txt: Path to samples description.
        matrix: Path to samples matrix (metrics).
        extra: Optional parameters besides IO and threading.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"samples": samples}
    if bed:
        inputs["bed"] = bed
    if pt:
        inputs["pt"] = pt

    outputs = {
        "pdf": pdf,
        "matched": matched,
        "txt": txt,
        "matrix": matrix,
    }

    params = {}
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/ngscheckmate/ncm",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def ncm(
    *,
    samples: Union[str, List[str]],
    bed: Optional[str] = None,
    pt: Optional[str] = None,
    pdf: str,
    matched: str,
    txt: str,
    matrix: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    NGS-Checkmate: Identify BAM/VCF/Fastq files that belong to the same individuals.

    Args:
        samples: Either a path to a list-file, or list of paths to alignment (BAM/SAM) files,
                 list of paths to variants files (VCF/BCF), or list of paths to FastQ files.
        bed: Path to an interval (BED) file, required for VCF/BAM input.
        pt: Path to a pattern file, required for FastQ input.
        pdf: Path to plot file (PDF formatted).
        matched: Path to matched samples table.
        txt: Path to samples description.
        matrix: Path to samples matrix (metrics).
        extra: Optional parameters besides IO and threading.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_ncm(
        samples=samples,
        bed=bed,
        pt=pt,
        pdf=pdf,
        matched=matched,
        txt=txt,
        matrix=matrix,
        extra=extra,
         
    )
