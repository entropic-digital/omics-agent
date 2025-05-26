from typing import Optional
import subprocess
from tools.tool_decorator import collect_tool
from core.snake_wrapper import run_snake_wrapper


def run_haplotag(
    *,
    vcf: str,
    vcf_index: str,
    aln: str,
    aln_index: str,
    ref: str,
    ref_index: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Phase BAM records by haplotype using WhatsHap.

    Args:
        vcf: Path to VCF.gz/BCF file of phased SNPs.
        vcf_index: Path to VCF index file (.tbi for VCF.gz, .csi for BCF).
        aln: Path to alignments for the sample in BAM/CRAM format.
        aln_index: Path to alignment index file in .bai/.crai format.
        ref: Path to FASTA reference used to create VCF file.
        ref_index: Path to FASTA index file in .fai format.
        output: Path to output phased BAM file.
        extra (optional): Additional program arguments (e.g., `--ignore-linked-read`,
                          `--linked-read-distance-cutoff`, `--ignore-read-groups`,
                          `--sample SAMPLE`, `--tag-supplementary`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:tools/whatshap/haplotag",
        inputs={
            "vcf": vcf,
            "vcf_index": vcf_index,
            "aln": aln,
            "aln_index": aln_index,
            "ref": ref,
            "ref_index": ref_index,
        },
        outputs={"output": output},
        params={"extra": extra} if extra else {},
         
    )


@collect_tool()
def haplotag(
    *,
    vcf: str,
    vcf_index: str,
    aln: str,
    aln_index: str,
    ref: str,
    ref_index: str,
    output: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Phase BAM records by haplotype using WhatsHap.

    Args:
        vcf: Path to VCF.gz/BCF file of phased SNPs.
        vcf_index: Path to VCF index file (.tbi for VCF.gz, .csi for BCF).
        aln: Path to alignments for the sample in BAM/CRAM format.
        aln_index: Path to alignment index file in .bai/.crai format.
        ref: Path to FASTA reference used to create VCF file.
        ref_index: Path to FASTA index file in .fai format.
        output: Path to output phased BAM file.
        extra (optional): Additional program arguments (e.g., `--ignore-linked-read`,
                          `--linked-read-distance-cutoff`, `--ignore-read-groups`,
                          `--sample SAMPLE`, `--tag-supplementary`).
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_haplotag(
        vcf=vcf,
        vcf_index=vcf_index,
        aln=aln,
        aln_index=aln_index,
        ref=ref,
        ref_index=ref_index,
        output=output,
        extra=extra,
         
    )
