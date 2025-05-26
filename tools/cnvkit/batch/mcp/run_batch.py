from typing import Optional, List
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_batch(
    *,
    bam: List[str],
    reference: Optional[str] = None,
    fasta: Optional[str] = None,
    antitarget: Optional[str] = None,
    target: Optional[str] = None,
    mappability: Optional[str] = None,
    method: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the CNVkit pipeline on BAM files to call cnv alterations or generate a new reference file.

    Args:
        bam: One or more BAM files.
        reference (optional): Copy reference file, when calling samples.
        fasta (optional): Reference genome, when building a new reference.
        antitarget (optional): BED antitarget file, when building a new reference.
        target (optional): BED target file, when building a new reference.
        mappability (optional): Mappability file, when building a new reference.
        method (optional): Method parameter for CNVkit, defaulting to CNVkit's internal value if unset.
        extra (optional): Additional arguments to pass.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"bam": bam}
    if reference:
        inputs["reference"] = reference
    if fasta:
        inputs["fasta"] = fasta
    if antitarget:
        inputs["antitarget"] = antitarget
    if target:
        inputs["target"] = target
    if mappability:
        inputs["mappability"] = mappability

    params = {}
    if method:
        params["method"] = method
    if extra:
        params["extra"] = extra

    return run_snake_wrapper(
        wrapper="file:tools/cnvkit/batch",
        inputs=inputs,
        params=params,
         
    )


@collect_tool()
def batch(
    *,
    bam: List[str],
    reference: Optional[str] = None,
    fasta: Optional[str] = None,
    antitarget: Optional[str] = None,
    target: Optional[str] = None,
    mappability: Optional[str] = None,
    method: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run the CNVkit pipeline on BAM files to call cnv alterations or generate a new reference file.

    Args:
        bam: One or more BAM files.
        reference (optional): Copy reference file, when calling samples.
        fasta (optional): Reference genome, when building a new reference.
        antitarget (optional): BED antitarget file, when building a new reference.
        target (optional): BED target file, when building a new reference.
        mappability (optional): Mappability file, when building a new reference.
        method (optional): Method parameter for CNVkit, defaulting to CNVkit's internal value if unset.
        extra (optional): Additional arguments to pass.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_batch(
        bam=bam,
        reference=reference,
        fasta=fasta,
        antitarget=antitarget,
        target=target,
        mappability=mappability,
        method=method,
        extra=extra,
         
    )
