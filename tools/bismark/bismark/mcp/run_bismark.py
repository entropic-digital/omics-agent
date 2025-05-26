from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_bismark(
    *,
    fq: Optional[str] = None,
    fq_1: Optional[str] = None,
    fq_2: Optional[str] = None,
    bismark_indexes_dir: str,
    genomic_freqs: Optional[str] = None,
    extra: Optional[str] = None,
    bam: Optional[str] = None,
    sam: Optional[str] = None,
    cram: Optional[str] = None,
    report: str,
    nucleotide_stats: Optional[str] = None,
    fq_unmapped: Optional[str] = None,
    fq_ambiguous: Optional[str] = None,
    bam_ambiguous: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Align bisulfite sequencing reads using Bismark.

    Args:
        fq (optional): For single end data, path to the read file.
        fq_1 (optional): For paired-end data, path to the first read file.
        fq_2 (optional): For paired-end data, path to the second read file.
        bismark_indexes_dir: Path to the folder containing `Bisulfite_Genome`.
        genomic_freqs (optional): Path to a `genomic_nucleotide_frequencies.txt` file.
        extra (optional): Additional arguments for Bismark.
        bam (optional): Output BAM file.
        sam (optional): Output SAM file.
        cram (optional): Output CRAM file.
        report: Path to the alignment report file.
        nucleotide_stats (optional): Path to the nucleotide stats file.
        fq_unmapped (optional): Path to write unmapped reads.
        fq_ambiguous (optional): Path to write ambiguously mapped reads.
        bam_ambiguous (optional): Path to write mappings for ambiguously mapped reads.
  
    Returns:
        subprocess.CompletedProcess: Information about the completed Snakemake process.
    """
    inputs = {}
    if fq:
        inputs["fq"] = fq
    if fq_1:
        inputs["fq_1"] = fq_1
    if fq_2:
        inputs["fq_2"] = fq_2
    inputs["bismark_indexes_dir"] = bismark_indexes_dir
    if genomic_freqs:
        inputs["genomic_freqs"] = genomic_freqs

    outputs = {"report": report}
    if bam:
        outputs["bam"] = bam
    if sam:
        outputs["sam"] = sam
    if cram:
        outputs["cram"] = cram
    if nucleotide_stats:
        outputs["nucleotide_stats"] = nucleotide_stats
    if fq_unmapped:
        outputs["fq_unmapped"] = fq_unmapped
    if fq_ambiguous:
        outputs["fq_ambiguous"] = fq_ambiguous
    if bam_ambiguous:
        outputs["bam_ambiguous"] = bam_ambiguous

    params = {"extra": extra} if extra else {}

    return run_snake_wrapper(
        wrapper="file:tools/bismark",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def bismark(
    *,
    fq: Optional[str] = None,
    fq_1: Optional[str] = None,
    fq_2: Optional[str] = None,
    bismark_indexes_dir: str,
    genomic_freqs: Optional[str] = None,
    extra: Optional[str] = None,
    bam: Optional[str] = None,
    sam: Optional[str] = None,
    cram: Optional[str] = None,
    report: str,
    nucleotide_stats: Optional[str] = None,
    fq_unmapped: Optional[str] = None,
    fq_ambiguous: Optional[str] = None,
    bam_ambiguous: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Align bisulfite sequencing reads using Bismark.

    Args:
        fq (optional): For single end data, path to the read file.
        fq_1 (optional): For paired-end data, path to the first read file.
        fq_2 (optional): For paired-end data, path to the second read file.
        bismark_indexes_dir: Path to the folder containing `Bisulfite_Genome`.
        genomic_freqs (optional): Path to a `genomic_nucleotide_frequencies.txt` file.
        extra (optional): Additional arguments for Bismark.
        bam (optional): Output BAM file.
        sam (optional): Output SAM file.
        cram (optional): Output CRAM file.
        report: Path to the alignment report file.
        nucleotide_stats (optional): Path to the nucleotide stats file.
        fq_unmapped (optional): Path to write unmapped reads.
        fq_ambiguous (optional): Path to write ambiguously mapped reads.
        bam_ambiguous (optional): Path to write mappings for ambiguously mapped reads.
  
    Returns:
        subprocess.CompletedProcess: Information about the completed Snakemake process.
    """
    return run_bismark(
        fq=fq,
        fq_1=fq_1,
        fq_2=fq_2,
        bismark_indexes_dir=bismark_indexes_dir,
        genomic_freqs=genomic_freqs,
        extra=extra,
        bam=bam,
        sam=sam,
        cram=cram,
        report=report,
        nucleotide_stats=nucleotide_stats,
        fq_unmapped=fq_unmapped,
        fq_ambiguous=fq_ambiguous,
        bam_ambiguous=bam_ambiguous,
         
    )
