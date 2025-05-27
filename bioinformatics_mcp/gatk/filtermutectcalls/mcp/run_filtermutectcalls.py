from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_filtermutectcalls(
    *,
    vcf: str,
    ref: str,
    vcf_out: str,
    stats_out: Optional[str] = None,
    aln: Optional[str] = None,
    contamination: Optional[str] = None,
    segmentation: Optional[str] = None,
    f1r2: Optional[str] = None,
    intervals: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk FilterMutectCalls to filter variants in a Mutect2 VCF callset.

    Args:
        vcf: Path to VCF file (pbgzipped, indexed).
        ref: Path to reference genome (with .dict file alongside).
        vcf_out: Filtered VCF file output path.
        stats_out (optional): Optional stats from Mutect2.
        aln (optional): Optional path to SAM/BAM/CRAM files.
        contamination (optional): Optional path to contamination table.
        segmentation (optional): Optional path to tumor segments.
        f1r2 (optional): Optional path to prior artefact (tar.gz2).
        intervals (optional): Optional file containing BED intervals.
        java_opts (optional): Java options for the GATK process.
        extra (optional): Additional program arguments for GATK FilterMutectCalls.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {"vcf": vcf, "ref": ref}
    if aln:
        inputs["aln"] = aln
    if contamination:
        inputs["contamination"] = contamination
    if segmentation:
        inputs["segmentation"] = segmentation
    if f1r2:
        inputs["f1r2"] = f1r2
    if intervals:
        inputs["intervals"] = intervals

    params = {}
    if java_opts:
        params["java_opts"] = java_opts
    if extra:
        params["extra"] = extra

    outputs = {"vcf_out": vcf_out}
    if stats_out:
        outputs["stats_out"] = stats_out

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/gatk/filtermutectcalls",
        inputs=inputs,
        params=params,
        outputs=outputs,
         
    )


@collect_tool()
def filtermutectcalls(
    *,
    vcf: str,
    ref: str,
    vcf_out: str,
    stats_out: Optional[str] = None,
    aln: Optional[str] = None,
    contamination: Optional[str] = None,
    segmentation: Optional[str] = None,
    f1r2: Optional[str] = None,
    intervals: Optional[str] = None,
    java_opts: Optional[str] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Run gatk FilterMutectCalls to filter variants in a Mutect2 VCF callset.

    Args:
        vcf: Path to VCF file (pbgzipped, indexed).
        ref: Path to reference genome (with .dict file alongside).
        vcf_out: Filtered VCF file output path.
        stats_out (optional): Optional stats from Mutect2.
        aln (optional): Optional path to SAM/BAM/CRAM files.
        contamination (optional): Optional path to contamination table.
        segmentation (optional): Optional path to tumor segments.
        f1r2 (optional): Optional path to prior artefact (tar.gz2).
        intervals (optional): Optional file containing BED intervals.
        java_opts (optional): Java options for the GATK process.
        extra (optional): Additional program arguments for GATK FilterMutectCalls.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_filtermutectcalls(
        vcf=vcf,
        ref=ref,
        vcf_out=vcf_out,
        stats_out=stats_out,
        aln=aln,
        contamination=contamination,
        segmentation=segmentation,
        f1r2=f1r2,
        intervals=intervals,
        java_opts=java_opts,
        extra=extra,
         
    )
