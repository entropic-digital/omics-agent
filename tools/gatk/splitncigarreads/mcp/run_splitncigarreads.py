from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_splitncigarreads(
    *,
    bam_file: str,
    split_bam_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk SplitNCigarReads.

    Args:
        bam_file: Path to the input BAM file.
        split_bam_file: Path to the output split BAM file.
        java_opts (optional): Additional arguments for the Java compiler (excluding -XmX and -Djava.io.tmpdir).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/gatk/splitncigarreads",
        inputs=dict(bam_file=bam_file),
        outputs=dict(split_bam_file=split_bam_file),
        params={"java_opts": java_opts, "extra": extra},
         
    )


@collect_tool()
def splitncigarreads(
    *,
    bam_file: str,
    split_bam_file: str,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk SplitNCigarReads.

    Args:
        bam_file: Path to the input BAM file.
        split_bam_file: Path to the output split BAM file.
        java_opts (optional): Additional arguments for the Java compiler (excluding -XmX and -Djava.io.tmpdir).
        extra (optional): Additional program arguments.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_splitncigarreads(
        bam_file=bam_file,
        split_bam_file=split_bam_file,
        java_opts=java_opts,
        extra=extra,
         
    )
