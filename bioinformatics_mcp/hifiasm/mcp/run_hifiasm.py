from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_hifiasm(
    *,
    pacbio_hifi_reads: str,
    hic_reads: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    A haplotype-resolved assembler for accurate Hifi reads.

    Args:
        pacbio_hifi_reads: Path to the PacBio HiFi reads in FASTA format.
        hic_reads (optional): Path to the Hi-C reads in FASTQ format, if available.
        extra (optional): Additional program arguments for customization.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/hifiasm",
        inputs=dict(pacbio_hifi_reads=pacbio_hifi_reads, hic_reads=hic_reads),
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def hifiasm(
    *,
    pacbio_hifi_reads: str,
    hic_reads: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    A haplotype-resolved assembler for accurate Hifi reads.

    Args:
        pacbio_hifi_reads: Path to the PacBio HiFi reads in FASTA format.
        hic_reads (optional): Path to the Hi-C reads in FASTQ format, if available.
        extra (optional): Additional program arguments for customization.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_hifiasm(
        pacbio_hifi_reads=pacbio_hifi_reads,
        hic_reads=hic_reads,
        extra=extra,
         
    )
