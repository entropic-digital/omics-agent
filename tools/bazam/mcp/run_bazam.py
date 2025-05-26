from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bazam(
    *,
    bam: str,
    reference: Optional[str] = None,
    reads: Optional[str] = None,
    r1: Optional[str] = None,
    r2: Optional[str] = None,
    extra: Optional[str] = None,
    java_opts: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Bazam: A smarter way to realign reads from one genome to another.

    Args:
        bam: Path to mapping file (BAM/CRAM formatted).
        reference (optional): Optional path to reference genome sequence (FASTA formatted). Required for CRAM input.
        reads (optional): Path to realigned reads (single-ended or interleaved) (FASTQ formatted).
        r1 (optional): Path to upstream reads (FASTQ formatted).
        r2 (optional): Path to downstream reads (FASTQ formatted).
        extra (optional): Optional parameters passed to `bazam`.
        java_opts (optional): Additional arguments passed to the java compiler (not for `-XmX` or `-Djava.io.tmpdir`).
  
    Notes:
        Output files include either paths to both `r1` and `r2`, or a single path to `reads`.
        This wrapper/tool does not handle multithreading.

    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    outputs = {"reads": reads} if reads else {"r1": r1, "r2": r2}
    params = {"extra": extra, "java_opts": java_opts} if extra or java_opts else {}

    return run_snake_wrapper(
        wrapper="file:tools/bazam",
        inputs={"bam": bam, "reference": reference} if reference else {"bam": bam},
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def bazam(
    *,
    bam: str,
    reference: Optional[str] = None,
    reads: Optional[str] = None,
    r1: Optional[str] = None,
    r2: Optional[str] = None,
    extra: Optional[str] = None,
    java_opts: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Bazam: A smarter way to realign reads from one genome to another.

    Args:
        bam: Path to mapping file (BAM/CRAM formatted).
        reference (optional): Optional path to reference genome sequence (FASTA formatted). Required for CRAM input.
        reads (optional): Path to realigned reads (single-ended or interleaved) (FASTQ formatted).
        r1 (optional): Path to upstream reads (FASTQ formatted).
        r2 (optional): Path to downstream reads (FASTQ formatted).
        extra (optional): Optional parameters passed to `bazam`.
        java_opts (optional): Additional arguments passed to the java compiler (not for `-XmX` or `-Djava.io.tmpdir`).
  
    Notes:
        Output files include either paths to both `r1` and `r2`, or a single path to `reads`.
        This wrapper/tool does not handle multithreading.

    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_bazam(
        bam=bam,
        reference=reference,
        reads=reads,
        r1=r1,
        r2=r2,
        extra=extra,
        java_opts=java_opts,
         
    )
