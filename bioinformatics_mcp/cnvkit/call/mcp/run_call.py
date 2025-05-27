from typing import Optional
import subprocess
from bioinformatics_mcp.tool_decorator import collect_tool
from bioinformatics_mcp.core.snake_wrapper import run_snake_wrapper


def run_call(
    *,
    segments: str,
    vcf: str,
    output_segments: str,
    filter: Optional[str] = None,
    purity: Optional[float] = None,
    ploidy: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Given segmented log2 ratio estimates (.cns), derive each segment’s absolute integer copy number.

    Args:
        segments: Input file containing copy ratios (.cnr or .cns).
        vcf: VCF file name containing variants for calculation of b-allele frequencies.
        output_segments: Output table file name (CNR-like table of segments, .cns).
        filter (optional): Merge segments flagged by the specified filter(s) with the adjacent segment(s).
        purity (optional): Purity value of the tumor.
        ploidy (optional): Ploidy of the sample cells.
        extra (optional): Additional parameters that will be forwarded to cnvkit call.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_snake_wrapper(
        wrapper="file:bioinformatics_mcp/cnvkit/call",
        inputs=dict(segments=segments, vcf=vcf),
        outputs=dict(segments=output_segments),
        params={
            "filter": filter,
            "purity": purity,
            "ploidy": ploidy,
            "extra": extra,
        },
         
    )


@collect_tool()
def call(
    *,
    segments: str,
    vcf: str,
    output_segments: str,
    filter: Optional[str] = None,
    purity: Optional[float] = None,
    ploidy: Optional[int] = None,
    extra: Optional[str] = None,
     
) -> subprocess.CompletedProcess:
    """
    Given segmented log2 ratio estimates (.cns), derive each segment’s absolute integer copy number.

    Args:
        segments: Input file containing copy ratios (.cnr or .cns).
        vcf: VCF file name containing variants for calculation of b-allele frequencies.
        output_segments: Output table file name (CNR-like table of segments, .cns).
        filter (optional): Merge segments flagged by the specified filter(s) with the adjacent segment(s).
        purity (optional): Purity value of the tumor.
        ploidy (optional): Ploidy of the sample cells.
        extra (optional): Additional parameters that will be forwarded to cnvkit call.
  
    Returns:
        CompletedProcess instance containing information about the completed Snakemake process.
    """
    return run_call(
        segments=segments,
        vcf=vcf,
        output_segments=output_segments,
        filter=filter,
        purity=purity,
        ploidy=ploidy,
        extra=extra,
         
    )
