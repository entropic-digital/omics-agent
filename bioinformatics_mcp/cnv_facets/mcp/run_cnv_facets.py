from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_cnv_facets(
    *,
    tumor: Optional[str] = None,
    normal: Optional[str] = None,
    vcf: str,
    pileup: Optional[str] = None,
    output_vcf: str,
    cnv: str,
    hist: str,
    spider: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Detects somatic copy number variants (CNVs) using cnv_facets.

    Args:
        tumor: Path to tumor aligned reads. (BAM, required if `pileup` is empty)
        normal: Path to normal aligned reads. (BAM, required if `pileup` is empty)
        vcf: Path to common, polymorphic SNPs. (pbgzip VCF)
        pileup: Path to pileup variants. (pbgzip CSV, replaces `tumor` and `normal`)
        output_vcf: Path to copy number variants. (pbgzip VCF)
        cnv: Path to a summary plot of CNVs across the genome. (PNG)
        hist: Path to histograms of the distribution of read depth across all the position
              in the tumour and normal sample, before and after filtering positions. (PDF)
        spider: Path to a diagnostic plot to check how well the copy number fits work (PDF)
        extra: Optional parameters given to `cnv_facets`, besides `-t`, `-n`, `-vcf` and `-o`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    inputs = {
        "tumor": tumor,
        "normal": normal,
        "vcf": vcf,
        "pileup": pileup,
    }
    outputs = {
        "vcf": output_vcf,
        "cnv": cnv,
        "hist": hist,
        "spider": spider,
    }
    params = {"extra": extra} if extra else {}

    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/cnv_facets",
        inputs=inputs,
        outputs=outputs,
        params=params,
         
    )


@collect_tool()
def cnv_facets(
    *,
    tumor: Optional[str] = None,
    normal: Optional[str] = None,
    vcf: str,
    pileup: Optional[str] = None,
    output_vcf: str,
    cnv: str,
    hist: str,
    spider: str,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Detects somatic copy number variants (CNVs) using cnv_facets.

    Args:
        tumor: Path to tumor aligned reads. (BAM, required if `pileup` is empty)
        normal: Path to normal aligned reads. (BAM, required if `pileup` is empty)
        vcf: Path to common, polymorphic SNPs. (pbgzip VCF)
        pileup: Path to pileup variants. (pbgzip CSV, replaces `tumor` and `normal`)
        output_vcf: Path to copy number variants. (pbgzip VCF)
        cnv: Path to a summary plot of CNVs across the genome. (PNG)
        hist: Path to histograms of the distribution of read depth across all the position
              in the tumour and normal sample, before and after filtering positions. (PDF)
        spider: Path to a diagnostic plot to check how well the copy number fits work (PDF)
        extra: Optional parameters given to `cnv_facets`, besides `-t`, `-n`, `-vcf` and `-o`.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_cnv_facets(
        tumor=tumor,
        normal=normal,
        vcf=vcf,
        pileup=pileup,
        output_vcf=output_vcf,
        cnv=cnv,
        hist=hist,
        spider=spider,
        extra=extra,
         
    )
