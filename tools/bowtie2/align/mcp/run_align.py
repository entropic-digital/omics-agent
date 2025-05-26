from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_align(
    *,
    sample: str,
    idx: str,
    ref: Optional[str] = None,
    ref_fai: Optional[str] = None,
    sam_bam_cram: str,
    idx_out: Optional[str] = None,
    metrics: Optional[str] = None,
    unaligned: Optional[str] = None,
    unpaired: Optional[str] = None,
    unconcordant: Optional[str] = None,
    concordant: Optional[str] = None,
    extra: Optional[str] = None,
    interleaved: bool = False,
     
) -> subprocess.CompletedProcess:
    """
    Map reads with Bowtie2.

    Args:
        sample: FASTQ file(s) containing the reads to map.
        idx: Path to Bowtie2 indexed reference index.
        ref (optional): Optional path to genome sequence (FASTA).
        ref_fai (optional): Optional path to reference genome sequence index (FAI).
        sam_bam_cram: Path to the output SAM/BAM/CRAM file.
        idx_out (optional): Optional path to the BAM index.
        metrics (optional): Optional path to metrics file.
        unaligned (optional): Optional path to unaligned unpaired reads.
        unpaired (optional): Optional path to unpaired reads that aligned at least once.
        unconcordant (optional): Optional path to pairs that didn't align concordantly.
        concordant (optional): Optional path to pairs that aligned concordantly at least once.
        extra (optional): Additional program arguments for Bowtie2.
        interleaved (optional): Indicates if the input `sample` contains interleaved paired-end FASTQ/FASTA reads.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/bowtie2/align",
        inputs=dict(sample=sample, idx=idx, ref=ref, ref_fai=ref_fai),
        outputs=dict(
            sam_bam_cram=sam_bam_cram,
            idx=idx_out,
            metrics=metrics,
            unaligned=unaligned,
            unpaired=unpaired,
            unconcordant=unconcordant,
            concordant=concordant,
        ),
        params={
            "extra": extra,
            "interleaved": interleaved,
        },
         
    )


@collect_tool()
def align(
    *,
    sample: str,
    idx: str,
    ref: Optional[str] = None,
    ref_fai: Optional[str] = None,
    sam_bam_cram: str,
    idx_out: Optional[str] = None,
    metrics: Optional[str] = None,
    unaligned: Optional[str] = None,
    unpaired: Optional[str] = None,
    unconcordant: Optional[str] = None,
    concordant: Optional[str] = None,
    extra: Optional[str] = None,
    interleaved: bool = False,
     
) -> subprocess.CompletedProcess:
    """
    Map reads with Bowtie2.

    Args:
        sample: FASTQ file(s) containing the reads to map.
        idx: Path to Bowtie2 indexed reference index.
        ref (optional): Optional path to genome sequence (FASTA).
        ref_fai (optional): Optional path to reference genome sequence index (FAI).
        sam_bam_cram: Path to the output SAM/BAM/CRAM file.
        idx_out (optional): Optional path to the BAM index.
        metrics (optional): Optional path to metrics file.
        unaligned (optional): Optional path to unaligned unpaired reads.
        unpaired (optional): Optional path to unpaired reads that aligned at least once.
        unconcordant (optional): Optional path to pairs that didn't align concordantly.
        concordant (optional): Optional path to pairs that aligned concordantly at least once.
        extra (optional): Additional program arguments for Bowtie2.
        interleaved (optional): Indicates if the input `sample` contains interleaved paired-end FASTQ/FASTA reads.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_align(
        sample=sample,
        idx=idx,
        ref=ref,
        ref_fai=ref_fai,
        sam_bam_cram=sam_bam_cram,
        idx_out=idx_out,
        metrics=metrics,
        unaligned=unaligned,
        unpaired=unpaired,
        unconcordant=unconcordant,
        concordant=concordant,
        extra=extra,
        interleaved=interleaved,
         
    )
